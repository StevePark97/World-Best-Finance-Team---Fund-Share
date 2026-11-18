# 01_data — TSMC (TSM / 2330.TW)

- **작성:** 사원(데이터 담당) · **작성일:** 2026-11-18
- **데이터 기준일:** 주가 TSM 2026-11-17 종가 / 2330.TW 2026-11-18 종가, 환율 2026-11-18, 재무 2026-09-30(3Q26)까지, 월매출 2026년 10월분(2026-11-10 공시)까지
- **통화 표기:** NT$ = 신대만달러(TWD), US$ = 미국달러. 별도 표기 없는 재무 단위는 **NT$ 백만(M)**.
- **태그:** `[계산]` = 본 문서에서 출처 숫자로 산술 계산, `[학습데이터, 최신 아님]` = 웹/도구 미확인, `[2차출처]` = 회사 원문 미확인, 언론·집계사이트 기반.
- **네트워크 제약:** WebFetch로 `www.sec.gov`, `www.trendforce.com` 접근 불가(DNS 차단). 6-K/20-F 원문과 TSMC IR PDF는 직접 열람하지 못했고, 웹검색 결과 요약(원문 인용 포함)으로 확인함. 상세는 맨 끝 데이터 품질 노트 참조.

---

## 1. 기업 기본

| 항목 | 내용 | 출처 |
|---|---|---|
| 정식 명칭 | Taiwan Semiconductor Manufacturing Company Limited (台灣積體電路製造股份有限公司) | SEC EDGAR, CIK 0001046179 |
| 티커/코드 | NYSE: TSM (ADR) / TWSE: 2330 | SEC EDGAR; TSMC 실적 보도자료 |
| ADR 비율 | 1 ADR = 보통주 5주 | 과장 지시사항; TSMC 보도자료의 "per ADR unit" EPS 표기 (예: 3Q26 EPS NT$29.43 → US$4.60/ADR) |
| 상장시장 | 대만증권거래소(TWSE), 뉴욕증권거래소(NYSE, ADR) | 동상 |
| 업종 | 반도체 파운드리(위탁 생산) | SEC EDGAR |
| 결산월 / 회계기준 / 보고통화 | 12월 / IFRS / NT$ | SEC 20-F |
| 최신 연차보고서 | 20-F (FY2025), 접수일 **2026-04-16**, Accession 0001628280-26-025362 | SEC EDGAR submissions API (data.sec.gov), 2026-11-18 조회 |
| 발행주식수 (보통주) | 25,932.37M주 (2026-09-30) | Yahoo Finance(yfinance) quarterly balance sheet, 2026-11-18 조회 |

---

## 2. 재무 — 연간 (FY2020~FY2025)

### 2-1. 손익·현금흐름·재무상태 (단위 NT$ M, 별도 표기 제외)

FY2020~FY2024 출처: SEC EDGAR XBRL companyfacts (`python3 tools/sec_edgar.py TSM`, 20-F 기준, 최신 XBRL 연차 접수일 2025-04-17).
FY2025 출처: 아래 각주 참조 (SEC XBRL에 FY2025 미반영).

| 항목 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| 매출 | 1,339,255 | 1,587,415 | 2,263,891 | 2,161,736 | 2,894,308 | 3,809,054 ^a |
| 매출 (US$ B) | 데이터 없음 (시도: SEC XBRL은 NT$만) | 데이터 없음 | 데이터 없음 | 데이터 없음 | 데이터 없음 | 122.42 ^b |
| 매출총이익률 | 데이터 없음 (시도: sec_edgar 미출력) | — | — | — | 56.1% ^b | 59.9% ^b |
| 영업이익 | 566,784 | 649,981 | 1,121,279 | 921,466 | 1,322,053 | 1,936,096 ^c |
| 영업이익률 | 42.3% [계산] | 40.9% [계산] | 49.5% [계산] | 42.6% [계산] | 45.7% [계산] | 50.8% ^b |
| 순이익(지배주주) | 510,744 | 592,359 | 992,923 | 851,740 | 1,158,380 | **1,717,9xx (회사) / 1,697,604 (Yahoo) — 불일치** ^d |
| 희석 EPS (NT$) | 19.70 | 22.84 | 38.29 | 32.85 | 44.67 | **66.25 (회사) / 65.47 (Yahoo) — 불일치** ^e |
| 영업현금흐름 | 822,666 | 1,112,161 | 1,610,599 | 1,241,967 | 1,826,177 | 2,274,976 ^c |
| CAPEX (유형자산 취득) | 507,239 | 839,196 | 1,082,672 | 949,817 | 956,006 | 1,282,597 ^c |
| CAPEX (US$ B) | — | — | — | — | — | 40.90 ^b |
| FCF (OCF−CAPEX) [계산] | 315,427 | 272,965 | 527,927 | 292,150 | 870,171 | 992,378 ^c |
| SBC | 7 | 8 | 302 | 483 | 1,243 | 1,246 ^c |
| 자사주 매입 | 없음 (SEC XBRL 태그 미보고) | 없음 | 없음(SEC) / 872 (Yahoo) ^f | 없음 | 없음(SEC) / 3,089 (Yahoo) ^f | 0 (Yahoo) |
| 현금배당 지급 | 데이터 없음 (시도: sec_edgar 미출력) | 데이터 없음 | 285,234 (Yahoo) | 291,722 (Yahoo) | 363,055 (Yahoo) | 466,779 (Yahoo) |
| 총자산 | 2,760,600 | 3,725,302 | 4,964,459 | 5,532,197 | 6,691,765 | 7,932,842 ^c |
| 자기자본(지배주주) | 1,834,811 | 2,149,260 | 2,903,020 | 3,429,522 | 4,244,266 | 5,355,039 ^c |
| 현금및현금성자산 | 660,171 | 1,064,990 | 1,342,814 | 1,465,428 | 2,127,627 | 2,767,856 ^c |
| 비유동 사채 (SEC 태그) | 254,105 | 610,071 | 834,336 | 913,900 | 926,604 | 데이터 없음 |
| 총차입금 (Yahoo "Total Debt") | 데이터 없음 | 데이터 없음 | 888,174 | 956,258 | 1,047,042 | 1,064,583 |
| 순차입금 A = 비유동사채 − 현금 [계산, SEC] | −406,066 | −454,919 | −508,478 | −551,528 | −1,201,023 | — |
| 순차입금 B = 총차입금 − 현금 [계산, Yahoo] | — | — | −454,640 | −509,170 | −1,080,585 | −1,703,273 |
| 희석 가중평균주식수 (M주) | 25,930.3 | 25,930.3 | 25,929.4 | 25,929.3 | 25,929.7 | 데이터 없음 (시도: SEC XBRL FY2025 없음) |
| 기말 보통주식수 (M주, Yahoo) | — | — | 25,930.4 | 25,932.1 | 25,932.7 | 25,932.5 |

