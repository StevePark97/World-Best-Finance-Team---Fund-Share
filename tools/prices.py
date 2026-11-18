#!/usr/bin/env python3
"""주가 요약 (yfinance). 국장은 005930.KS(코스피) / 247540.KQ(코스닥) 형식.
사용법: python3 tools/prices.py NVDA 005930.KS
주의: Yahoo는 레이트리밋(429)이 잦음. 실패하면 리포트에 기록하고 다른 출처로 대체할 것.
"""
import sys, time

try:
    import yfinance as yf
except ImportError:
    sys.exit("pip install yfinance 필요")


def summary(t):
    for attempt in range(3):
        try:
            h = yf.Ticker(t).history(period="5y", auto_adjust=True)
            if h.empty:
                raise RuntimeError("빈 응답")
            break
        except Exception as e:
            if attempt == 2:
                return f"| {t} | 실패: {e} | | | | | |"
            time.sleep(5 * (attempt + 1))
    c = h["Close"]
    last = c.iloc[-1]
    y1 = c[c.index >= c.index[-1] - __import__("pandas").Timedelta(days=365)]
    ret = lambda days: (last / c[c.index <= c.index[-1] - __import__("pandas").Timedelta(days=days)].iloc[-1] - 1) * 100
    try:
        r1, r3, r5 = ret(365), ret(365 * 3), ret(365 * 5 - 10)
    except IndexError:
        r1 = r3 = r5 = float("nan")
    return (f"| {t} | {last:,.2f} | {c.index[-1].date()} | {y1.min():,.2f} ~ {y1.max():,.2f} | "
            f"{r1:+.1f}% | {r3:+.1f}% | {r5:+.1f}% |")


def main():
    print("| 티커 | 종가(수정) | 기준일 | 52주 범위 | 1년 | 3년 | 5년 |")
    print("|---|---|---|---|---|---|---|")
    for t in sys.argv[1:]:
        print(summary(t))
    print("\n출처: Yahoo Finance via yfinance (수정주가, 배당 재투자 미반영)")


if __name__ == "__main__":
    main()
