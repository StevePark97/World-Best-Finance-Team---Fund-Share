#!/usr/bin/env python3
"""한국은행 ECOS 주요 지표 최신값.
사용법: ECOS_API_KEY=... python3 tools/ecos.py
API 키 발급(무료): https://ecos.bok.or.kr/api/
통계표 코드는 ECOS '통계코드 검색'으로 확인 가능. 아래 코드는 키 발급 후 실제 응답으로 검증할 것.
"""
import json, os, sys, urllib.request, datetime

KEY = os.environ.get("ECOS_API_KEY")
# (이름, 통계표코드, 주기, 항목코드)
SERIES = [
    ("한국 기준금리(%)", "722Y001", "D", "0101000"),
    ("국고채 3년(%)", "817Y002", "D", "010200000"),
    ("국고채 10년(%)", "817Y002", "D", "010210000"),
    ("원/달러 환율(매매기준율)", "731Y001", "D", "0000001"),
]


def fetch(code, cycle, item):
    end = datetime.date.today()
    start = end - datetime.timedelta(days=400)
    url = (f"https://ecos.bok.or.kr/api/StatisticSearch/{KEY}/json/kr/1/1000/"
           f"{code}/{cycle}/{start:%Y%m%d}/{end:%Y%m%d}/{item}")
    with urllib.request.urlopen(url, timeout=30) as r:
        d = json.load(r)
    if "StatisticSearch" not in d:
        raise RuntimeError(d.get("RESULT", d))
    return d["StatisticSearch"]["row"]


def main():
    if not KEY:
        sys.exit("ECOS_API_KEY 환경변수가 없습니다. https://ecos.bok.or.kr/api/ 에서 무료 발급 후 설정하세요.")
    print("| 지표 | 최신값 | 기준일 | 약 1년 전 | 출처 |")
    print("|---|---|---|---|---|")
    for name, code, cyc, item in SERIES:
        try:
            rows = fetch(code, cyc, item)
            last, first = rows[-1], rows[0]
            print(f"| {name} | {last['DATA_VALUE']} | {last['TIME']} | {first['DATA_VALUE']} ({first['TIME']}) | ECOS {code}/{item} |")
        except Exception as e:
            print(f"| {name} | 실패: {e} | | | ECOS {code}/{item} |")


if __name__ == "__main__":
    main()
