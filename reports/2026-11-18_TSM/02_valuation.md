# 02_valuation — TSMC (2330.TW / NYSE: TSM)

- **작성:** 대리(밸류에이션 담당) · **작성일:** 2026-11-18
- **데이터 기준일:** 2330.TW 종가 NT$2,175.00 (2026-11-18), TSM ADR 종가 US$359.69 (2026-11-17), USD/TWD 32.947 (2026-11-18), 재무 3Q26(2026-09-30)까지, 피어 Yahoo Finance 2026-11-18 조회
- **입력:** `reports/2026-11-18_TSM/01_data.md` (사원). 01에 없는 숫자는 `tools/fred.py`, yfinance, 웹검색으로 확보하고 출처를 달았다.
- **통화:** 밸류에이션은 모두 **NT$** 기준이다. ADR 환산 = 주당가치 × 5 ÷ 32.947.
- **태그:** `[계산]` 본 문서 Python 계산 · `[추정]` 대리 가정 · `[학습데이터, 최신 아님]`
- **소스 불일치 처리:** 01_data의 불일치 항목은 **회사 발표치**를 썼다. FY2025 순이익 ≈NT$1,717.9B와 EPS 66.25(Yahoo 1,697.6B / 65.47 아님), 4Q25 순이익 505,744(Yahoo 485,465 아님), TTM 순이익 2,547,850과 EPS 98.26(Yahoo trailingEps 97.47 아님), FY2022~24 EPS는 SEC 값, CAPEX FY2024는 SEC 956,006을 썼다. 예외로 FY2025 현금흐름·재무상태는 회사 원문이 없어서 Yahoo 값을 그대로 썼다(01_data ^c).
- 이 문서에는 투자 의견이 없다. 숫자와 범위만 적었다.

---

## 0. 요약 표

| 항목 | 값 |
|---|---|
| 현재가 | NT$2,175 (2330) / US$359.69 (ADR = NT$2,370/주 상당, 프리미엄 +9.0%) |
| WACC (TWD) | **9.0%** [추정] (근거 3-1절) |
| 역DCF: 내포 10년 FCF CAGR (TTM FCF 기준, g=3%) | **12.9%** (2330 기준) / 14.0% (ADR 가격 기준) [계산] |
| 역DCF: 기본 마진·CAPEX 경로에서 내포된 10년 매출 CAGR | **11.0%** (2330) / 12.2% (ADR) [계산] |
| DCF 주당 가치 약세 / 기본 / 강세 | **NT$1,098 / 2,336 / 3,847** (ADR US$166.6 / 354.5 / 583.8) [계산] |
| 안전마진 (2330 NT$2,175 기준) | 약세 −98.0% / 기본 **+6.9%** / 강세 +43.5% [계산] |
| 안전마진 (ADR US$359.69 기준) | 약세 −115.8% / 기본 **−1.5%** / 강세 +38.4% [계산] |
| 기본 시나리오에서 터미널가치 비중 | **EV의 60.5%**, 주주가치의 57.5% [계산] |
| 가장 민감한 가정 | **할인율(WACC, 대만 지정학 프리미엄 포함)**. ±1%p에 주당가치 −14.3% / +20.1%. 다만 매출 성장 경로 전체를 ±25% 조정하면 −19.7% / +24.3%로 이보다 크다(5절 토네이도 참조) |

---

## 1. 수익성·질 지표 (FY2020~FY2025)

단위 NT$ M. 입력은 01_data 2-1절이다(FY2020~24 SEC XBRL, FY2025 회사/Yahoo). 세율과 EBITDA는 yfinance `2330.TW` 연간 손익(2026-11-18 조회)에서 가져왔다.

| 지표 | FY2020 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|---|
| 유효세율 | 13.0% [추정] | 13.0% [추정] | 13.2% | 13.1% | 17.7% | 17.0% |
| 투하자본 (자기자본+차입금−현금) | 1,428,745 | 1,694,341 | 2,448,380 | 2,920,352 | 3,163,681 | 3,651,766 |
| **ROIC** (NOPAT/평균 투하자본) | 34.5%* | 36.2% | 47.0% | 29.8% | 35.8% | **47.2%** |
| **ROE** (순이익/평균 자기자본) | 27.8%* | 29.7% | 39.3% | 26.9% | 30.2% | **35.8%** |
| **영업이익률** | 42.3% | 40.9% | 49.5% | 42.6% | 45.7% | **50.8%** |
| OCF/매출 | 61.4% | 70.1% | 71.1% | 57.5% | 63.1% | 59.7% |
| CAPEX/매출 | 37.9% | 52.9% | 47.8% | 43.9% | 33.0% | 33.7% |
| **FCF 마진** (OCF−CAPEX) | 23.6% | 17.2% | 23.3% | 13.5% | 30.1% | **26.1%** |
| **FCF/순이익** (이익의 질) | 0.62 | 0.46 | 0.53 | 0.34 | 0.75 | **0.58** |
| SBC 차감 FCF 마진 | 23.55% | 17.20% | 23.31% | 13.49% | 30.02% | 26.02% |

(*FY2020은 기초 잔액이 없어 기말 기준으로 계산. 2020~21 세율은 Yahoo 결측이라 [추정] 13%. 2020~21 차입금은 SEC 비유동사채, 2022~25는 Yahoo 총차입금이라 정의가 다르다.) [계산]

- **TTM(4Q25~3Q26)** [계산, 01_data 3절]: 영업이익률 58.0%(=2,866,830/4,944,817, 2Q26은 Yahoo 분기 영업이익 766,568 사용), FCF 1,457,584, FCF 마진 29.5%, FCF/순이익 0.57.
- **ROIC > WACC:** 6년 내내 ROIC가 29.8%~47.2%로 WACC 9.0%의 3~5배였다. 저점인 FY2023(반도체 다운사이클)에도 29.8%였다.
- **이익의 질:** 5년 평균 FCF/순이익은 0.55다. 순이익의 약 절반이 다시 CAPEX로 들어간다는 뜻이다. TSMC는 FCF를 순이익보다 체계적으로 적게 만드는 회사이므로 PER만으로 비교하면 실제보다 싸 보인다.
- **SBC:** FY2025 NT$1,246M으로 매출의 0.03%다(01_data 9절). SBC 차감 전후 FCF 차이는 사실상 0이다. 미장 피어(NVDA, INTC, GFS)는 SBC가 FCF 수익률을 0.2~1.1%p 깎는다(4절).

## 2. 성장 지표

| 지표 (NT$) | 3년 CAGR (FY2022→FY2025) | 5년 CAGR (FY2020→FY2025) |
|---|---|---|
| 매출 | 18.9% | 23.3% |
| 희석 EPS (회사/SEC) | 20.1% | 27.5% |
| FCF (OCF−CAPEX) | 23.4% | 25.8% |

