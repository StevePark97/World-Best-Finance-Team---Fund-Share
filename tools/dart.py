#!/usr/bin/env python3
"""금감원 DART OpenAPI에서 국내 상장사 연간 재무(사업보고서) 추출.
사용법: DART_API_KEY=... python3 tools/dart.py 005930 [--years 5] [--fs CFS|OFS]
API 키 발급(무료): https://opendart.fss.or.kr
"""
import argparse, io, json, os, sys, urllib.parse, urllib.request, zipfile, datetime
import xml.etree.ElementTree as ET

KEY = os.environ.get("DART_API_KEY")
BASE = "https://opendart.fss.or.kr/api"
CACHE = os.path.join(os.path.dirname(__file__), ".corpcode_cache.json")

ACCOUNTS = {
    "매출액": ["ifrs-full_Revenue", "매출액", "수익(매출액)", "영업수익"],
    "영업이익": ["dart_OperatingIncomeLoss", "영업이익", "영업이익(손실)"],
    "당기순이익": ["ifrs-full_ProfitLoss", "당기순이익", "당기순이익(손실)"],
    "지배주주순이익": ["ifrs-full_ProfitLossAttributableToOwnersOfParent"],
    "영업활동현금흐름": ["ifrs-full_CashFlowsFromUsedInOperatingActivities", "영업활동현금흐름", "영업활동으로 인한 현금흐름"],
    "유형자산취득": ["ifrs-full_PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities", "유형자산의 취득"],
    "자산총계": ["ifrs-full_Assets", "자산총계"],
    "부채총계": ["ifrs-full_Liabilities", "부채총계"],
    "자본총계": ["ifrs-full_Equity", "자본총계"],
    "현금및현금성자산": ["ifrs-full_CashAndCashEquivalents", "현금및현금성자산"],
}


def call(path, **params):
    params["crtfc_key"] = KEY
    url = f"{BASE}/{path}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read()


def corp_code(stock_code):
    if os.path.exists(CACHE):
        m = json.load(open(CACHE))
    else:
        z = zipfile.ZipFile(io.BytesIO(call("corpCode.xml")))
        root = ET.fromstring(z.read(z.namelist()[0]))
        m = {}
        for el in root.iter("list"):
            sc = (el.findtext("stock_code") or "").strip()
            if sc:
                m[sc] = [el.findtext("corp_code"), el.findtext("corp_name")]
        json.dump(m, open(CACHE, "w"), ensure_ascii=False)
    if stock_code not in m:
        sys.exit(f"종목코드 {stock_code}를 DART에서 찾지 못함")
    return m[stock_code]


def annual(cc, year, fs):
    raw = call("fnlttSinglAcntAll.json", corp_code=cc, bsns_year=str(year), reprt_code="11011", fs_div=fs)
    d = json.loads(raw)
    if d.get("status") != "000":
        return None, d.get("message")
    return d["list"], None


def pick(items, keys):
    for k in keys:
        for it in items:
            if it.get("account_id") == k or it.get("account_nm", "").strip() == k:
                v = (it.get("thstrm_amount") or "").replace(",", "")
                try:
                    return int(v)
                except ValueError:
                    pass
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stock_code")
    ap.add_argument("--years", type=int, default=5)
    ap.add_argument("--fs", default="CFS", help="CFS=연결, OFS=별도")
    a = ap.parse_args()
    if not KEY:
        sys.exit("DART_API_KEY 환경변수가 없습니다. https://opendart.fss.or.kr 에서 무료 발급 후 설정하세요.")
    cc, name = corp_code(a.stock_code)
    this_year = datetime.date.today().year
    data = {}
    for y in range(this_year - 1, this_year - 1 - a.years - 1, -1):
        items, err = annual(cc, y, a.fs)
        if items:
            data[y] = items
        if len(data) == a.years:
            break
    if not data:
        sys.exit("사업보고서 재무 데이터를 가져오지 못함")
    years = sorted(data)
    print(f"# {name} ({a.stock_code}) — DART corp_code {cc}, {'연결' if a.fs=='CFS' else '별도'}")
    print("출처: DART OpenAPI 단일회사 전체 재무제표(fnlttSinglAcntAll), 사업보고서(11011)\n")
    print("| 항목 (억원) | " + " | ".join(map(str, years)) + " |")
    print("|---|" + "---|" * len(years))
    for label, keys in ACCOUNTS.items():
        vals = []
        for y in years:
            v = pick(data[y], keys)
            vals.append("—" if v is None else f"{v/1e8:,.0f}")
        print(f"| {label} | " + " | ".join(vals) + " |")
    print("\n주의: 계정명은 회사마다 다를 수 있음. '—'는 원문 사업보고서에서 확인 필요.")


if __name__ == "__main__":
    main()