각주:
- ^a FY2025 매출 NT$3,809.05B(+31.6% YoY): TSMC 4Q25 실적 보도자료(2026-01-15), https://pr.tsmc.com/english/news/3281 ; SEC 6-K https://www.sec.gov/Archives/edgar/data/1046179/000104617926000008/a4q25e_withguidancexfinal.htm (웹검색 요약으로 확인). Yahoo 값 3,809,054와 일치.
- ^b FY2025 US$ 매출 122.42B(+35.9%), 매출총이익률 59.9%(FY2024 56.1%), 영업이익률 50.8%(FY2024 45.7%), CAPEX US$40.90B(4Q25 US$11.51B): 4Q25 실적 발표 관련 보도 [2차출처] — https://www.morningstar.com/news/dow-jones/20260115161/tsmc-ends-2025-with-a-bang-as-ai-keeps-boosting-profits , https://manufacturingdive.com/news/tsmc-q4-full-year-2025-earnings-ai-taiwan/809775 , https://telecomlead.com/semiconductor/tsmc-delivers-record-2025-revenue-and-profit-as-ai-chip-demand-fuels-growth-us-expansion-accelerates-124150
- ^c Yahoo Finance (yfinance `2330.TW` income_stmt / cashflow / balance_sheet), 2026-11-18 조회. 회사 원문 대조 안 됨. Yahoo CAPEX는 SEC 태그와 정의 차이 가능(FY2024: Yahoo 964,982 vs SEC 956,006, 차이 8,976 / FY2022: Yahoo 1,089,626 vs SEC 1,082,672).
- ^d 회사 기준 FY2025 순이익: 분기 합 361,56x(1Q25) + 398,27x(2Q25) + 452,301(3Q25) + 505,744(4Q25) ≈ 1,717,9xx [계산]. 1Q25·2Q25는 `[학습데이터, 최신 아님]`, 3Q25·4Q25는 회사 보도자료(웹검색 확인). 교차검증: EPS 66.25 × 약 25,930M주 ≈ 1,717.9B [계산]. Yahoo 1,697,604는 4Q25를 485,465로 기록(회사 505,744와 차이 20,279).
- ^e FY2025 EPS NT$66.25(+46.4%): 4Q25 실적 보도 [2차출처], yfinance earnings_estimate의 yearAgoEps 66.25와 일치. Yahoo income_stmt Diluted EPS 65.47은 불일치. 참고로 Yahoo 연간 EPS는 FY2024 45.25(SEC 44.67), FY2023 32.34(SEC 32.85), FY2022 39.20(SEC 38.29)으로 SEC와 모두 다름 → SEC 값 우선.
- ^f Yahoo "Repurchase Of Capital Stock" FY2022 −871.6M, FY2024 −3,089.2M. SEC XBRL에는 자사주매입 태그 없음. 직원 양도제한조건부주식(RSA)용 자기주식 취득일 가능성 있으나 원문 미확인 → 불일치로 기록.

### 2-2. 영업이익률·FCF 5년 요약 [계산]
- 매출 CAGR FY2020→FY2025 (NT$): (3,809,054/1,339,255)^(1/5) − 1 = **23.3%** [계산]
- FCF 합계 FY2021~FY2025 (NT$): 2,955,591M [계산, FY2021~24 SEC + FY2025 Yahoo]

---

## 3. 재무 — 최근 분기 (3Q25 ~ 3Q26)

단위 NT$ M (별도 표기 제외). 손익은 TSMC 분기 실적 보도자료(웹검색으로 원문 수치 확인), 현금흐름·재무상태는 Yahoo Finance(yfinance `2330.TW` quarterly), 2026-11-18 조회.