[계산] 참고로 FY2026 가이던스가 암시하는 매출은 NT$5,561.8~5,625.4B(+46~48% YoY, NT$)이고, 컨센서스 EPS는 FY2026E 110.63, FY2027E 149.53이다(Yahoo, 01_data 8절). FY2025→FY2027E EPS CAGR은 **50.2%** [계산]이다. 최근 2년의 성장률은 5년 추세의 2배에 가깝다. 따라서 밸류에이션 결과는 이 고성장이 얼마나 오래 가느냐에 크게 좌우된다.

---

## 3. 역DCF (핵심)

### 3-1. 할인율(WACC) 가정과 근거

| 입력 | 값 | 근거 |
|---|---|---|
| 미국 10년물 | **5.12%** (2026-11-16) | `python3 tools/fred.py DGS10` 실행 결과(1년 전 4.13%). yfinance `^TNX` 5.10%(2026-11-17)로 교차 확인 |
| 대만 10년물 | **1.90%** [추정] | 11월 값은 확보하지 못했다(웹검색 2회, tradingeconomics.com WebFetch는 DNS 차단). 확보된 가장 최근 값은 2026-07 말 약 1.88%다(Trading Economics 보도, https://tradingeconomics.com/taiwan/government-bond-yield/news/569237 ). 2026-07-28 1.82% 보도도 있다(https://tradingeconomics.com/taiwan/government-bond-yield/news/570284 ). 이 값을 반올림해 썼다 |
| 베타 | 1.233 | yfinance `info` (TSM, 2330.TW 동일값), 2026-11-18 조회 |
| 주식위험프리미엄(ERP, 성숙시장) | 4.5% | [학습데이터, 최신 아님] Damodaran 성숙시장 ERP 4~4.6% 범위 |
| 국가위험프리미엄(대만) | 1.0% | [학습데이터, 최신 아님] Damodaran 대만 CRP는 1% 미만~1% 수준(Aa3 등급). 1.0%로 올려 잡았다 |
| 지정학 추가 프리미엄 | 0.5% [추정] | 양안 리스크의 꼬리 위험. CRP에 다 반영되지 않는다고 보고 대리가 판단해 더했다 |
| 자기자본비용 | **9.07%** | ① USD CAPM 5.12+1.233×4.5+1.0 = 11.67%에서 미·대만 금리차 3.22%p를 빼 TWD로 환산하면 8.45%. ② 현지 CAPM 1.90+1.233×(4.5+1.0) = 8.68%. ①②의 평균 8.57%에 0.5%p를 더했다 [계산] |
| 세전 부채비용 | 1.16% | 이자비용 12,370 / 총차입금 1,064,583 (Yahoo FY2025) [계산] |
| 부채 비중 | 1.9% | 총차입금 1,065,988 / (시총 56,402,883 + 차입금) [계산] |
| **WACC** | 8.92%를 **9.0%**로 반올림 | [계산] |

ADR 투자자 시각에서 덧붙이면, 미국 10년물이 5.12%로 1년 새 +0.99%p 올랐다. USD 기준 자기자본비용은 11.7% 안팎이다. USD로 받는 현금흐름에는 TWD 절상 기대(금리차만큼)를 더해야 결과가 같아지는데, 금리평가가 실제로 성립하지 않으면 ADR 투자자의 할인율은 더 높아진다. WACC 민감도는 5절에 있다.

### 3-2. 역DCF 결과

방법은 다음과 같다. 기준 FCF에서 10년간 일정한 성장률로 커지고, 이후 터미널 성장률 g=3%를 적용한다. 할인 시점은 기준일 2026-11-18부터의 mid-year convention이다. 이렇게 계산한 EV에 순현금을 더한 값이 시가총액과 같아지는 성장률을 구했다. 순현금은 현금+단기투자 4,094,653 − 총차입금 1,065,988 = **NT$3,028,665M**(3Q26)이다.

| 기준 FCF | WACC 8% | **WACC 9%** | WACC 10% |
|---|---|---|---|
| TTM FCF 1,457,584 → 2330 시총 NT$56.40T | 10.2% | **12.9%** | 15.2% |
| TTM FCF → ADR 가격 내포 시총 NT$61.46T | 11.4% | 14.0% | 16.4% |
| FY2025 FCF 992,378 → 2330 시총 | 15.2% | 18.0% | 20.5% |
| FY2025 FCF → ADR 내포 시총 | 16.4% | 19.2% | 21.7% |

[계산]

**CAPEX 사이클을 반영한 역DCF.** 기본 시나리오의 OCF 마진과 CAPEX 경로(4절)를 그대로 두고 매출 성장 경로의 크기만 조정했다. 이때 현재 주가와 맞는 10년 매출 CAGR은 **2330 기준 11.0%**(첫해 FY2027 +27.6%), **ADR 기준 12.2%**(FY2027 +30.5%)다 [계산].

해석(의견 아님, 숫자 비교):
- 현재 2330 주가가 요구하는 수준은 FCF가 10년간 연 12.9% 성장하는 것이다. 과거 3년 FCF CAGR 23.4%, 5년 25.8%의 약 절반이다.
- 기준점을 FY2025 FCF로 바꾸면 요구 성장률이 18.0%로 올라간다. TTM FCF는 AI 수요 정점 구간의 실적이다. 어느 기준점을 쓰느냐가 결론에 크게 영향을 준다.
- ADR 프리미엄 9%는 내포 성장률을 약 1.1%p 더 올린다.

### 3-3. FY2026 CAPEX 사이클 모델링 (기준 연도)

| 항목 | 값 | 근거 |
|---|---|---|
| FY2026E 매출 | NT$5,593,600M | 가이던스 암시 범위 5,561.8~5,625.4B의 중간값 (01_data 3-1) |
| 4Q26E 매출 | 1,694,873 | FY2026E − 1~3Q 누적 3,898,727 [계산] |
| 1~3Q26 CAPEX | NT$1,308,573M (US$40.64B) | 01_data 6-1 |
| 4Q26E CAPEX | US$21.36B × 32.947 = NT$703.7B | 가이던스 US$60~64B − 누적 = US$19.36~23.36B의 중간값 [계산] |
| **FY2026E CAPEX** | **NT$2,012,321M (매출의 36.0%, 현재 환율로 US$61.1B)** | [계산] |
| 4Q26E OCF | 매출 × 61% = 1,033,873 | [추정] TTM OCF/매출 63.3%보다 보수적으로 잡음 |
| FY2026E FCF | NT$1,423,669M (2330 시총 대비 FCF 수익률 2.52%) | [계산] |
| 4Q26E 잔여 FCF (DCF에 포함) | NT$330,125M | [계산] |
| 2027~2028 CAPEX | "2026~2028년 CAPEX는 직전 3년보다 유의미하게 높을 것" (회사, 수치 없음) | 01_data 6-1. 직전 3년(FY2023~25) 합계는 NT$3,188B다. 기본 시나리오의 2026~2028 합계 7,277B는 이 수준을 크게 넘는다 [계산] |

---

## 4. DCF 3개 시나리오

공통 가정: 명시 기간 FY2027~FY2036(10년), WACC 9.0%, FCF = 매출 × (OCF 마진 − CAPEX/매출), 순현금 3,028,665 가산, 주식수 25,932.36M주. SBC는 무시했다(매출의 0.03%).

### 4-1. 가정 표 [추정]

| 가정 | 약세 | 기본 | 강세 |
|---|---|---|---|
| 매출 성장 FY27/28/29/30/31 | +15 / +5 / **−5** / +8 / +6% | +30 / +20 / +15 / +12 / +10% | +38 / +25 / +20 / +16 / +14% |
| 매출 성장 FY32~36 | 6 / 5 / 5 / 4 / 4% | 9 / 8 / 7 / 6 / 5% | 12 / 10 / 9 / 8 / 7% |
| 10년 매출 CAGR [계산] | 5.2% | 12.0% | 15.6% |
| FY2027 매출 vs 컨센 7,691.2B | 6,433B | 7,272B (−5.5%) | 7,719B (≈컨센) |
| OCF 마진 (매출총이익률 대리변수) | 58% → 52% (FY2029~) | 61% → 55% (FY2033~) | 63% → 59% |
| CAPEX/매출 | 34 → 28% | 34 → 27% | 33 → 25% |
| 터미널 FCF 마진 | 24% | 28% | 34% |
| 터미널 성장률 g | 2.0% | 3.0% | 3.5% |
| 시나리오 설명 | AI 투자 소화로 2029년 매출 역성장. 해외 팹 희석과 경쟁으로 마진 하락. CAPEX는 약정 때문에 고공 유지 | 컨센보다 약간 낮은 성장이 점진적으로 둔화. 해외 팹 희석(회사 언급 3~4%)으로 마진 점감 | 컨센 수준 성장, 첨단 노드 가격 결정력 유지, CAPEX 효율 개선 |

비교 기준: 5년 평균 FCF 마진은 22.0%다(FY2021~25 평균, [계산] 17.2/23.3/13.5/30.1/26.1). 기본 시나리오의 터미널 FCF 마진 28%는 과거 평균보다 높다. 이는 현재 GM 66%(3Q26) 국면이 일부 지속된다는 가정이다.

### 4-2. 결과 [계산]

| 항목 (NT$ M) | 약세 | 기본 | 강세 |
|---|---|---|---|
| FY2036 FCF | 2,228,405 | 4,853,017 | 8,078,826 |
| FCF CAGR (TTM → FY2036) | 4.3% | 12.8% | 18.7% |
| PV(명시기간 FCF + 4Q26) | 11,882,184 | 22,719,530 | 33,163,820 |
| PV(터미널가치) | 13,575,009 | 34,829,047 | 63,557,931 |
| **EV 대비 터미널 비중** | **53.3%** | **60.5%** | **65.7%** |
| EV | 25,457,193 | 57,548,577 | 96,721,751 |
| 주주가치 (+순현금) | 28,485,858 | 60,577,242 | 99,750,416 |
| **주당 내재가치 (NT$)** | **1,098** | **2,336** | **3,847** |
| ADR당 (US$, ×5÷32.947) | 166.6 | 354.5 | 583.8 |
| 안전마진 vs 2330 NT$2,175 | −98.0% | +6.9% | +43.5% |
| 안전마진 vs ADR US$359.69 | −115.8% | −1.5% | +38.4% |

- 확률가중(25/50/25, [추정] 가중치)은 NT$2,404, ADR 환산 US$364.9다. 안전마진은 2330 기준 +9.5% [계산].
- **가정이 결과를 지배한다.** 기본 시나리오 EV의 **60.5%가 터미널가치**다. 즉 2036년 이후의 FCF가 현재 가치의 과반을 차지한다. 약세와 강세의 주당가치 차이는 3.5배(1,098 vs 3,847)다. 이 차이는 거의 전부 ① AI 수요 사이클의 지속 기간(매출 경로)과 ② CAPEX 강도에서 나온다.
- 기본 시나리오의 주당가치(2,336)는 현재가(2,175)와 ADR 원주 환산가(2,370) 사이에 있다. 기본 가정이 시장 가격과 거의 같다. 이는 역DCF 결과(내포 매출 CAGR 11.0~12.2% vs 기본 12.0%)와도 일치한다.

### 4-3. ADR 프리미엄

- ADR 가격 US$359.69 × 32.947 ÷ 5 = NT$2,370.1로, 2330 종가보다 **+9.0%** 높다(기준일이 11-17과 11-18로 하루 다르다) [계산].
- 내재가치를 ADR에 적용하면 같은 내재가치라도 안전마진이 2330보다 약 9%p 낮다. 기본 시나리오 기준 2330은 +6.9%, ADR은 −1.5%다.
- 프리미엄이 생기는 이유는 대만 외국인 투자 한도·결제 절차, 미국 투자자의 USD 거래 편의 수요, 그리고 원주→ADR 전환 제약(전환 한도) 때문이라고 일반적으로 알려져 있다 [학습데이터, 최신 아님]. 이 프리미엄이 0으로 수렴한다고 가정하면 ADR 보유자는 약 −8.3%(=1/1.09−1)의 추가 손익 요인을 안는다 [계산]. 반대로 프리미엄이 유지되면 이 요인은 생기지 않는다. 과거 프리미엄 범위는 데이터 없음(시도: 01_data에 시계열 없음).

---

## 5. 민감도

### 5-1. WACC × 터미널 성장률 (기본 시나리오, NT$/주) [계산]

| g \ WACC | 8.0% | 8.5% | **9.0%** | 9.5% | 10.0% |
|---|---|---|---|---|---|
| 2.0% | 2,495 | 2,300 | 2,133 | 1,989 | 1,863 |
| 2.5% | 2,636 | 2,414 | 2,227 | 2,067 | 1,928 |
| **3.0%** | 2,805 | 2,549 | **2,336** | 2,156 | 2,003 |
| 3.5% | 3,011 | 2,710 | 2,465 | 2,261 | 2,089 |
| 4.0% | 3,268 | 2,908 | 2,620 | 2,385 | 2,190 |

현재가 2,175 아래로 떨어지는 칸: WACC 9.5% 이상이면서 g ≤ 2.5%이거나, WACC 9.0%이면서 g=2.0%인 경우 등.

### 5-2. 매출총이익률 변화 × WACC (기본 시나리오, g=3%, NT$/주) [계산]

매출총이익률(GM) 변화분 × (1−세율 17%)만큼 OCF 마진을 평행 이동시킨 근사다.

| GM 변화 \ WACC | 8.0% | 8.5% | **9.0%** | 9.5% | 10.0% |
|---|---|---|---|---|---|
| −8%p (GM 약 58%, 해외팹 희석+경쟁) | 2,173 | 1,977 | 1,815 | 1,678 | 1,561 |
| −5%p | 2,410 | 2,192 | 2,010 | 1,857 | 1,727 |
| −3%p | 2,568 | 2,334 | 2,141 | 1,977 | 1,837 |
| **0** | 2,805 | 2,549 | **2,336** | 2,156 | 2,003 |
| +3%p | 3,042 | 2,763 | 2,531 | 2,336 | 2,169 |

### 5-3. 토네이도 (기본 NT$2,336 기준, 하나씩 변경) [계산]

| 가정 | 하방 | 상방 | 변화율 |
|---|---|---|---|
| 매출 성장 경로 ×0.75 / ×1.25 (10년 CAGR 9.0% / 14.9%) | 1,876 | 2,904 | −19.7% / +24.3% |
| **WACC +1%p / −1%p** | 2,003 | 2,805 | **−14.3% / +20.1%** |
| OCF 마진 ±4%p (≈GM ±5%p) | 2,022 | 2,650 | −13.4% / +13.4% |
| CAPEX/매출 +4%p / −4%p | 2,022 | 2,650 | −13.4% / +13.4% |
| 터미널 g −1%p / +1%p | 2,133 | 2,620 | −8.7% / +12.2% |

**가장 민감한 단일 가정은 WACC(대만 지정학 프리미엄 포함)로 지정했다.** 이유는 세 가지다.
1. 숫자 하나로 정의되는 파라미터 가운데 현실적인 ±1%p 범위에서 변동폭이 가장 크다.
2. 근거가 가장 약하다. 대만 10년물 11월 값을 확보하지 못했고, 지정학 프리미엄은 대리의 판단이다.
3. 미국 10년물이 1년 새 +0.99%p 움직였다.

다만 **매출 성장 경로 전체(AI 수요 지속 기간)**는 단일 파라미터가 아닌데도 영향이 더 크다. 아울러 OCF 마진 ±4%p와 CAPEX 강도 ±4%p는 FCF 마진에 같은 크기로 작용하므로 결과가 똑같다. 즉 "GM이 4%p 떨어진다"와 "CAPEX가 매출의 4%p만큼 더 든다"는 가치에 미치는 영향이 같다.

---

## 6. 멀티플

### 6-1. 자사 5년 평균 대비

연말 종가(01_data 7-1)와 연간 재무로 계산했다. EV = 시총 + 총차입금 − 현금이고, EBITDA는 Yahoo 연간 값이다(FY2021 EBITDA는 D&A 결측이라 제외). [계산]

| 지표 | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | 평균 | **현재** | 현재 vs 평균 |
|---|---|---|---|---|---|---|---|---|
| PER (종가/EPS) | 26.9 | 11.7 | 18.1 | 24.1 | 23.4 | 20.8 | **22.1** (TTM EPS 98.26) | +6.3% |
| PBR | 7.42 | 4.01 | 4.48 | 6.57 | 7.51 | 6.00 | **8.06** | +34.3% |
| EV/EBITDA | — | 7.0 | 9.8 | 12.9 | 14.0 | 10.9 (4년) | **14.9** (TTM, 영업이익+D&A) | +36.3% |
| FCF 수익률 | 1.71% | 4.54% | 1.90% | 3.12% | 2.47% | 2.75% | **2.58%** (TTM) | −0.17%p |
| PEG (PER / 직전 3년 EPS CAGR) | — | — | 0.97 | 0.96 | 1.17 | 1.03 | **1.10** (22.1/20.1) | +6.6% |

- 선행 PER: FY2026E 19.7배, FY2027E 14.5배다(컨센 EPS 110.63 / 149.53, 01_data 8절) [계산].
- 선행 PEG(TTM PER / FY2025→FY2027E EPS CAGR 50.2%)는 0.44, Yahoo trailingPegRatio는 0.61이다. 선행 PEG는 2026~27년 고성장이 지속된다는 컨센서스를 그대로 받아들인 값이라 낮게 나온다.
- 멀티플을 자사 평균으로 되돌렸을 때의 주당가치(교차 점검) [계산]: PER 20.8 × TTM EPS = NT$2,047, × FY2026E EPS = NT$2,304. EV/EBITDA 10.9 × TTM = NT$1,621. FCF 수익률 2.75% → NT$2,044. PBR 6.0 → NT$1,619. 범위는 **NT$1,619~2,304**다. 이익 기준 멀티플(PER)은 현재가 근처이고, 자산·EBITDA 기준은 현재가보다 25% 이상 낮다. EBITDA와 장부가치 대비 이익률이 과거보다 크게 높아진 상태(ROE 35.8%)이기 때문이다.

### 6-2. 피어 대비 (TTM)

출처: Yahoo Finance via yfinance(`info`, `quarterly_income_stmt`, `quarterly_cashflow`, `quarterly_balance_sheet`), 2026-11-18 조회. 직전 4분기 합계로 계산했다 [계산].

일관성을 위해 EBITDA = 영업이익 + D&A, FCF = OCF − CAPEX로 직접 계산했다(Yahoo의 `enterpriseToEbitda`, `freeCashflow`는 쓰지 않음). ASML은 시총 USD를 EURUSD 1.0964(yfinance `EURUSD=X`, 2026-11-18)로 EUR 환산했다. PEG는 Yahoo `trailingPegRatio`(Yahoo 정의, 5년 기대성장 기반)다.

| 회사 | 시총 (현지통화) | PER | PBR | EV/EBITDA | FCF 수익률 | SBC 차감 FCF 수익률 | PEG (Yahoo) | 비고 |
|---|---|---|---|---|---|---|---|---|
| **TSMC (2330)** | NT$56.40T | **22.1** | **8.06** | **14.9** | **2.58%** | 2.58% | 0.61 | 순이익은 회사 기준 |
| Samsung Electronics (005930.KS) | ₩1,267.9T | 6.0 | 2.09 | 3.0 | 11.08% | 데이터 없음 | 0.09 | 메모리 호황 이익. Yahoo 시총은 우선주 포함 여부 미확인 |
| Intel (INTC) | US$293.2B | 적자(N/M) | 2.55 | 15.5 | 1.29% | 0.46% | 데이터 없음 | TTM 순손실 −US$12.0B |
| ASML (ASML) | €486.2B | 36.1 | 22.04 | 29.3 | 4.32% | 4.27% | 0.75 | 장비, 저자본집약 |
| NVIDIA (NVDA) | US$3,754B | 19.5 | 16.39 | 18.5 | 3.38% | 3.19% | 0.19 | TTM은 FY27 2Q(2026-07-31)까지 |
| GlobalFoundries (GFS) | US$22.1B | 112.1 | 1.85 | 10.2 | 1.95% | 0.85% | 0.59 | 순수 파운드리 피어 |
| 피어 중앙값 (5개사) | — | 27.8 (흑자 4개사) | 2.55 | 15.5 | 3.38% | — | 0.39 (4개사) | [계산] |

해석(숫자만):
- TSMC의 PER 22.1은 흑자 피어 중앙값 27.8보다 낮다. 다만 그 중앙값은 이익이 극히 적은 GFS(PER 112)와 ASML 때문에 올라간 값이다. 이익 규모가 큰 NVDA(19.5)와 Samsung(6.0)보다는 높다.
- EV/EBITDA 14.9는 피어 중앙값 15.5와 비슷하다.
- FCF 수익률 2.58%는 ASML, NVDA, Samsung보다 낮다. TSMC의 CAPEX 강도(36%)가 피어보다 훨씬 높기 때문이다(ASML·NVDA는 매출의 5% 미만, [계산] 위 분기 데이터).
- PBR 8.06은 제조업 피어(Samsung, INTC, GFS 1.9~2.6배)의 3~4배다. ROE 차이(TSMC 35.8% vs GFS 1.7%, Yahoo)로 설명되는 부분이다.
- 피어 간 비교 한계: 회계기준(IFRS, K-IFRS, US GAAP)과 결산 시점이 다르고, 사업모델(장비·팹리스·IDM·메모리)도 이질적이다. 순수 파운드리 피어는 GFS뿐이다.

---

## 7. 결론 표

| 항목 | 값 |
|---|---|
| DCF 내재가치 범위 (NT$/주) | **1,098 (약세) ~ 2,336 (기본) ~ 3,847 (강세)**, 확률가중 25/50/25 = 2,404 |
| ADR 환산 (US$/ADR) | 166.6 ~ 354.5 ~ 583.8, 확률가중 364.9 |
| 멀티플 교차점검 범위 (자사 5년 평균 회귀) | NT$1,619 ~ 2,304 |
| 현재가 | NT$2,175 (2330) / US$359.69 (ADR, 원주 대비 +9.0%) |
| 안전마진 (V−P)/V, 2330 | 약세 −98.0% / **기본 +6.9%** / 강세 +43.5% / 확률가중 +9.5% |
| 안전마진, ADR | 약세 −115.8% / **기본 −1.5%** / 강세 +38.4% |
| 역DCF 내포 성장 | TTM FCF 기준 10년 FCF CAGR 12.9%(2330) / 14.0%(ADR). 기본 마진·CAPEX 경로에서 매출 CAGR 11.0% / 12.2% |
| 터미널가치 비중 | 기본 EV의 60.5% (약세 53.3%, 강세 65.7%) |
| **가장 민감한 가정** | **WACC: ±1%p → 주당 −14.3% / +20.1%** (5-1 민감도 표). 매출 경로 ±25% → −19.7% / +24.3% |
| 핵심 불확실성(데이터) | 대만 10년물 11월 값 미확보, ERP·CRP는 [학습데이터], FY2025 현금흐름은 Yahoo(회사 원문 미대조), 2027년 이후 CAPEX 가이던스 없음 |

---

## 부록 A. 입력값 일람

| 입력 | 값 | 출처 |
|---|---|---|
| 주가 2330.TW | NT$2,175.00 (2026-11-18) | 01_data 7-1 (yfinance) |
| ADR TSM | US$359.69 (2026-11-17) | 01_data 7-1 |
| USD/TWD | 32.947 | 01_data 7-4 |
| 보통주 수 | 25,932.36M주 | 01_data 7-2 |
| 현금+단기투자 / 총차입금 (3Q26) | 4,094,653 / 1,065,988 | 01_data 3절 |
| 현금성자산 (3Q26, 멀티플용 EV) | 3,621,894 | 01_data 3절 |
| TTM 순이익 / EPS / FCF | 2,547,850 / 98.26 / 1,457,584 | 01_data 3절 (회사 기준) |
| TTM 영업이익+D&A | 3.613T (D&A 분기: 162,112 / 165,450 / 198,538 / 220,204) | yfinance 2330.TW quarterly, 2026-11-18 |
| 연간 EBITDA FY22~25 | 1,593,077 / 1,523,507 / 2,079,132 / 2,742,122 | yfinance 2330.TW income_stmt |
| 세금비용/세전이익 FY22~25 | 150,778/1,144,072; 128,289/979,317; 248,316/1,405,840; 346,530/2,041,655 | 동상 |
| 이자비용 FY2025 | 12,370 | 동상 |
| 1~3Q26 OCF / CAPEX | 2,402,117 / 1,308,573 | 01_data 3절 (Yahoo) |
| FY2026 CAPEX 가이던스 | US$60~64B, 1~9월 US$40.64B | 01_data 6-1 |
| 컨센 EPS FY26E/27E, 매출 FY27E | 110.63 / 149.53, 7,691.2B | 01_data 8절 |
| DGS10 | 5.12% (2026-11-16) | `python3 tools/fred.py DGS10` (2026-11-18 실행) |
| 대만 10년물 | 1.90% [추정] (2026-07 말 1.88%) | Trading Economics 보도 (위 링크) |
| 베타 | 1.233 | yfinance info |
| EURUSD | 1.0964 | yfinance EURUSD=X, 2026-11-18 |
| 피어 원자료 | 6-2절 표 | yfinance, 2026-11-18 |

## 부록 B. 계산 코드

재현 방법: Python 3, yfinance 1.8.0. 피어 원자료는 B-3 스크립트가 `peers.json`, `ttm.json`으로 저장하고, B-4가 이 파일을 읽는다. scipy가 없는 환경이라 brentq는 이분법으로 직접 구현했다.

### B-1 과거 지표 (hist.py)

```python
# 과거 지표 계산 (단위 NT$ M). 입력: 01_data.md 2-1/3절, Yahoo(yfinance) EBITDA·D&A·세금
Y=[2020,2021,2022,2023,2024,2025]
rev=[1339255,1587415,2263891,2161736,2894308,3809054]
op=[566784,649981,1121279,921466,1322053,1936096]
ni=[510744,592359,992923,851740,1158380,1717900]   # FY2025 회사 기준 ≈1,717.9B (01_data ^d)
eps=[19.70,22.84,38.29,32.85,44.67,66.25]
ocf=[822666,1112161,1610599,1241967,1826177,2274976]
capex=[507239,839196,1082672,949817,956006,1282597]
sbc=[7,8,302,483,1243,1246]
eq=[1834811,2149260,2903020,3429522,4244266,5355039]
cash=[660171,1064990,1342814,1465428,2127627,2767856]
debt=[254105,610071,888174,956258,1047042,1064583]  # 2020-21 SEC 비유동사채, 2022-25 Yahoo 총차입금
tax={2022:150777.5/1144072.2,2023:128288.8/979316.5,2024:248316.1/1405840.0,2025:346529.8/2041654.7}
for y in (2020,2021): tax[y]=0.13  # [추정] 결측
ebitda={2022:1593076.5,2023:1523506.8,2024:2079132.0,2025:2742121.5}
px={2021:615.0,2022:448.5,2023:593.0,2024:1075.0,2025:1550.0}
sh={2021:25930.3,2022:25930.4,2023:25932.1,2024:25932.7,2025:25932.5}
fcf=[o-c for o,c in zip(ocf,capex)]
rows=[]
for i,y in enumerate(Y):
    ic=eq[i]+debt[i]-cash[i]
    ic_prev=(eq[i-1]+debt[i-1]-cash[i-1]) if i>0 else ic
    nopat=op[i]*(1-tax[y])
    roic=nopat/((ic+ic_prev)/2)
    roe=ni[i]/((eq[i]+eq[i-1])/2) if i>0 else ni[i]/eq[i]
    print(f"{y} tax={tax[y]:.1%} IC={ic:,.0f} ROIC={roic:.1%} ROE={roe:.1%} OPM={op[i]/rev[i]:.1%} FCF={fcf[i]:,} FCFm={fcf[i]/rev[i]:.1%} FCF/NI={fcf[i]/ni[i]:.2f} SBCadjFCFm={(fcf[i]-sbc[i])/rev[i]:.2%} capex/rev={capex[i]/rev[i]:.1%} OCFm={ocf[i]/rev[i]:.1%}")
cagr=lambda a,b,n:(b/a)**(1/n)-1
for nm,s in [("rev",rev),("eps",eps),("fcf",fcf),("ni",ni)]:
    print(nm,"3y",f"{cagr(s[2],s[5],3):.1%}","5y",f"{cagr(s[0],s[5],5):.1%}")
print("--- multiples at year-end")
mult={}
for y in range(2021,2026):
    i=Y.index(y); mc=px[y]*sh[y]; ev=mc+debt[i]-cash[i]
    pe=px[y]/eps[i]; pb=mc/eq[i]; fy=fcf[i]/mc
    eve=ev/ebitda[y] if y in ebitda else None
    peg=pe/(cagr(eps[i-1] if y>2021 else 19.70, eps[i],1)*100)
    mult[y]=(pe,pb,eve,fy)
    print(y,f"PE={pe:.1f} PB={pb:.2f} EV/EBITDA={eve if eve is None else round(eve,1)} FCFy={fy:.2%} EV={ev:,.0f}")
import statistics as st
print("avg PE",st.mean(m[0] for m in mult.values()),"avg PB",st.mean(m[1] for m in mult.values()),
      "avg EV/EBITDA(22-25)",st.mean(m[2] for m in mult.values() if m[2]),"avg FCFy",st.mean(m[3] for m in mult.values()))
# PEG 5y: PE / 이후 실현 아닌 직전 3년 EPS CAGR
for y in range(2023,2026):
    i=Y.index(y); g=cagr(eps[i-3],eps[i],3)*100 if i>=3 else None
    print(y,"PEG(PE/trailing3yEPS CAGR)",round(mult[y][0]/g,2), round(g,1))
```

### B-2 DCF·역DCF·민감도 (dcf.py)

```python
import numpy as np
def brentq(f,a,b,tol=1e-10):
    fa=f(a)
    for _ in range(300):
        m=(a+b)/2; fm=f(m)
        if (fm>0)==(fa>0): a,fa=m,fm
        else: b=m
        if b-a<tol: break
    return (a+b)/2
# ---------- 입력 ----------
SH=25932.36        # 보통주 M주 (01_data 7-2)
PX=2175.0          # 2330.TW 2026-11-18
MCAP=PX*SH         # NT$ M
FX=32.947          # USD/TWD 2026-11-18
ADR_PX=359.69      # TSM 2026-11-17
NETCASH=4094653-1065988   # 현금+단기투자 − 총차입금, 3Q26 (01_data 3절)
# WACC
RF_US=5.12; RF_TW=1.90   # FRED DGS10 2026-11-16 / 대만 10Y 2026-07 말 약 1.88% [추정 반올림]
BETA=1.233; ERP=4.5; CRP=1.0; GEO=0.5
coe_us=RF_US+BETA*ERP+CRP                     # USD 기준
coe_tw_from_us=coe_us-(RF_US-RF_TW)           # 금리차(=기대 환율변화)로 TWD 환산
coe_tw_local=RF_TW+BETA*(ERP+CRP)             # 현지 CAPM
coe=round((coe_tw_from_us+coe_tw_local)/2+GEO,2)
D=1065988; E=MCAP; kd=12370.4/1064583*100; tax=0.17
wacc=E/(D+E)*coe + D/(D+E)*kd*(1-tax)
print(f"CoE US={coe_us:.2f} TWfromUS={coe_tw_from_us:.2f} TWlocal={coe_tw_local:.2f} CoE used={coe:.2f} kd={kd:.2f} WACC={wacc:.2f}")
WACC=round(wacc*2)/2/100   # 0.5%p 단위 반올림
print("WACC used",WACC)
# ---------- FY2026E ----------
rev26=(5561.8e3+5625.4e3)/2                 # 가이던스 암시 중간값 NT$ M
q4rev=rev26-3898727
ocf_9m=698976+783365+919776
capex_9m=351706+508395+448472
q4capex_usd=(19.36+23.36)/2*1e3              # US$ M
q4capex=q4capex_usd*FX
q4ocf=q4rev*0.61                             # [추정] TTM OCF/매출 63%보다 보수적
capex26=capex_9m+q4capex; ocf26=ocf_9m+q4ocf
fcf_q4=q4ocf-q4capex
print(f"rev26={rev26:,.0f} q4rev={q4rev:,.0f} capex26={capex26:,.0f} (int {capex26/rev26:.1%}) ocf26={ocf26:,.0f} fcf26={ocf26-capex26:,.0f} q4FCF={fcf_q4:,.0f}")
T0=0.12  # 2026-11-18 → 2026-12-31 (년)
def dcf(growth, ocfm, capexi, g, wacc=WACC, ret_detail=False, ocf_shift=0.0):
    rev=rev26; pv=fcf_q4/(1+wacc)**(T0/2); rows=[]
    for i,(gr,om,ci) in enumerate(zip(growth,ocfm,capexi)):
        rev*=1+gr; f=rev*(om+ocf_shift-ci); t=T0+i+0.5
        pv+=f/(1+wacc)**t; rows.append((2027+i,rev,om+ocf_shift,ci,f))
    tv=rows[-1][4]*(1+g)/(wacc-g); pvtv=tv/(1+wacc)**(T0+10)
    ev=pv+pvtv; eq=ev+NETCASH; ps=eq/SH
    if ret_detail: return dict(rows=rows,pv=pv,pvtv=pvtv,ev=ev,eq=eq,ps=ps,tvshare=pvtv/ev)
    return ps
S={
 "bear":dict(growth=[.15,.05,-.05,.08,.06,.06,.05,.05,.04,.04], ocfm=[.58,.55,.52,.52,.52,.52,.52,.52,.52,.52],
             capexi=[.34,.33,.30,.29,.28,.28,.28,.28,.28,.28], g=.02),
 "base":dict(growth=[.30,.20,.15,.12,.10,.09,.08,.07,.06,.05], ocfm=[.61,.60,.59,.58,.57,.56,.55,.55,.55,.55],
             capexi=[.34,.32,.30,.29,.28,.27,.27,.27,.27,.27], g=.03),
 "bull":dict(growth=[.38,.25,.20,.16,.14,.12,.10,.09,.08,.07], ocfm=[.63,.63,.62,.61,.60,.60,.59,.59,.59,.59],
             capexi=[.33,.31,.29,.27,.26,.25,.25,.25,.25,.25], g=.035),
}
out={}
for k,s in S.items():
    r=dcf(s["growth"],s["ocfm"],s["capexi"],s["g"],ret_detail=True); out[k]=r
    rc=np.prod([1+x for x in s["growth"]])**(1/10)-1
    print(f"\n[{k}] rev CAGR10={rc:.1%} g={s['g']:.1%} EV={r['ev']:,.0f} PV(FCF)={r['pv']:,.0f} PV(TV)={r['pvtv']:,.0f} TV share={r['tvshare']:.1%}")
    print(f"  equity={r['eq']:,.0f} per share NT${r['ps']:,.0f}  ADR US${r['ps']*5/FX:,.1f}  MoS vs 2175={(r['ps']-PX)/r['ps']:.1%}  MoS ADR vs 359.69={(r['ps']*5/FX-ADR_PX)/(r['ps']*5/FX):.1%}")
    for y,rv,om,ci,f in r["rows"]:
        print(f"  {y} rev={rv:,.0f} OCFm={om:.0%} capex%={ci:.0%} capex={rv*ci:,.0f} FCF={f:,.0f} FCFm={om-ci:.0%}")
    # 터미널 재투자 점검: 2036 capex / (감가상각 proxy 없음) -> NOPAT 대비 재투자율
# ---------- 역DCF ----------
target=MCAP-NETCASH
adr_mcap=ADR_PX/5*FX*SH; target_adr=adr_mcap-NETCASH
print(f"\nMCAP={MCAP:,.0f} target EV={target:,.0f}  ADR-implied MCAP={adr_mcap:,.0f} prem={adr_mcap/MCAP-1:.1%}")
def rev_fcf(base,g_term,wacc,tgt):
    def f(x):
        pv=0; c=base
        for i in range(10):
            c*=1+x; pv+=c/(1+wacc)**(T0+i+0.5)
        tv=c*(1+g_term)/(wacc-g_term)/(1+wacc)**(T0+10)
        return pv+tv-tgt
    return brentq(f,-0.5,1.0)
ttm_fcf=1457584; fy25=992378
for lbl,base in [("TTM FCF 1,457,584",ttm_fcf),("FY2025 FCF 992,378",fy25)]:
    for w in [0.08,WACC,0.10]:
        print(f"reverse FCF CAGR base={lbl} WACC={w:.1%} g=3%: local {rev_fcf(base,.03,w,target):.1%}  ADR-implied {rev_fcf(base,.03,w,target_adr):.1%}")
# 역DCF B: 기본 시나리오 마진·CAPEX 경로 유지, 매출 성장률을 일정 비율로 스케일 → 내포 매출 CAGR
b=S["base"]
def implied_scale(tgt_ps):
    f=lambda k: dcf([x*k for x in b["growth"]],b["ocfm"],b["capexi"],b["g"])-tgt_ps
    k=brentq(f,-2,3); rc=np.prod([1+x*k for x in b["growth"]])**(1/10)-1; return k,rc
for lbl,p in [("2330",PX),("ADR",ADR_PX/5*FX)]:
    k,rc=implied_scale(p); print(f"implied revenue CAGR (base margins/capex) {lbl}: scale={k:.2f} CAGR={rc:.1%}, yr1={b['growth'][0]*k:.1%}")
# 내포 FCF CAGR 대비 기본시나리오 FCF CAGR
fb=out["base"]["rows"][-1][4]; print("base FCF CAGR TTM->2036", (fb/ttm_fcf)**(1/10.0)-1)
for k in out: print(k,"FCF CAGR TTM->2036",(out[k]["rows"][-1][4]/ttm_fcf)**(1/10)-1)
# ---------- 민감도 ----------
print("\nWACC x g (base, NT$/share)")
ws=[0.08,0.085,0.09,0.095,0.10]; gs=[0.02,0.025,0.03,0.035,0.04]
print("g\\WACC",ws)
for g in gs: print(g,[round(dcf(b["growth"],b["ocfm"],b["capexi"],g,wacc=w)) for w in ws])
print("\nOCF margin shift x WACC (g=3%)")
for sh_ in [-0.06,-0.04,-0.02,0,0.02,0.04]:
    print(sh_,[round(dcf(b["growth"],b["ocfm"],b["capexi"],.03,wacc=w,ocf_shift=sh_)) for w in ws])
print("\nTornado (base, one at a time)")
base_ps=dcf(b["growth"],b["ocfm"],b["capexi"],b["g"])
tests={
 "WACC ±1%p":(dcf(b["growth"],b["ocfm"],b["capexi"],.03,wacc=WACC+.01),dcf(b["growth"],b["ocfm"],b["capexi"],.03,wacc=WACC-.01)),
 "terminal g ±1%p":(dcf(b["growth"],b["ocfm"],b["capexi"],.02),dcf(b["growth"],b["ocfm"],b["capexi"],.04)),
 "OCF margin ±4%p (≈GM ±5%p)":(dcf(b["growth"],b["ocfm"],b["capexi"],.03,ocf_shift=-.04),dcf(b["growth"],b["ocfm"],b["capexi"],.03,ocf_shift=.04)),
 "CAPEX intensity ±4%p":(dcf(b["growth"],b["ocfm"],[c+.04 for c in b["capexi"]],.03),dcf(b["growth"],b["ocfm"],[c-.04 for c in b["capexi"]],.03)),
 "revenue growth ×0.75/×1.25":(dcf([x*.75 for x in b["growth"]],b["ocfm"],b["capexi"],.03),dcf([x*1.25 for x in b["growth"]],b["ocfm"],b["capexi"],.03)),
}
print("base",round(base_ps))
for k,(lo,hi) in tests.items(): print(f"{k}: {lo:,.0f} / {hi:,.0f}  ({lo/base_ps-1:+.1%} / {hi/base_ps-1:+.1%})")
print("\nGM sensitivity table: OCF shift approximates GM shift ×0.83 (1-tax). GM shift x WACC")
for gm in [-0.08,-0.05,-0.03,0,0.03]:
    print(gm,[round(dcf(b["growth"],b["ocfm"],b["capexi"],.03,wacc=w,ocf_shift=gm*0.83)) for w in ws])
```

### B-3 피어 원자료 수집 (peers.py, ttm.py)

```python
import yfinance as yf, json
keys=["shortName","currentPrice","regularMarketPrice","marketCap","enterpriseValue","trailingPE","forwardPE","priceToBook","enterpriseToEbitda","ebitda","freeCashflow","trailingEps","forwardEps","pegRatio","trailingPegRatio","earningsGrowth","revenueGrowth","financialCurrency","currency","operatingMargins","grossMargins","returnOnEquity","totalDebt","totalCash","sharesOutstanding"]
out={}
for t in ["2330.TW","TSM","005930.KS","INTC","ASML","NVDA","AVGO","GFS"]:
    try:
        i=yf.Ticker(t).info
        out[t]={k:i.get(k) for k in keys}
    except Exception as e:
        out[t]=str(e)
json.dump(out,open("peers.json","w"),indent=1)
print(json.dumps(out,indent=1))
```

### B-3b

```python
import yfinance as yf, json, pandas as pd
def g(df,names):
    for n in names:
        if n in df.index: return df.loc[n]
    return None
out={}
for t in ["2330.TW","005930.KS","INTC","ASML","NVDA","GFS"]:
    tk=yf.Ticker(t); r={}
    try:
        qi=tk.quarterly_income_stmt; qc=tk.quarterly_cashflow; qb=tk.quarterly_balance_sheet
        r["q_dates"]=[str(c.date()) for c in qi.columns[:4]]
        for lab,df,names in [("NI",qi,["Net Income Common Stockholders","Net Income"]),("EBITDA",qi,["EBITDA","Normalized EBITDA"]),("OpInc",qi,["Operating Income"]),("Rev",qi,["Total Revenue"]),
                             ("OCF",qc,["Operating Cash Flow"]),("CAPEX",qc,["Capital Expenditure"]),("DA",qc,["Depreciation And Amortization","Depreciation Amortization Depletion"]),("SBC",qc,["Stock Based Compensation"])]:
            s=g(df,names)
            r[lab+"_q"]=None if s is None else [None if pd.isna(x) else float(x) for x in s.iloc[:4]]
        for lab,names in [("Equity",["Stockholders Equity","Common Stock Equity"]),("Debt",["Total Debt"]),("Cash",["Cash Cash Equivalents And Short Term Investments","Cash And Cash Equivalents"])]:
            s=g(qb,names); r[lab]=None if s is None else float(s.iloc[0]); r[lab+"_date"]=str(qb.columns[0].date())
    except Exception as e: r["err"]=str(e)
    if t=="2330.TW":
        ci=tk.income_stmt; cc=tk.cashflow
        r["annual_EBITDA"]={str(c.date()):float(v) for c,v in g(ci,["EBITDA"]).items() if not pd.isna(v)}
        r["annual_DA"]={str(c.date()):float(v) for c,v in g(cc,["Depreciation And Amortization","Depreciation Amortization Depletion"]).items() if not pd.isna(v)}
        r["annual_tax"]={str(c.date()):float(v) for c,v in g(ci,["Tax Rate For Calcs"]).items() if not pd.isna(v)}
        r["annual_pretax"]={str(c.date()):float(v) for c,v in g(ci,["Pretax Income"]).items() if not pd.isna(v)}
        r["annual_taxprov"]={str(c.date()):float(v) for c,v in g(ci,["Tax Provision"]).items() if not pd.isna(v)}
        r["annual_interest"]={str(c.date()):float(v) for c,v in g(ci,["Interest Expense"]).items() if not pd.isna(v)}
    out[t]=r
json.dump(out,open("ttm.json","w"),indent=1)
print(json.dumps(out,indent=1))
```

### B-4 피어 멀티플 (peers_calc.py, ../ 경로는 B-3 산출물)

```python
import json
d=json.load(open("../ttm.json")); info=json.load(open("../peers.json"))
EURUSD=1.0963709
def calc(t,mc_fin,debt,cash,eq,growth_note=None):
    r=d[t]; s=lambda k:sum(x for x in r[k] if x is not None)
    ni=s("NI_q"); ocf=s("OCF_q"); capex=-s("CAPEX_q"); da=s("DA_q"); op=s("OpInc_q"); sbc=s("SBC_q") if r.get("SBC_q") else 0
    ebitda=op+da   # 일관된 정의: 영업이익+감가상각 (Yahoo EBITDA는 일회성 포함되어 INTC 등 왜곡)
    ev=mc_fin+debt-cash
    fcf=ocf-capex
    return dict(PE=mc_fin/ni, PB=mc_fin/eq, EV_EBITDA=ev/ebitda, FCFy=fcf/mc_fin, FCFy_sbc=(fcf-sbc)/mc_fin, ni=ni, ebitda=ebitda, fcf=fcf, ev=ev, mc=mc_fin, sbc=sbc)
res={}
# TSMC: 시총 NT$, 회사기준 TTM 순이익 2,547,850M (01_data), 현금=현금성자산(과거 멀티플과 일관)
t=calc("2330.TW",56402.9e9,1065.988e9,3621.894e9,6997.901e9)
t["PE"]=56402.9e9/2547.850e9
res["TSMC(2330)"]=t
res["Samsung"]=calc("005930.KS",info["005930.KS"]["marketCap"],info["005930.KS"]["totalDebt"],info["005930.KS"]["totalCash"],d["005930.KS"]["Equity"])
for k in ["INTC","NVDA","GFS"]:
    res[k]=calc(k,info[k]["marketCap"],d[k]["Debt"],d[k]["Cash"],d[k]["Equity"])
res["ASML"]=calc("ASML",info["ASML"]["marketCap"]/EURUSD,d["ASML"]["Debt"],d["ASML"]["Cash"],d["ASML"]["Equity"])
for k,v in res.items():
    print(f"{k:12s} PE={v['PE']:.1f} PB={v['PB']:.2f} EV/EBITDA={v['EV_EBITDA']:.1f} FCFy={v['FCFy']:.2%} FCFy-SBC={v['FCFy_sbc']:.2%} NI={v['ni']:.4g} EBITDA={v['ebitda']:.4g} FCF={v['fcf']:.4g} MC={v['mc']:.4g}")
# forward PE / PEG
peg={k:info[k]["trailingPegRatio"] for k in info}
fpe={k:info[k]["forwardPE"] for k in info}
print("Yahoo trailingPegRatio",peg); print("Yahoo forwardPE",fpe)
# TSMC PEG: TTM PER / EPS CAGR FY2025->FY2027E
g=(149.53/66.25)**0.5-1; print("TSMC EPS CAGR 25->27E",g, "PEG",(2175/98.26)/(g*100))
print("TSMC fwd PE 26E",2175/110.63,"27E",2175/149.53)
```

### B-5 교차점검·확률가중 (extra.py)

```python
import numpy as np
exec(open("dcf.py").read().split("out={}")[0])
b=S["base"]
for k in (0.75,1.25): print(k, np.prod([1+x*k for x in b["growth"]])**0.1-1)
v={k:dcf(S[k]["growth"],S[k]["ocfm"],S[k]["capexi"],S[k]["g"]) for k in S}
pw=0.25*v["bear"]+0.5*v["base"]+0.25*v["bull"]; print("prob-weighted 25/50/25",pw,(pw-PX)/pw, pw*5/FX)
SH_=25932.36
print("PE avg20.83 x TTM98.26",20.83*98.26," x FY26E110.63",20.83*110.63)
ebitda_ttm=3.613e6; netcash_c=3621894-1065988
print("EV/EBITDA 10.93 x TTM", (10.93*ebitda_ttm+netcash_c)/SH_)
print("FCFy 2.75% TTM",1457584/0.0275/SH_)
print("PB avg 6.00 x BVPS",6.0*6997901/SH_)
print("ADR price NT equiv",ADR_PX/5*FX)
# 기본 시나리오 FY2027 매출 vs 컨센 7,691.2B
print("base 2027 vs cons", 7271680/7691200-1)
```
