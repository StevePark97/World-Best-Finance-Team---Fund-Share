#!/usr/bin/env python3
"""FRED 시계열 최신값과 1년 전 대비 (API 키 불필요, CSV 다운로드).
사용법: python3 tools/fred.py DGS10 FEDFUNDS T10Y2Y CPIAUCSL UNRATE
"""
import csv, io, sys, urllib.request, datetime

NAMES = {
    "DGS10": "미국 10년물 국채금리(%)", "DGS2": "미국 2년물(%)", "FEDFUNDS": "연방기금금리(%)",
    "T10Y2Y": "10년-2년 스프레드(%p)", "CPIAUCSL": "CPI 지수", "UNRATE": "실업률(%)",
    "DEXKOUS": "원/달러 환율", "BAMLH0A0HYM2": "하이일드 스프레드(%)", "VIXCLS": "VIX",
}


def fetch(sid):
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}"
    with urllib.request.urlopen(url, timeout=30) as r:
        rows = list(csv.reader(io.StringIO(r.read().decode())))
    out = []
    for d, v in rows[1:]:
        try:
            out.append((datetime.date.fromisoformat(d), float(v)))
        except ValueError:
            continue
    return out


def main():
    ids = sys.argv[1:] or ["DGS10", "FEDFUNDS", "T10Y2Y", "CPIAUCSL", "UNRATE"]
    print("| 지표 | 최신값 | 기준일 | 1년 전 | 변화 | 출처 |")
    print("|---|---|---|---|---|---|")
    for sid in ids:
        try:
            s = fetch(sid)
        except Exception as e:
            print(f"| {sid} | 실패: {e} | | | | |")
            continue
        d, v = s[-1]
        target = d.replace(year=d.year - 1)
        prev = min(s, key=lambda x: abs((x[0] - target).days))
        chg = f"{(v/prev[1]-1)*100:+.1f}% (YoY)" if sid == "CPIAUCSL" else f"{v-prev[1]:+.2f}"
        print(f"| {NAMES.get(sid, sid)} | {v:,.2f} | {d} | {prev[1]:,.2f} | {chg} | FRED {sid} |")


if __name__ == "__main__":
    main()