| 항목 | 3Q25 (비교용) | 4Q25 | 1Q26 | 2Q26 | 3Q26 |
|---|---|---|---|---|---|
| 실적 발표일 | 2025-10-16 | 2026-01-15 | 2026-04-16 | 2026-07-16 | 2026-10-15 |
| 매출 | 989,918 | 1,046,090 | 1,134,103 | 1,270,381 | 1,494,243 |
| 매출 (US$ B) | 데이터 없음 (시도: 웹검색) | 33.73 | 35.90 | 40.20 | 46.72 |
| 매출 YoY (NT$) | — | 데이터 없음 | +35.1% | 데이터 없음 | +50.9% |
| 매출 YoY (US$) | — | +25.5% | +40.6% | +33.7% | +41.2% |
| 매출총이익 | 588,543 | 651,987 | 751,295 | 860,311 | 992,379 |
| 매출총이익률 | 59.5% | 62.3% | 66.2% | 67.7% | 66.4% |
| 영업이익 | 500,685 | 564,881 | 658,949 | 766,603 (회사) / 766,568 (Yahoo) | 876,432 |
| 영업이익률 | 50.6% | 54.0% | 58.1% | 60.3% | 58.7% |
| 순이익(지배주주) | 452,301 | **505,744 (회사) / 485,465 (Yahoo)** | 572,480 | 706,562 | 763,064 |
| 순이익률 | 45.7% | 48.3% | 50.5% | 55.6% | 51.1% |
| 희석 EPS (NT$) | 17.44 | 19.50 | 22.08 | 27.25 | 29.43 |
| ADR당 EPS (US$) | 데이터 없음 | 3.14 | 3.49 | 4.31 | 4.60 |
| 영업현금흐름 (Yahoo) | 426,829 | 725,509 | 698,976 | 783,365 | 919,776 |
| CAPEX (Yahoo, NT$) | 288,443 | 361,468 | 351,706 | 508,395 | 448,472 |
| CAPEX (US$ B) | 데이터 없음 | 11.51 ^b | 데이터 없음 | 데이터 없음 | 13.84 [2차출처] |
| FCF [계산] | 138,386 | 364,041 | 347,270 | 274,970 | 471,303 |
| SBC (Yahoo) | 273.4 | 173.0 | 114.0 | 123.0 | 103.3 |
| 자사주 매입 (Yahoo) | 0 | 0 | 데이터 없음(NaN) | 데이터 없음(NaN) | 데이터 없음(NaN) |
| 현금배당 지급 (Yahoo) | 116,697 | 129,663 | 129,663 | 155,595 | 155,595 |
| 총자산 | 7,354,107 | 7,932,842 | 8,660,950 | 9,375,655 | 10,052,890 |
| 자기자본(지배주주) | 4,998,307 | 5,355,039 | 5,890,960 | 6,432,518 | 6,997,901 |
| 현금및현금성자산 | 2,470,759 | 2,767,856 | 3,035,637 | 3,134,218 | 3,621,894 |
| 현금+단기투자 | 2,804,928 | 3,128,068 | 3,452,597 | 3,597,437 | 4,094,653 |
| 총차입금 (Yahoo) | 1,025,433 | 1,064,583 | 1,090,769 | 1,064,950 | 1,065,988 |
| 순차입금 (총차입금−현금) [계산] | −1,445,326 | −1,703,273 | −1,944,868 | −2,069,268 | −2,555,906 |
| 기말 보통주식수 (M주) | 25,932.6 | 25,932.5 | 25,932.4 | 25,932.4 | 25,932.4 |

분기 손익 출처:
- 3Q25: https://pr.tsmc.com/english/news/3264 ; SEC 6-K https://www.sec.gov/Archives/edgar/data/1046179/000104617925000116/a3q25e_withguidancexfinal.htm
- 4Q25: https://pr.tsmc.com/english/news/3281 ; https://pr.tsmc.com/system/files/newspdf/attachment/9b721d84eaa4310b918005eb0f845d5a1847736d/4Q25%20%28E%29_with%20guidance_final_wmn.pdf
- 1Q26: https://pr.tsmc.com/english/news/3297 ; SEC 6-K https://www.sec.gov/Archives/edgar/data/1046179/000104617926000199/a1q26e_withguidancexfinal.htm
- 2Q26: https://pr.tsmc.com/english/news/3326 ; SEC 6-K https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000451/a2q26e_withguidancexfinal.htm
- 3Q26: https://pr.tsmc.com/english/news/3346 ; SEC 6-K https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm ; 3Q26 Management Report https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/f83780000ddc0c3b48e57a87eab6814c4ab35058/3Q26%20ManagementReport.pdf
- 4Q25·1Q26 매출총이익·영업이익 일부 금액은 Yahoo 값(이익률은 회사 발표치와 일치 확인: 4Q25 564,881/1,046,090 = 54.0%, 1Q26 658,949/1,134,103 = 58.1% [계산]).
- 1Q26 순이익 NT$572.48B, 2Q26 NT$706.56B, 3Q26 NT$763.06B: 회사 보도자료 수치 = Yahoo 값과 일치.
- 최근 4개 분기(4Q25~3Q26) 합계 [계산]: 매출 4,944,817 / 순이익 2,547,850 (회사 기준) / 희석 EPS NT$98.26 / FCF 1,457,584. (Yahoo trailingEps 97.47은 4Q25 Yahoo 순이익 기준으로 추정되는 차이)
- 2026년 1~9월 누적 매출 3,898,727 [계산] / 순이익 2,042,106 [계산] / 희석 EPS NT$78.76 [계산].

### 3-1. 2026년 4분기 가이던스 (2026-10-15 발표)

| 항목 | 가이던스 | 출처 |
|---|---|---|
| 매출 | US$52.3B ~ US$54.3B (중간값 기준 QoQ +14%, YoY +58% — 회사 측 설명 인용 보도) | TSMC 3Q26 보도자료/6-K (웹검색 요약), https://pr.tsmc.com/english/news/3346 ; https://www.allblogthings.com/2026/10/tsmc-forecasts-q4-revenue-up-to-54-3-billion-keeps-capital-spending-unchanged.html |
| 환율 가정 | US$1 = NT$31.8 | 동상 |
| 매출 NT$ 환산 | NT$1,663.1B ~ 1,726.7B [계산: US$ × 31.8]; 보도상 "약 NT$1.66~1.73조" (Focus Taiwan) | [계산]; https://focustaiwan.tw/business/202611110009 |
| 매출총이익률 | 65% ~ 67% | 동상 |
| 영업이익률 | 56.5% ~ 58.5% (회사) / 56.0~58.0%로 기재한 2차출처 존재(Averin) — 불일치, 회사값 우선 | https://averin.com/en/journal/ruslan-averin-tsmc-tsm-q3-2026-earnings-results-ai-demand-guidance |
| FY2026 매출 성장률 (US$) | 약 44% (3Q26 컨퍼런스콜) | https://focustaiwan.tw/business/202610150018 ; https://www.stocktitan.net/articles/tsmc-q3-2026-earnings-ai-chip-boom |
| FY2026 매출 암시값 [계산] | US$175.1B ~ 177.1B (1~3Q US$122.82B + 4Q 가이던스) → FY2025 대비 +43.0% ~ +44.7%; NT$ 5,561.8B ~ 5,625.4B | [계산] |
| 해외 팹 GM 희석 | FY2026 약 2% (기존 2~3% 가이던스), 향후 수년 3~4% | 3Q26 컨퍼런스콜 보도 [2차출처], https://www.webull.com/news/15751044230423552 |

