#!/usr/bin/env python3
"""SEC EDGAR XBRL에서 연간 핵심 재무 추출. 미국 기업(10-K, US GAAP)과
해외 ADR 기업(20-F, IFRS — 예: TSM, ASML)을 모두 지원.
사용법: python3 tools/sec_edgar.py AAPL [--years 5]
"""
import argparse, json, os, sys, urllib.request

UA = os.environ.get("SEC_USER_AGENT", "ai-analyst-team research-bot research@example.com")

CONCEPTS = {
    # US GAAP 태그 다음에 IFRS 태그 (태그 이름이 겹치지 않으므로 한 목록으로 처리)
    "매출": ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet",
             "Revenue", "RevenueFromContractsWithCustomers"],
    "영업이익": ["OperatingIncomeLoss", "ProfitLossFromOperatingActivities"],
    "순이익": ["NetIncomeLoss", "ProfitLossAttributableToOwnersOfParent", "ProfitLoss"],
    "희석EPS": ["EarningsPerShareDiluted", "DilutedEarningsLossPerShare", "DilutedEarningsLossPerShareFromContinuingOperations"],
    "영업현금흐름": ["NetCashProvidedByUsedInOperatingActivities", "CashFlowsFromUsedInOperatingActivities"],
    "CAPEX": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets",
              "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"],
    "SBC": ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense", "AdjustmentsForSharebasedPayments"],
    "자사주매입": ["PaymentsForRepurchaseOfCommonStock", "PaymentsToAcquireOrRedeemEntitysShares"],
    "총자산": ["Assets"],
    "자기자본": ["StockholdersEquity", "EquityAttributableToOwnersOfParent", "Equity"],
    "현금": ["CashAndCashEquivalentsAtCarryingValue", "CashAndCashEquivalents"],
    "장기부채": ["LongTermDebtNoncurrent", "LongTermDebt", "NoncurrentPortionOfNoncurrentBondsIssued",
                "LongtermBorrowings"],
    "희석주식수": ["WeightedAverageNumberOfDilutedSharesOutstanding", "AdjustedWeightedAverageShares"],
}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def cik_for(ticker):
    data = get("https://www.sec.gov/files/company_tickers.json")
    for row in data.values():
        if row["ticker"].upper() == ticker.upper():
            return str(row["cik_str"]).zfill(10), row["title"]
    sys.exit(f"티커 {ticker}를 SEC 목록에서 찾지 못함")


def _days(a, b):
    from datetime import date
    return (date.fromisoformat(b) - date.fromisoformat(a)).days


def annual_series(facts, names):
    """후보 태그 전부를 병합 (회사가 연도별로 태그를 바꾸는 경우 대응).
    흐름 항목은 기간이 약 1년(350~380일)인 10-K 수치만 사용, 분기 수치 배제."""
    gaap = {**facts["facts"].get("ifrs-full", {}), **facts["facts"].get("us-gaap", {})}
    out, used, unit_used = {}, [], None
    for name in names:
        if name not in gaap:
            continue
        units = gaap[name]["units"]
        # 통화가 여러 개면 가장 많이 보고된 단위 사용 (예: TWD vs USD 환산)
        unit = max(units, key=lambda u: len(units[u]))
        for f in units[unit]:
            if not str(f.get("form", "")).startswith(("10-K", "20-F")):
                continue
            if "start" in f and not (350 <= _days(f["start"], f["end"]) <= 380):
                continue
            key = f["end"]
            # 같은 기말: 앞선 후보 태그 우선, 같은 태그면 최신 접수본
            if key in out and out[key]["tag"] != name:
                continue
            if key not in out or f["filed"] > out[key]["filed"]:
                out[key] = {"val": f["val"], "filed": f["filed"], "accn": f["accn"], "tag": name}
        if name not in used and any(v["tag"] == name for v in out.values()):
            used.append(name)
            unit_used = unit_used or unit
    return "/".join(used) or None, unit_used, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ticker")
    ap.add_argument("--years", type=int, default=5)
    a = ap.parse_args()
    cik, title = cik_for(a.ticker)
    facts = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json")
    print(f"# {title} ({a.ticker.upper()}) — CIK {cik}")
    print(f"출처: SEC EDGAR XBRL companyfacts, https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json\n")
    rows = {}
    ends = set()
    for label, names in CONCEPTS.items():
        tag, unit, ser = annual_series(facts, names)
        rows[label] = (tag, unit, ser)
        ends.update(ser.keys())
    # 회계연도 말일은 매출 기준으로 정렬 (없으면 전체)
    base = rows["매출"][2] or rows["순이익"][2]
    periods = sorted(base.keys())[-a.years:] if base else sorted(ends)[-a.years:]
    print("| 항목 | 단위 | " + " | ".join(periods) + " | XBRL 태그 |")
    print("|---|---|" + "---|" * len(periods) + "---|")
    for label, (tag, unit, ser) in rows.items():
        vals = []
        for p in periods:
            v = ser.get(p, {}).get("val")
            if v is None:
                vals.append("—")
            elif unit and len(unit) == 3 and unit.isupper() and abs(v) >= 1e6:
                vals.append(f"{v/1e6:,.0f}M")
            elif unit == "shares":
                vals.append(f"{v/1e6:,.1f}M")
            else:
                vals.append(f"{v:,}")
        print(f"| {label} | {unit or '—'} | " + " | ".join(vals) + f" | {tag or '없음'} |")
    filed = sorted({v['filed'] for _, _, s in rows.values() for k, v in s.items() if k in periods})
    print(f"\n최신 연차보고서(10-K/20-F) 접수일: {filed[-1] if filed else '알 수 없음'}")
    print("주의: XBRL 태그는 회사마다 다를 수 있음. '—'는 해당 태그로 보고되지 않음을 뜻하며, 원문 10-K/20-F에서 확인 필요.")
    print("주의: 20-F(해외 기업)는 현지 통화 기준(예: TSM=TWD). ADR 1주가 보통주 몇 주인지(TSM은 1 ADR = 5주) 확인 후 EPS·주가 비교할 것.")
    print("주의: 각 연도 값은 해당 10-K 원본 기준이라 액면분할 이전 연도의 EPS·주식수는 분할 미반영. 주식수가 연도 간 수 배로 뛰면 분할 여부를 확인하고 조정할 것.")


if __name__ == "__main__":
    main()