참고 — 직전 분기 가이던스 대비 실적: 2Q26 가이던스(매출 US$39.0~40.2B, GM 65.5~67.5%, OPM 56.5~58.5%, 환율 31.7) → 실적 US$40.20B / 67.7% / 60.3%. 3Q26 가이던스(US$44.6~45.8B, GM 65~67%, OPM 56~58%, 환율 32.0) → 실적 US$46.72B / 66.4% / 58.7%. (출처: 1Q26·2Q26 보도자료, 위 링크)

---

## 4. 월별 매출 (최근 6개월, NT$ B)

| 월 | 매출 | MoM | YoY | 공시일 | 출처 |
|---|---|---|---|---|---|
| 2026-05 | 416.975 | +1.5% | +30.1% | 2026-06-10 | Focus Taiwan https://focustaiwan.tw/business/202606100008 ; SEC 6-K tsm-revenue20260610.htm |
| 2026-06 | 442.68 | +6.2% | +67.9% | 2026-07-13 | SEC 6-K https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000447/tsm-revenue20260713.htm |
| 2026-07 | 467.58 | +5.6% | +44.7% | 2026-08-10 | SEC 6-K https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000471/tsm-revenue20260810.htm |
| 2026-08 | 514.81 [2차출처] | +10.1% [계산] | 데이터 없음 (시도: 웹검색 2회) | 2026-09-10 | 9월 매출 보도 내 인용 https://letsdatascience.com/news/tsmc-september-revenue-rose-546-from-a-year-earlier-5240f1c8 ; 교차검증: 3Q26 매출 1,494.24 − 7월 467.58 − 9월 511.86 = 514.80 [계산] |
| 2026-09 | 511.86 | −0.6% | +54.6% | 2026-10-08 | SEC 6-K https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000680/tsm-revenue20261008.htm |
| 2026-10 | 586.89 | +14.7% | +59.7% | 2026-11-10 | SEC 6-K https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000796/tsm-revenue20261110.htm ; https://pr.tsmc.com/english/news/3349 ; CNBC https://www.cnbc.com/2026/11/10/tsmcs-october-sales-.html |

- 2026년 1~10월 누적: NT$4,485.62B (+43.3% YoY) (출처: 10월 매출 6-K, 위 링크). 교차검증: 1~3Q 분기 매출 합 3,898.73 + 10월 586.89 = 4,485.62 [계산] — 일치.
- 2Q26 교차검증: 4월 410.725 + 5월 416.975 + 6월 442.68 = 1,270.38 = 2Q26 분기 매출 [계산] — 일치.
- **불일치:** Yahoo Finance 기사(https://finance.yahoo.com/technology/ai/articles/tsmc-reports-59-7-rise-111242338.html)는 10월 매출을 NT$367.47B로 표기 → 회사 6-K(586.89)·CNBC와 불일치. 회사값 채택.

---

## 5. 매출 구성 (3Q26)

출처: TSMC 3Q26 Management Report (https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-10/f83780000ddc0c3b48e57a87eab6814c4ab35058/3Q26%20ManagementReport.pdf), 웹검색 요약으로 수치 확인. 2차 확인: https://sector-signals.net/en/themes/advanced-packaging/articles/tsmc-3q26-results-hpc-68-percent-2nm-2026

### 5-1. 공정 노드별 (웨이퍼 매출 비중)
| 노드 | 3Q26 | 2Q26 |
|---|---|---|
| 2nm | 8% | 3% |
| 3nm | 33% | 30% |
| 5nm | 28% | 33% |
| 7nm | 10% | 11% |
| 7nm 이하 합계 | 79% | 77% [계산] |
| 16nm 이상 | 21% [계산] (세부 데이터 없음, 시도: 웹검색) | 23% [계산] |

### 5-2. 플랫폼별 (순매출 비중)
| 플랫폼 | 3Q26 | 2Q26 |
|---|---|---|
| HPC | 68% (QoQ 매출 +22% 보도) | 66% |
| 스마트폰 | 21% | 22% |
| IoT | 4% | 데이터 없음 |
| 자동차 | 4% | 데이터 없음 |
| DCE(디지털 가전) | 1% | 데이터 없음 |
| 기타 | 2% | 데이터 없음 |

### 5-3. 지역별 (고객 본사 소재지 기준, 순매출 비중)
| 지역 | 3Q26 | 비고 / 출처 |
|---|---|---|
| 북미 | 79% (sec-api 분석: 미국 78.9%) | https://sec-api.io/insights/tsmc-tsm-q3-2026-earnings-nt-1-49tn-revenue-58-7-operating-margin-and-a-us-52-3bn-to-us-54-3bn-q4-outlook-sec-filing-analysis [2차출처] |
| 중국 | 5% (sec-api 분석: 5.5%) — 3Q25 8% | 동상, https://www.crnasia.com/news/2026/components-and-peripherals/tsmc-third-quarter-revenue-tops-guidance-as-ceo-says-ai-dema |
| 일본 | 3% (2Q26 4%) | https://xenospectrum.com/en/tsmc-q3-2026-gross-margin-capex/ [2차출처] |
| 아시아태평양 / EMEA | 데이터 없음 (시도: 웹검색 2회, Management Report PDF 직접 열람 실패) | 잔여 13% [계산] |

---

## 6. CAPEX 가이던스 및 해외 팹

### 6-1. CAPEX
| 항목 | 값 | 출처 |
|---|---|---|
| FY2025 실적 | US$40.90B | 4Q25 실적 보도 [2차출처], ^b |
| FY2026 가이던스 (2026-01-15 최초) | US$52B ~ 56B | https://www.tomshardware.com/tech-industry/semiconductors/tsmc-very-nervous-about-ai-bubble-concerns-despite-another-record-setting-quarter-but-assured-of-demand-ceo-says-careless-investment-would-be-a-disaster-for-tsmc-for-sure-company-will-invest-usd52-usd56-billion-in-capex |
| FY2026 가이던스 (2026-07-16 상향) | US$60B ~ 64B | https://www.trendforce.com/news/2026/07/16/news-tsmc-lifts-2026-capex-15-to-60-64b-hikes-sales-outlook-to-over-40-despite-q3-margin-dip/ (검색 결과 제목·요약) |
| FY2026 가이던스 (2026-10-15 유지) | US$60B ~ 64B 유지 | https://focustaiwan.tw/business/202610150018 ; https://cryptobriefing.com/tsmc-capex-64-billion-ai-demand/ |
| 3Q26 CAPEX | 약 US$13.84B | https://fourweekmba.com/ai-tsmc-q3-revenue-rises-to-46-7b-with-a-66-4-gross-margin/ [2차출처] |
| 2026년 1~9월 누적 CAPEX | US$40.64B [2차출처] / NT$1,308,573M (Yahoo 분기 합 [계산]) | 동상; yfinance |
| 4Q26 암시 CAPEX [계산] | US$19.36B ~ 23.36B (가이던스 − 누적) | [계산] |
| 2026~2028 CAPEX | "직전 3년보다 유의미하게 높을 것" 언급, 2027 수치 가이던스 없음 | 3Q26 컨퍼런스콜 보도, https://www.webull.com/news/15757014150898688 |
| 이사회 자본예산 승인 (2026-11-10) | 약 US$40,926.70M (장기 생산능력 계획용) | TSMC 이사회 결의, https://pr.tsmc.com/english/news/3352 |

### 6-2. 해외 팹 진행 상황
| 팹 | 사실 | 출처 |
|---|---|---|
| 애리조나 Fab 1 (N4) | 2024년 4분기 양산 시작 | `[학습데이터, 최신 아님]` |
| 애리조나 Fab 2 (3nm) | 건설 완료, 장비 반입·설치 진행 중. 양산 3Q27 예정(기존 일정보다 소폭 앞당김) — 3Q26 컨퍼런스콜(2026-10-15) C.C. Wei 발언 | https://www.webull.com/news/15751044230423552 ; https://www.techpowerup.com/345226/tsmc-expecting-to-start-3-nm-production-in-arizona-in-2h-2027 |
| 애리조나 총 투자 | US$165B 계획(2025-03 발표) — 이후 추가 확대 보도(EE Times "adds $100B") 있으나 날짜·금액 원문 미확인 | `[학습데이터, 최신 아님]`; https://www.eetimes.com/tsmc-boosts-2026-expansion-budget-adds-100b-to-u-s-investment/ (제목만 확인) |
| 일본 구마모토 JASM Fab 1 | 2024년 말 양산 시작 | `[학습데이터, 최신 아님]` |
| 일본 구마모토 JASM Fab 2 | 건설 착수 언급(웨이 회장). Nikkei: 당초 6/7nm 계획에서 4nm 전환 검토 보도 — 회사 확인 없음 | 웹검색 요약 [2차출처] |
| 독일 드레스덴 ESMC | 2026-01 사무동 상량식. 2H26 장비 반입 예정 보도. 2026-09 기준 약 2,000명 현장 작업(Focus Taiwan). 2027년 생산 개시 목표(보도별 "2027" / "2027년 말" 차이) | https://evertiq.com/design/2026-01-28-esmc-holds-topping-out-ceremony-at-dresden-fab-site ; https://focustaiwan.tw/business/202609150007 ; https://www.trendforce.com/news/2025/11/20/news-tsmc-dresden-fab-reportedly-wraps-structural-build-eyes-equipment-move-in-in-2h26/ |
| 정부 보조금 | 미국·일본·독일·중국으로부터 NT$167.6B 보조금 수령(기록치) 보도, 대상 기간 원문 미확인 | https://focustaiwan.tw/business/202611140005 |

---

## 7. 주가·시가총액·배당·환율

### 7-1. 주가 (`python3 tools/prices.py TSM 2330.TW`, 1회 성공, 레이트리밋 없음)

| 티커 | 종가(수정) | 기준일 | 52주 범위(종가) | 1년 | 3년 | 5년 |
|---|---|---|---|---|---|---|
| TSM (US$) | 359.69 | 2026-11-17 | 272.18 ~ 485.80 | +28.9% | +275.9% | +232.8% |
| 2330.TW (NT$) | 2,175.00 | 2026-11-18 | 1,358.34 ~ 2,585.00 | +56.7% | +293.1% | +301.0% |

출처: Yahoo Finance via yfinance (수정주가). 52주 범위 차이: yfinance `info`(장중 기준) TSM US$266.82 ~ 487.47, 2330.TW NT$1,375 ~ 2,590 — 종가/장중·수정주가 기준 차이.

5년 연말 종가(비수정, yfinance):
| 연말 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026-11-17/18 |
|---|---|---|---|---|---|---|
| TSM (US$) | 120.31 | 74.49 | 104.00 | 197.49 | 303.89 | 359.69 |
| 2330.TW (NT$) | 615.0 | 448.5 | 593.0 | 1,075.0 | 1,550.0 | 2,175.0 |

- TSM 2026-11-17 일간 −3.68% (−US$13.76) — https://www.heygotrade.com/en/news/tsmc-tsm-stock-news-november-18-2026/ [2차출처]

### 7-2. 시가총액
| 기준 | 값 | 출처 |
|---|---|---|
| 2330.TW | NT$56,402.9B (= 2,175 × 25,932.36M주) | yfinance info, 2026-11-18 |
| 2330.TW US$ 환산 | US$1,711.9B [계산, 환율 32.947] | [계산] |
| TSM (ADR 가격 기준, yfinance) | US$1,865.5B (ADR 환산주식 5,186.47M × 359.69) | yfinance info, 2026-11-17 |
| ADR 프리미엄 [계산] | TSM 359.69/5 × 32.947 = NT$2,370.2 vs 2330.TW 2,175 → **+9.0%** (주의: TSM 11-17 종가 vs 2330 11-18 종가, 기준일 상이) | [계산] |

### 7-3. 배당 (보통주 1주당 NT$, 분기)
| 대상 분기 | 주당 배당 | 배당락일 | 지급일 | 출처 |
|---|---|---|---|---|
| 2Q25 | NT$5.00 | 2025-12-11 | — | yfinance dividends |
| 3Q25 | NT$6.00 | 2026-03-17 | — | yfinance dividends |
| 4Q25 | NT$6.00 | 2026-06-11 | — | yfinance dividends |
| 1Q26 | NT$7.00 | 2026-09-16 (기준일 09-22) | 2026-10-08 | yfinance; 2026-05-12 이사회 결의 https://pr.tsmc.com/english/news/3311 |
| 2Q26 | NT$7.00 (결의 2026-08-11) | 2026-12-10 (기준일 12-16) | 2027-01-07 | https://pr.tsmc.com/system/files/newspdf/attachment/a348e07f3638a461f4f2f20ff3f7cd3ad611d75f/0811%20board%20meeting%20%28E%29_final_wmn.pdf |
| 3Q26 | **NT$9.00** (결의 2026-11-10) | 2027-03-11 (기준일 03-17) | 2027-04-08 | https://pr.tsmc.com/english/news/3352 ; https://focustaiwan.tw/business/202611110009 |

- 직전 12개월 배당락 합계: NT$24.00 (5+6+6+7) [계산] = yfinance dividendRate 24.0. 2330.TW 기준 배당수익률 1.10% [계산, 24/2,175].
- 발표 기준 연환산(최근 결의 NT$9 × 4): NT$36.00 [계산] → 1.66% [계산].
- ADR 배당(US$/ADR, yfinance): 2025-12-11 0.835 / 2026-03-17 0.956 / 2026-06-11 0.955 / 2026-09-16 1.107.
- 2Q26 배당부터 해외투자 규정상 외국인 주주 US$ 배당 수령 선택 가능 (2026-08-11 이사회 자료, 위 링크).

### 7-4. 환율
- USD/TWD = **32.947** (2026-11-18), 직전 5영업일 32.862 ~ 32.963, 52주 30.652 ~ 33.125 (출처: yfinance `TWD=X`, 2026-11-18 조회)
- 참고: 4Q26 가이던스 가정 환율 NT$31.8

---

## 8. 컨센서스

| 항목 | 값 | 애널리스트 수 | 출처 / 기준일 |
|---|---|---|---|
| FY2026E EPS (NT$) | 110.63 (범위 98.4 ~ 113.4) | 35 | Yahoo Finance (yfinance earnings_estimate, 2330.TW), 2026-11-18 조회 |
| FY2027E EPS (NT$) | 149.53 (126.5 ~ 167.13) | 36 | 동상 |
| 4Q26E EPS (NT$) | 33.14 (31.9 ~ 34.64) | 21 | 동상 |
| FY2026E 매출 (NT$) | 5,582.1B (5,157.0 ~ 5,728.5B) | 40 | 동상 |
| FY2027E 매출 (NT$) | 7,691.2B (6,879.0 ~ 8,534.4B) | 41 | 동상 |
| 4Q26E 매출 (NT$) | 1,707.8B (1,647.3 ~ 1,753.0B) | 26 | 동상 |
| FY2026E EPS (US$/ADR) | 17.50 (17.18 ~ 17.95) | 11 | yfinance (TSM) |
| FY2027E EPS (US$/ADR) | 23.39 (21.45 ~ 25.87) | 13 | yfinance (TSM) |
| 4Q26E EPS (US$/ADR) | 5.16 | 8 | yfinance (TSM) |
| 목표주가 평균 | TSM US$586.69 (20명) / 2330.TW NT$3,402.51 (35명) | — | yfinance info, 2026-11-18 |
| (대안) FY2026E/2027E 매출 | NT$5,466B / NT$7,429B | — | TIKR, 2026-10 (3Q26 발표 전후, 날짜 불명확) https://tikr.com/blog/tsmc-posts-a-sixth-straight-record-quarter-and-its-q4-guide-says-the-ai-boom-isnt-slowing-heres-the-fuller-picture |
| (대안) FY2026E/2027E ADR EPS | US$17.04 / US$22.30 | — | 동상 |
| (대안) FY2026E 매출 US$ | US$171.6B | — | Visible Alpha via S&P Global, 2026-07-21 (3Q26 발표 이전) https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/07/tsmc-postq-ai-drives-beat-outlook-raised-higher-capex-weighs-on-sentiment |
| 3Q26 실적 vs 컨센서스 | 순이익 NT$763.06B vs LSEG SmartEstimate NT$746.34B; ADR EPS US$4.60 vs 컨센 US$4.42 | — | https://www.tipranks.com/stocks/tsm/earnings/q3-2026-report 등 검색 요약 [2차출처] |

- 소스 간 차이: FY2026E 매출 Yahoo NT$5,582.1B vs TIKR NT$5,466B (차이 NT$116.1B, 2.1%); FY2027E EPS(ADR) Yahoo US$23.39 vs TIKR US$22.30. 회사 가이던스 암시 FY2026 매출 NT$5,561.8~5,625.4B [계산, 3-1절].

---

## 9. 지분 구조 (미장 추가 항목 + 참고)

| 항목 | 값 | 출처 / 기준일 |
|---|---|---|
| 외국인 지분율 (2330 보통주, ADR 포함 여부 출처 미기재) | 69.21% (약 179.5억주) | EBC 기사, 2026-09-15 기준 https://www.ebc.com/zh-cn/jinrong/312144.html [2차출처] |
| 외국인 지분율 1년 전 | 약 73.8% (2025-09경) | 동상 |
| ADR(예탁기관) 보유 비중 | 20.49% | TSMC 2025 연차보고서 주요주주 표 (웹검색 요약) https://investor.tsmc.com/static/annualReports/2025/english/pdf/2025_tsmc_ar_e_ch4.pdf |
| 최대 단일 주주 | 행정원 국가발전기금 6.38% | 동상 |
| 기타 주요 주주 | 싱가포르 정부 2.08%, 노르웨이 중앙은행 1.81% | 동상 |
| 기관 보유비율 (Yahoo) | 2330.TW 43.34% / TSM ADR 15.38% (기관 4,752곳), 내부자 0.022% | yfinance, 2026-11-18 |
| 자사주 | 소각/매입 프로그램 데이터 없음 (시도: SEC XBRL, yfinance — 2025 이후 매입 0 또는 NaN) | — |
| SBC | FY2025 NT$1,246M (매출 대비 0.03% [계산]); 3Q26 NT$103M | yfinance; FY2020~24 SEC XBRL (2-1절) |
| 자사주 매입액 | FY2020~FY2024 SEC XBRL 태그 없음 → **없음**(SEC). Yahoo는 FY2022 NT$872M, FY2024 NT$3,089M 기록 → 불일치 | 2-1절 ^f |

---

## 10. 주요 리스크 공시 (20-F Risk Factors — 지정학·관세)

- **20-F (FY2025) 원문 Risk Factors: 데이터 없음** (시도: SEC EDGAR 원문 URL — WebFetch DNS 차단으로 열람 실패; 웹검색 — 원문 인용 없음). 접수일 2026-04-16 확인(EDGAR submissions API).
- 관련 사실(2차출처, 20-F 원문 아님):
  - 2025-05: TSMC가 미 상무부에 반도체 관세(Section 232)가 수요 감소 및 애리조나 투자 계획에 영향 줄 수 있다는 의견서 제출 — https://www.notebookcheck.net/TSMC-warns-US-chip-tariffs-could-derail-165-billion-Arizona-investment.1025325.0.html
  - 2025-08: 미국 대통령이 반도체 수입 100% 관세 방침 발표, 미국 내 생산·투자 약정 기업 면제 방침 — KGI 리포트 https://www.kgi.com.hk/zh-cn/-/media/files/kgishk/research-reports/tw-reports/semiconductor-sector_07082025e.pdf . 2026년 최종 규정 여부: 데이터 없음 (시도: 웹검색).
  - 2025-09: 미 상무부, TSMC 난징 팹의 VEU(검증된 최종사용자) 지위 철회(2025-12-31 발효) — https://www.techrepublic.com/article/news-tsmc-export-hurdles-us-pulls-china-waiver/ ; 이후 1년짜리 장비 반입 라이선스 취득 보도 https://rallies.ai/news/tsmc-gets-one-year-us-export-license-shares-up-on-45-rally-and-ai-upgrades (날짜 원문 미확인)
  - 20-F 미래예측 진술 고지에 "지역 정치 안정성 및 지정학적 긴장"이 위험요인으로 기재됐다는 3자 요약 — https://macmyths.com/what-are-the-risks-of-investing-in-tsmc/ (원문 미확인)

---

## 11. 최근 90일 공시·뉴스 헤드라인 (2026-08-20 ~ 2026-11-18)

| 날짜 | 헤드라인 (1줄 요약) | 출처 |
|---|---|---|
| 2026-08-25 | 6-K 월말 공시(내부자 지분변동 등) 제출 | SEC EDGAR submissions (tsm-monthend6kx20260825.htm) |
| 2026-09-01 | 6-K 배당 조정 관련 공시 제출 (내용 미확인) | SEC EDGAR submissions (tsm-dividendadjustmentx202.htm) |
| 2026-09-08 | TSMC·ASML, High-NA EUV용 대형 포토마스크 전환 공동 추진 발표 | TSMC 뉴스룸 (웹검색 요약) https://pr.tsmc.com/english/latest-news |
| 2026-09-10 | 8월 매출 NT$514.81B 공시 | SEC 6-K tsm-revenue20260910.htm; 4절 |
| 2026-09-15 | 외국인 지분율 69.21% (1년 전 약 73.8%) 보도 | https://www.ebc.com/zh-cn/jinrong/312144.html |
| 2026-10-08 | 9월 매출 NT$511.86B (−0.6% MoM, +54.6% YoY) | SEC 6-K https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000680/tsm-revenue20261008.htm |
| 2026-10-15 | 3Q26 실적: 매출 NT$1,494.24B, 순이익 NT$763.06B(+68.7% YoY), EPS NT$29.43; 4Q26 매출 가이던스 US$52.3~54.3B; FY2026 CAPEX US$60~64B 유지; FY2026 성장률 약 44%(US$) | https://pr.tsmc.com/english/news/3346 ; https://focustaiwan.tw/business/202610150018 |
| 2026-10-15 | 실적 발표 당일 주가 하락 보도 (ADR −4.0% / 대만 −2.8%, 출처별 상이) | https://www.alpha-sense.com/earnings/tsm/ ; https://investinglive.com/stocks/icymi-tsmc-profit-jumps-nearly-70-on-ai-demand-but-margin-outlook-weighs-on-shares/ |
| 2026-11-06 | The Information 보도 인용: Nvidia 요청으로 3D DRAM 등 AI 메모리 칩 생산 검토 (회사 미확인) | Bloomberg https://www.bloomberg.com/news/articles/2026-11-06/tsmc-mulls-making-advanced-ai-memory-chips-information-says |
| 2026-11-10 | 10월 매출 NT$586.89B (+14.7% MoM, +59.7% YoY), 1~10월 누적 NT$4,485.62B (+43.3%) | https://pr.tsmc.com/english/news/3349 ; SEC 6-K tsm-revenue20261110.htm |
| 2026-11-10 | 이사회: 3Q26 분기배당 NT$9.0 결의, 자본예산 약 US$40,926.70M 승인, Anthropic PBC(IPO 가격, 한도 US$500M)·OpenAI Group PBC(한도 US$500M) 투자 승인, 반도체 투자회사(자본금 한도 US$500M) 설립 승인 | https://pr.tsmc.com/english/news/3352 ; https://pr.tsmc.com/system/files/newspdf/attachment/e05987700f76438755c64d950b3b0b99369aeed2/1110%20board%20meeting%20%28E%29_final_wmn.pdf |
| 2026-11-12 | 6-K "Statement regarding ..." 제출 (내용 미확인) | SEC EDGAR submissions (a20261112statementregardin.htm) |
| 2026-11-13 | 6-K 재무제표(3Q26 연결재무제표 추정) 제출 | SEC EDGAR submissions (tsm-fsx20261113x6k.htm) |
| 2026-11-14 | 미국·일본·독일·중국 정부 보조금 NT$167.6B(기록치) 수령 보도 | https://focustaiwan.tw/business/202611140005 |
| 2026-11-17 | 2026 공급망 우수 협력사 35곳 시상 (ASML, KLA 등) | https://kucoin.com/news/flash/tsmc-announces-2026-supply-chain-excellence-award-winners |
| 2026-11-17 | TSM ADR −3.68% (US$359.69). 집계사이트는 미 상무부 파운드리 관련 신규 규정을 원인으로 기재 — 규정 실체 미확인 (웹검색 2회) | https://www.heygotrade.com/en/news/tsmc-tsm-stock-news-november-18-2026/ [2차출처, 미검증] |

참고(90일 범위 직전): 2026-08-11 Sony Semiconductor Solutions와 차세대 이미지센서 JV 설립 합의(SEC 6-K sonysemiconductorsolutions.htm); 2026-08-11 2Q26 배당 NT$7.0 결의.

---

## 데이터 품질 노트

### 도구 실행 결과
| 도구 | 결과 |
|---|---|
| `python3 tools/sec_edgar.py TSM` | 성공. FY2020~FY2024만 반환. 최신 연차 접수일을 2025-04-17로 표시하나, EDGAR submissions API상 FY2025 20-F는 **2026-04-16 접수**(0001628280-26-025362) → companyfacts XBRL에 FY2025 미반영. |
| `python3 tools/prices.py TSM 2330.TW` | 1회 성공 (레이트리밋 없음). |
| yfinance 직접 호출 (info, 재무제표, 추정치, 배당, `TWD=X`) | 성공. 회사 원문과 대조되지 않은 값은 각주로 표기. |
| WebFetch `www.sec.gov` (3Q26 6-K 원문) | **실패 — DNS 차단(세션 허용 도메인 외)**. |
| WebFetch `www.trendforce.com` | **실패 — DNS 차단**. 이후 추가 사이트 WebFetch 시도 중단, 웹검색 요약으로 대체. |

### 결측
1. FY2025 희석 가중평균주식수, FY2025 비유동사채 (SEC XBRL 미반영).
2. FY2020~FY2023 매출총이익률, FY2020~FY2021 배당 지급액.
3. 3Q26 지역별 매출 중 아시아태평양·EMEA 비중; 16nm 이상 노드 세부 비중; 2Q26 IoT/자동차/DCE 비중.
4. 1Q26·2Q26 분기 CAPEX(US$), 3Q25 US$ 매출·ADR EPS.
5. 8월 매출 YoY, 8월 매출 회사 원문(2차출처만).
6. **20-F(FY2025) Risk Factors 원문** (지정학·관세 문구) — 미확보.
7. 반도체 Section 232 관세 최종 규정 여부(2026년), 2026-11-17 "미 상무부 파운드리 규정" 실체.
8. 2026-09-01, 2026-11-12 6-K 내용.
9. 컨센서스 LSEG/FactSet 원자료 (Yahoo·TIKR·Visible Alpha 2차 집계만 확보).

### 소스 간 불일치
| 항목 | 소스 A | 소스 B | 차이 | 채택 |
|---|---|---|---|---|
| 4Q25 순이익 | 회사 NT$505,744M | Yahoo NT$485,465M | 20,279M | 회사 |
| FY2025 순이익 | 회사 기준 ≈NT$1,717.9B [계산] | Yahoo NT$1,697.6B | ≈20.3B | 회사 |
| FY2025 희석 EPS | 회사 NT$66.25 | Yahoo NT$65.47 | 0.78 | 회사 |
| FY2022~24 희석 EPS | SEC 38.29 / 32.85 / 44.67 | Yahoo 39.20 / 32.34 / 45.25 | — | SEC |
| CAPEX FY2024 | SEC 956,006 | Yahoo 964,982 | 8,976 | SEC (정의 차이 가능) |
| 자사주 매입 FY2022·FY2024 | SEC 태그 없음 | Yahoo 872 / 3,089 | — | 병기 |
| 2Q26 영업이익 | 회사 766,603 | Yahoo 766,568 | 35 | 회사 |
| 10월 매출 | 회사 6-K NT$586.89B | Yahoo 기사 NT$367.47B | 219.42B | 회사 |
| 4Q26 OPM 가이던스 | 회사 56.5~58.5% | Averin 56.0~58.0% | 0.5%p | 회사 |
| 52주 범위 TSM | prices.py(수정 종가) 272.18~485.80 | yfinance info 266.82~487.47 | 기준 차이 | 병기 |
| 3Q26 중국 비중 | 5% | 5.5% (sec-api) | 반올림 | 병기 |
| FY2026E 매출 컨센 | Yahoo NT$5,582.1B | TIKR NT$5,466B | 2.1% | 병기 |
| 시가총액 | 2330 기준 US$1,711.9B [계산] | TSM ADR 기준 US$1,865.5B | ADR 프리미엄 ≈9.0% 및 기준일 차이 | 병기 |
| 드레스덴 생산 개시 | "2027" | "2027년 말" | — | 병기 |

### 미검증 정보 (본문 헤드라인에서 제외)
- 집계사이트(heygotrade)의 2026-11-12 "Nvidia CEO 사임" 관련 TSM 주가 −1.90% 기사: 단일 2차출처, 교차확인 없음 → 사실로 채택하지 않음.
- 2026-11-17 하락 원인으로 언급된 "미 상무부 파운드리 신규 규정": 웹검색 2회로 확인 불가.

### 학습데이터 의존 항목 `[학습데이터, 최신 아님]`
- 1Q25·2Q25 순이익(FY2025 순이익 합산용), 애리조나 Fab 1 및 구마모토 Fab 1 양산 시점, 애리조나 US$165B 투자 계획.
