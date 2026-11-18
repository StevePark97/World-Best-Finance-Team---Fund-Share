# 05_redteam — TSMC (NYSE: TSM ADR / TWSE: 2330)

- **작성:** 차장(레드팀) · **작성일:** 2026-11-18
- **역할:** 이 문서는 매수하면 안 되는 이유만 다룬다. 균형 잡힌 판단은 이사(06)가 한다.
- **데이터 기준일:** 2330.TW NT$2,175 (2026-11-18), TSM US$359.69 (2026-11-17), USD/TWD 32.947, 재무 3Q26까지. 앞 리포트(01~04)의 기준일을 그대로 쓴다.
- **1차 원문 (이번에 새로 확보한 것 포함, 모두 `sources/`에 저장):**
  - `TSM_20-F_FY2025.txt`: 20-F FY2025, 접수 2026-04-16, accession 0001628280-26-025362. 이하 "20-F FY25".
  - `TSM_20-F_FY2024.txt`: 20-F FY2024, accession 0001193125-25-083423. curl로 받아 텍스트로 변환. 이하 "20-F FY24".
  - `TSM_6-K_4Q25_earnings.txt`: 4Q25 실적 보도자료 6-K (2026-01-15).
  - `US_Proclamation_11002_Sec232_semis.txt`: Federal Register Vol.91 No.12 (2026-01-20), Proclamation 11002.
- **태그:** `[계산]` 차장 Python 계산 (부록 코드) · `[추정]` 차장 판단 · `[2차출처]` · `[학습데이터, 최신 아님]`
- **도구 실패:** WebFetch `kpmg.com` DNS 차단. 대신 govinfo.gov의 관보 원문 PDF를 curl로 받았다.

---

## 1. 숫자 검증

### 1-1. 원문과 다르거나 틀린 수치

| # | 리포트 | 앞 리포트의 수치 | 원문 확인 결과 | 영향 |
|---|---|---|---|---|
| N1 | 01 §2-1, 02 전체, 03 §2-1 | FY2025 순이익 ≈NT$1,717.9B, 희석 EPS **66.25**를 "회사 기준"으로 채택. 같은 수치를 보고한 Yahoo(1,697,604 / 65.47)는 "불일치"로 처리함 | **20-F FY25 감사 재무제표(IFRS, IASB 기준):** 지배주주 순이익 **NT$1,697,604M**, 희석 EPS **NT$65.47** (20-F FY25 F-8, MD&A "Net income attributable to shareholders of the parent 1,697,604"). 66.25와 505.74B(4Q25)는 6-K 보도자료 값이며, 보도자료에 "prepared in accordance with **TIFRS**"(대만 IFRS)라고 명시돼 있다(6-K 4Q25, 2026-01-15). 두 값의 차이 20,279M은 미처분이익 유보세(surtax) 인식 시점 차이로 설명된다. 20-F는 유보세를 "이익이 발생한 해에 비용 처리"하며(20-F FY25 F-25), FY2025 유보세 64,394.7 − FY2024 44,131.1 = **20,263.6**으로 차이 금액과 거의 일치한다 [계산·추정] | 사원은 **감사받은 수치를 오류로 분류**했다. 01 ^d는 1Q25·2Q25 `[학습데이터]` 합산으로 1,717.9B를 "검증"했는데, 이는 TIFRS 분기 값을 더한 것이라 검증이 되지 않는다. IFRS 기준으로 바꾸면 4Q25 EPS ≈18.72, TTM EPS ≈**97.48**(98.26 아님), TTM PER **22.3배**, FY2025 ROE **35.4%**(35.8% 아님), FY25→27E EPS CAGR 51.1%다 [계산]. 성장기에는 TIFRS 순이익이 IFRS보다 체계적으로 높게 나온다(유보세 이연). FY2026에도 같은 방향의 차이가 생긴다 [추정] |
| N2 | 01 §2-1, 02 §1 | FY2025 CAPEX 1,282,597 (Yahoo), FCF 992,378 | 20-F FY25: "capital expenditures of NT$**1,272,411** million", OCF 2,274,976 → FCF **1,002,565** [계산] | FY2025 기준 역DCF 내포 성장률 18.0% → 17.8% [계산]. 영향은 작다. 다만 원문이 있는데도 Yahoo 값을 쓴 것은 01 데이터 규칙("회사 원문 우선") 위반이다 |
| N3 | 03 §5-3, 04 §3-3 | NT$ 1% 절상 시 **매출총이익률 약 0.4%p** 하락 (과장은 2차출처, 부장은 `[학습데이터]`). 부장은 이를 근거로 "4Q26 GM 상방 약 +1.4%p"라고 씀 | 20-F FY25 원문: "every 1% depreciation of the U.S. dollar against the NT dollar would result in an approximately **0.3 percentage point decrease in our operating margin** based on our 2025 results" | 지표(GM이 아니라 OPM)와 크기(0.3%p)가 모두 다르다. 3.5% 환율 괴리에 적용하면 OPM 약 +1.0%p다(+1.4%p 아님) [계산]. 회사가 공식 수치를 공시하고 있으므로 2차·학습데이터 수치를 쓸 이유가 없다 |
| N4 | 03 §5-7, §4 | Section 232 "1단계(**2026-02**): 일부 로직 칩 HS 코드에 25%. 대만 기업은 미국 증설 계획 물량의 **2.5배**(완공 시 1.5배)까지 **면세 쿼터(2026-01-15 발효)**" | **Proclamation 11002**는 2026-01-14 서명, **2026-01-15 발효**다(관보 2026-01-20). 대상은 HS 코드 일반이 아니라 "certain advanced computing chips and certain derivative products"로, 연방관보 원문은 Annex의 성능 기준으로 범위를 정한다. 웹검색 요약(EY·KPMG 등)으로는 NVIDIA H200·AMD MI325X가 예시로 언급됐다(백악관 팩트시트 인용) [2차출처]. 해당 품목은 TSMC 생산품이다. 미국 데이터센터·R&D·스타트업·민간 소비자 용도 등은 면제다(관보 원문 clause 3). **2.5배/1.5배 쿼터는 관보와 20-F 어디에도 없다.** 20-F FY25(2026-04-16 접수)는 대만 합의가 "preferential Section 232 treatment"를 준다고 쓰면서도 "details regarding … the preferential treatment with respect to Section 232 tariffs, **including any offsets, are still unclear**"라고 적었다. 관보는 오프셋 프로그램을 "may consider imposing **significant tariffs** … as well as an accompanying tariff offset program"이라는 **장래 조치**로 서술한다 | 과장의 "쿼터 면세 구조"(논리 3의 전제)는 **원문으로 뒷받침되지 않는다.** 판정: **일부 틀림.** 날짜가 틀렸고, 쿼터가 "발효"됐다는 근거가 없으며, 오프셋은 아직 미정이다 |
| N5 | 03 §5-7, 04 §6 | 관세 리스크를 232조 하나로만 서술 | 20-F FY25에는 리포트에 없는 사실이 세 가지 더 있다. ① 2026-02 미 대법원이 IEEPA 상호관세를 위법으로 판결했다. ② 그 후 Trade Act **Section 122** 대체 관세가 부과됐다. ③ 2026-03 USTR이 **Section 301 조사 2건**(과잉생산, 강제노동)을 개시했고 그 대상에 **대만이 포함**됐다("targeting various economies, including Taiwan, which could result in … additional tariffs") | 대만을 겨냥한 301조 조사가 진행 중인데 과장의 촉매표·Kill criteria에는 빠져 있다 |
| N6 | 03 §1-5 | 2위 고객(보도상 Apple) FY2024 비중 "22%~24%, 출처마다 다름" | 20-F FY25: 최대 고객 비중 2023/2024/2025 = **25% / 22% / 19%**, 2위 고객 = **11% / 12% / 17%**, 상위 10개 = 70% / 76% / 78% | 원문 값이 있다(22%). "출처마다 다름"은 원문을 확인하지 않은 결과다. 또 매출채권의 **84%**(FY2024 93%)가 상위 10개 고객에게 몰려 있는데(20-F FY25 신용위험 주석) 어느 리포트도 이를 언급하지 않았다 |
| N7 | 01 §10, 03 §5-5 | 20-F Risk Factors "데이터 없음" | 원문을 확보했다. 6절 Q3과 1-3절에 반영 | — |
| N8 | 02 §3-1 | 베타 1.233 (yfinance info) | 부장이 주간 수익률로 회귀한 값은 2024-11~2026-11 1.56, 2026년 1.48이다(04 §2) | 대리의 자기자본비용은 부장 자체 추정보다 낮은 베타를 쓴다. 1-2절 할인율 재계산에 포함 |
| N9 | 04 §6-A | 대만 무역합의 "2026-02-12 상호무역협정" | 20-F FY25는 "in **January 2026**, the U.S. announced it had reached a trade and investment agreement with Taiwan"이라고 쓴다 | 발표일과 서명일의 차이일 수 있다. 조정되지 않은 채 남아 있음 |
| N10 | 01 §11, 03 §4, 04 §6-D | 2026-11-17 "미 상무부 파운드리 신규 규정" | 차장이 웹검색을 1회 더 했으나 실체를 확인하지 못했다. 확인된 것은 2026-08 상원의원들이 BIS에 Foundry Due Diligence Rule 존속 명확화를 요구한 서한(2차출처)뿐이다 | **사실로 쓰지 않는다.** 아래 논증에도 쓰지 않았다 |

### 1-2. 할인율 불일치 재계산 (오케스트레이터 공격 포인트 1)

대리 WACC는 9.0%(NT$)이고 부장 제안은 US$ 자기자본비용 11.6%(범위 10.6~13.6%)다. 대리의 DCF 코드(02 부록 B-2)를 그대로 재현하고 할인율만 바꿨다. 매출·마진·CAPEX 경로와 순현금은 대리 가정 그대로다 [계산, 부록 A].

TWD 환산은 부장 방식을 따랐다. 기대 인플레 차이(미국 BEI 2.21% vs CBC 2027 CPI 전망 1.83%)를 Fisher 식으로 적용하면 (1+r_USD)×1.0183/1.0221−1이다.
- 부장 기본값 11.6% → **11.19%**
- 부장 범위 10.6% / 13.6% → **10.19% / 13.18%**
- 대리 자신의 USD CAPM 11.67% → 11.25%

| 할인율 | 약세 | **기본** | 강세 | 확률가중 25/50/25 | 안전마진 기본 (2330) | 안전마진 기본 (ADR) | ADR 환산 기본 | 터미널 비중 |
|---|---|---|---|---|---|---|---|---|
| 대리 9.0% | 1,098 | **2,336** | 3,847 | 2,404 | +6.9% | −1.5% | US$354.5 | 60.5% |
| 부장 하단 (TWD 10.2%) | 952 | **1,948** | 3,124 | 1,993 | **−11.7%** | −21.7% | US$295.6 | 54.7% |
| **부장 기본 (TWD 11.2%)** | 860 | **1,712** | 2,697 | 1,745 | **−27.0%** | **−38.4%** | **US$259.8** | 50.3% |
| 부장 기본 USD 11.6% (환산 없이) | 829 | 1,634 | 2,556 | 1,663 | −33.1% | −45.1% | US$247.9 | 48.7% |
| 부장 상단 (TWD 13.2%) | 726 | **1,382** | 2,113 | 1,401 | −57.3% | −71.5% | US$209.8 | 42.6% |

(NT$/주. 안전마진 = (V−P)/V. ADR은 NT$2,370.1 상당과 비교) [계산]

**왜 9.0%가 가장 낙관적인 가정인가:**
1. 대리 식 ①은 USD 자기자본비용 11.67%에서 **미·대 금리차 3.22%p**를 빼서 TWD 8.45%를 만들었다. 이 환산이 성립하려면 NT$ 현금흐름에 **금리평가가 내포하는 TWD 절상**이 들어 있어야 한다. 그 경로를 그대로 적용하면 USD/TWD는 10년 후 약 **24.1**이 된다(32.947×(1.019/1.0512)^10) [계산]. 그런데 대리 모델은 환율을 사실상 고정해 두고(FY2026 CAPEX를 32.947로 환산, 성장률은 환율 중립) 할인율만 TWD로 낮췄다. 낮은 TWD 할인율과 USD 성격의 성장률을 섞은 것이다.
2. 20-F FY25에 따르면 "substantially all of our sales are denominated in U.S. dollars"이고, 2025년 평균 환율 32.13 → 31.11의 TWD 절상이 매출에 불리하게 작용했다고 회사가 직접 밝혔다. TWD 절상은 TSMC의 NT$ 현금흐름을 줄이는 **실제 경험된 경로**다.
3. 할인율을 어느 쪽으로 맞추든 결과는 같다. 부장의 TWD 환산 11.2%를 쓰면 **기본 가치 NT$1,712, 2330 안전마진 −27%, ADR −38%**가 된다. 강세 시나리오조차 13.2%에서는 현재가 아래(NT$2,113)다.
4. 확률가중 가치 1,745(11.2%)에서는 25/50/25 가중치를 어떻게 잡아도 현재가를 정당화하기 어렵다. 약세와 기본의 확률을 같게 둘 때 현재가를 맞추려면 **강세 확률이 63%**여야 한다 [계산].

### 1-3. 기타 수치 지적
- 02 §6-1 "PER 22.1배"와 03의 ROE 계산은 TIFRS 이익 기준이다. 감사 IFRS 기준으로 계산하면 PER은 22.3배다(N1).
- 03 §2-1 "3Q26 연환산 ROE 45.5%"는 사상 최고 분기를 4배 한 값이다. 감사받은 연간 ROE(IFRS)는 35.4%다 [계산].

---

## 2. 논리 반박

### 논리 1 반박 — "AI 수요가 가이던스보다 빠르게 매출로 확인된다"

1. **성장의 절반이 가격·믹스다.** 20-F FY25에 따르면 웨이퍼 출하량은 12,910K → 15,022K로 **+16.4%**, 웨이퍼당 매출은 **+13.1%**였다. 매출 +31.6%의 약 절반이 가격·믹스에서 나왔다 [계산]. 회사도 FY2025 성장 요인을 "increase in ASP due to a higher proportion of advanced technology"로 1순위에 놓았다. 다운사이클에서 가장 먼저 되돌려지는 것이 가격·믹스다. FY2023에 매출은 −4.5%(NT$), EPS는 −14.2%였다(SEC XBRL, 04 §3-2).
2. **공급이 따라잡는 중이다.** 20-F FY25 연간 생산능력은 ">17 million"(2024년 "approximately 17 million")이었다. 2026년 CAPEX는 US$60~64B인데 1~9월에 이미 US$40.64B를 썼다. 이는 FY2025 연간 CAPEX US$40.90B와 같은 수준이다(01 §6-1). 과장이 인용한 TrendForce 보도도 CoWoS 수급 부족률이 20%에서 10%로 줄어든다고 본다. 공급 부족이 해소되면 가격 결정력의 근거가 약해진다.
3. **회사 자체 장기 가이던스는 급감속을 뜻한다.** 과장 자신의 계산이 그렇다. 전사 2024~29 CAGR "approach 25%"를 그대로 적용하면 2026~29 암시 CAGR은 **약 16%**다(03 §3). 과장은 이를 "가이던스가 실적에 뒤처졌다"며 상방 촉매로 읽었다. 그러나 이 숫자는 회사가 공식 제시한 **유일한** 장기 숫자이고, 44%에서 16%로의 감속을 함축한다.
4. **수요 측 경고:**
   - MSFT 2026 역년 CAPEX가 약 US$190B에서 약 US$170B로 하향됐다(04 §4-1, 2차출처).
   - SOX는 2026-06 고점 대비 −34.1%, NVDA는 9월 말 228.4에서 155.5로 떨어졌다(04 §4-1, yfinance).
   - AI 회의론의 핵심 논거는 다음과 같다. 하이퍼스케일러 CAPEX가 현금흐름을 앞서 부채 조달이 늘고 있다. GPU 내용연수 가정이 이익을 부풀린다(Burry 주장 보도). 1990년대 말 통신 버블과 닮았다는 지적이 있다(Advisor Perspectives "AI Bear Case: What Skeptics Get Right And Wrong", 2026-08-03, https://www.advisorperspectives.com/commentaries/2026/08/03/ai-bear-case-skeptics-right-wrong ; Futuriom "Hyperscaler AI Spending Doubts Rising", 2026-04, https://www.futuriom.com/articles/news/ctp-is-hyperscaler-ai-spending-sustainable/2026/04) [2차출처, 의견 기사].
5. **고객 집중이 커지고 있다.** 상위 10개 고객 비중은 70% → 76% → 78%, 상위 2개는 36%다. 매출채권의 84%가 상위 10개 고객에 몰려 있다(20-F FY25). 20-F는 FY24부터 "growth … particularly in the AI sector, is volatile or not sustainable"이면 매출이 크게 흔들릴 수 있다고 명시해 왔다. FY25에는 "customers have accelerated the cadence of introducing new products … If we are unable to meet these shorter product time-to-market, we risk losing these customers"가 **새로 추가**됐다(20-F FY24 대비 diff, 1절 방법론은 부록 B).
6. **Kill criteria가 후행적이다.** "FY2027 USD 매출 가이던스 +20% 미만"은 컨센서스 FY2027 +37.8%(NT$ 7,691B/5,582B)의 절반 수준이다. 이 조건이 발동할 때쯤이면 주가는 이미 2022년처럼 먼저 조정을 받았을 것이다. 부장은 2022년 주가 바닥이 실적 바닥보다 2~3분기 앞섰다고 정리했다(04 §3-2).

### 논리 2 반박 — "해자가 점유율·마진으로 확대 중 (GM 66%)"

1. **GM 66%는 사이클 고점이다.** 20-F FY25가 설명하는 FY2025 GM 상승 요인은 "higher capacity utilization and cost improvement"다. 가동률은 경기순환 변수다. 연간 GM은 FY2023 54.4%, FY2024 56.1%였다(20-F FY25). 3Q26 GM 66.4%는 FY2023보다 12%p 높다.
2. **감가상각 파도가 온다.** 20-F FY25 기준 기계장치 내용연수는 **5년**이다. FY2026E CAPEX NT$2.01T(대리 추정)는 TTM 감가상각 NT$746B(02 부록 A)의 **2.7배**다 [계산]. 장비 NT$1T가 추가될 때마다 연간 감가상각이 약 NT$200B 늘고, 이는 FY2026E 매출의 약 3.6%p에 해당한다 [추정]. 여기에 해외 팹 희석 3~4%p(회사 가이던스, 2차출처)와 N2 초기 희석이 겹친다.
3. **해외 팹 마진은 보조금이 받쳐 준다.** 20-F FY25 회계정책상 유형자산 관련 정부보조금은 **자산 장부가에서 차감**되어 감가상각을 줄인다. 현금 수령액은 NT$47.5B(2023) → 75.2B(2024) → **76.3B(2025)**다(20-F 현금흐름표). 보조금에는 "conditions, compliance requirements … project milestone requirements"가 붙어 있다. TSMC 본사는 애리조나 법인의 미 상무부 채무를 **무조건 보증**한다(20-F FY25 Item 4). 보조금의 "clawback"은 Risk Factors에도 명시돼 있다.
4. **경쟁 신호:**
   - Intel은 2026-07 "14A 2028 HVM 램프에 전면 커밋"했다. 2026-09 CFO는 외부 고객 확보에 "conviction"이 있다고 말했다(Tom's Hardware, https://www.tomshardware.com/tech-industry/semiconductors/intel-says-it-has-two-prospective-customers-for-14a-expects-to-hear-about-commitments-in-second-half-of-2026 ; bits-chips https://bits-chips.com/article/intel-signals-external-customer-wins-for-14a-foundry-process/) [2차출처].
   - Seeking Alpha 필자 한 명은 "Intel Just Got A Second Life"를 이유로 TSMC 등급을 내렸다(https://seekingalpha.com/article/4851078-tsmc-wide-moat-remains-intel-just-got-second-life-rating-downgrade) [2차출처, 개인 의견].
   - 확정 고객이 아직 없다는 점은 사실이다. 그러나 Kill ③("공식 발표")이 발동하면 이미 2~3년 뒤 물량의 이탈이 확정된 시점이다.
5. **해자의 정치화는 원문에 적혀 있다.** Proclamation 11002의 목적 조항은 "reduce our Nation's reliance on foreign sources and foreign supply chains"이고, 대만산 첨단 칩 수입 의존 축소를 명시한다. 정책 목표 자체가 TSMC 대만 생산의 상대적 가치를 낮추는 쪽이다.
6. **2027년 단가 인상은 확인되지 않았다.** 과장 자료에서도 TSMC는 확인을 거부했다. 확인되지 않은 인상으로 해외 팹 희석을 "상쇄할 것"이라는 [추정]이 논리 2의 지지대다.

### 논리 3 반박 — "현금창출력 충분, 지정학·관세는 숫자로 미실현"

1. **FCF/순이익이 떨어지고 있다.** FY2025는 0.59다(20-F: FCF 1,002,565 / 순이익 1,697,604). TTM은 0.57이다. FY2026E는 대리 FCF NT$1,423,669M를 컨센서스 순이익(EPS 110.63×25,932M주 ≈ NT$2,869B)으로 나누면 **0.50**이다 [계산]. 회사는 2026~28년 CAPEX가 "직전 3년보다 유의미하게 높을 것"이라고 했다. 이익이 늘어나도 주주가 쓸 수 있는 현금의 비율은 줄어든다.
2. **"관세는 대만 쿼터 면세 구조"는 원문과 맞지 않는다(N4, N5).** 확인된 사실은 다음과 같다.
   - 25% 관세가 이미 발효됐고, 대상이 바로 TSMC가 만드는 AI 칩이다.
   - 2단계 "significant tariffs"가 예고돼 있다.
   - 대만 우대의 세부는 "still unclear"다.
   - 대만을 겨냥한 301조 조사가 진행 중이다.
   - 이 상태에서 "미실현"은 "아직 미확정"이라는 뜻일 뿐, 리스크가 없다는 근거가 되지 못한다.
3. **수출통제 위반 리스크가 미해결이다.**
   - 20-F FY25: "In October 2024, we notified relevant U.S. and Taiwan authorities that one type of our customer's chip manufactured by us might have been diverted to a restricted entity … and since then have been cooperating". 1년 반이 지나도록 결론이 나지 않았다.
   - Reuters는 2025-04에 이 건(Sophgo–Huawei Ascend 910B)으로 **US$1B 이상의 벌금** 가능성을 보도했다(Business Today 인용 https://www.businesstoday.in/amp/technology/news/story/tsmc-could-face-over-1-billion-fine-in-us-export-control-probe-linked-to-huawei-reuters-471343-2025-04-09) [2차출처]. 최종 결과는 데이터 없음.
   - FY25에 새로 들어간 문구: "export controls … often depend on the products' specific features or performance characteristics that **foundries may not be able to verify independently** … we could be found in violation". 회사가 스스로 구조적 위반 가능성을 인정한 것이다.
4. **중국 팹은 1년짜리 라이선스에 의존한다.** 20-F FY25에 따르면 난징 VEU는 2025-12에 만료됐고 연간 수출 라이선스로 대체됐다("no assurance that this annual export license will not be terminated"). 과장이 인용한 중국 법인 이익 NT$39.2B(2차출처)가 이 라이선스에 걸려 있다.
5. **대만 정부의 생산능력 사용권이 있다.** 20-F FY25 주석 36에 따르면, ITRI 기술협력 계약상 "the R.O.C. Government or its designee … can use **up to 35% of TSMC's capacity**"이고, 계약은 5년 단위로 자동 갱신된다. 아직 행사된 적은 없다. 그러나 유사시에 주주가 아닌 국가가 생산능력의 일부를 쓸 수 있는 조항이다. 01~04 어디에도 이 내용이 없다.
6. **ADR 보유자의 실수령 배당**은 대만 원천징수로 약 21% 줄어든다(03 §5-2, 2차출처). "배당 1.66%"는 ADR 보유자에게 약 1.3%다 [계산].

---

## 3. 밸류에이션 공격

### 3-1. 대리 가정 중 가장 낙관적인 것: 할인율 9.0%
1-2절 참조. 일관된 할인율(TWD 11.2%)에서는 기본 가치 **NT$1,712 / ADR US$259.8**, 안전마진 **−27% / −38%**다. 대리 자신도 WACC를 가장 근거가 약한 가정으로 꼽았다(02 §5-3).

### 3-2. 두 번째로 낙관적인 가정: 터미널 FCF 마진, 그리고 "약세"가 약세가 아니다

| 항목 | 값 | 비교 |
|---|---|---|
| 기본 터미널 FCF 마진 | 28% | FY2021~25 평균 22.0%. 5년 중 이를 넘은 해는 FY2024(30.1%) 한 번뿐 [계산, 02 §1] |
| **약세** 터미널 FCF 마진 | **24%** | 과거 5년 평균(22.0%)**보다 높다** |
| 약세 매출 경로 | FY27 +15%, 역성장은 2029년 −5% 한 해뿐 | 실제 다운사이클: FY2023 −4.5%(NT$). 2001년 및 2009년 역성장 `[학습데이터, 최신 아님]` |
| 확률 25/50/25 | 근거 없음 (02에 `[추정]`) | 9.0% WACC에서도 기본 비중을 50%로 두고 약세 확률을 **33%**로만 올리면 확률가중 가치가 현재가와 같아진다 [계산] |

정리하면 대리의 "약세"는 실제로는 "기본보다 덜 좋은" 시나리오다. 과거 실적 수준의 마진을 가정하는 진짜 약세 시나리오가 없다.

### 3-3. 역DCF가 요구하는 성장률은 역사적으로 얼마나 드문가

**참조 집단.** Mauboussin, *The Base Rate Book* (Credit Suisse, 2016-09-26), Exhibit 4와 부록 관측치를 썼다. 기간은 1950~2015, 대상은 매출 US$50B 초과 기업이며 **인플레 조정 실질 매출 CAGR** 기준이다. 원문 PDF: https://josephnoko.com/wp-content/uploads/2024/04/The-Base-Rate-Book-Michael-Mauboussin.pdf . TSMC의 FY2026E 매출은 약 US$175B로 이 집단에 속한다.

| 10년 실질 CAGR | 관측치 (총 1,099) | 비율 |
|---|---|---|
| 10~15% | 33 | 3.0% |
| 15~20% | 10 | 0.9% |
| 20% 이상 | 0 | **0.0%** |
| **10% 이상 합계** | 43 | **3.9%** |

| 현재가가 요구하는 것 | 명목 | 실질 근사 (대만 CPI 약 1.8~2.0% 차감) | 매출 US$50B 초과 기업 중 달성 비율 |
|---|---|---|---|
| 대리 WACC 9.0%, 2330 | FCF CAGR 12.9% | ≈11% | **3.9% 이하** |
| 대리 WACC 9.0%, ADR | 14.0% | ≈12% | 3.9% 이하 |
| **일관 할인율 11.2%, 2330** | **17.8%** [계산] | ≈16% | **0.9% 이하** |
| 일관 할인율 11.2%, ADR | 19.1% [계산] | ≈17% | 0.9% 이하 |
| 기본 마진 경로 매출 CAGR (11.2%) | 15.4% / 16.6% (2330/ADR) | ≈13.5~14.5% | 약 3% 이하 |

- **주의:** 이 표는 매출 기준이고 FCF 기준이 아니다. FCF는 마진이 오르면 매출보다 빨리 클 수 있다. 그러나 TSMC의 TTM FCF 마진 29.5%는 이미 과거 최고치(FY2024 30.1%) 근처라서 마진 확장 여지가 작다. 또한 표본에는 생존자 편향이 있어 성장률이 오히려 과대평가되는 쪽이다.
- **절대 규모로 보면:**
  - 12.9% FCF CAGR이 10년 이어지면 FY2036 FCF는 약 **US$149B**다 [계산].
  - 대리 기본 시나리오의 FY2036 매출은 **US$526B**로, WSTS 2026년 전 세계 반도체 시장 추정 US$1.51T(04 §4-1)의 **약 35%**다 [계산]. 게다가 그 2026년 시장 규모에는 메모리 가격 급등 효과가 들어 있다(04).
- **외부 "공정가치" 추정도 사이클을 따라 움직인다.** Morningstar의 TSM 공정가치는 2025-04 US$262에서 2026-10 US$534로 18개월 만에 두 배 넘게 올랐다(Stocktwits 2026-10-16 보도, https://stocktwits.com/news-articles/markets/equity/tsmc-s-leave-no-food-on-the-table-pledge-signals-more-ai-chip-investment/cZxKGj2RBsa ; morningstar.ca https://morningstar.ca/ca/news/250638/tsmc-fair-value-raised-45-on-ai-demand.aspx) [2차출처]. Simply Wall St DCF는 TSM이 공정가치보다 약 13% 높다고 봤다(https://www.webull.com/news/15625565074375680) [2차출처]. 셀사이드 매도 의견은 찾지 못했다. 가장 비관적인 목표가도 US$430이었다(Yahoo 집계 기사, 날짜 혼재) [2차출처]. 매수 쏠림 자체가 반대 신호다 [추정].

---

## 4. 회계 위험 신호

| 신호 | 확인 결과 | 출처 | 판정 |
|---|---|---|---|
| **재고 증가율 > 매출원가 증가율** | 3Q26 재고 YoY **+48.2%** vs 매출원가 **+25.0%** (매출 +50.9%). DIO 65.5일(3Q25) → 74.0 → **85.6(2Q26)** → 77.6(3Q26). 회사 재고 구성(FY2025)은 WIP 188.0B / 288.1B = **65%**. 재고평가손실은 NT$888.7M(2024) → **2,125.9M(2025, +139%)** | 분기: yfinance 2330.TW quarterly [계산]. 구성·평가손: 20-F FY25 주석 13 | **경계.** 재고는 원가로 기록되므로 매출원가와 비교해야 맞다. 이렇게 보면 재고가 원가의 약 2배 속도로 쌓이고 있다. N2 램프의 WIP로 설명될 수도 있지만 회사의 분기 구성 공시는 데이터 없음 |
| **매출채권 증가율 > 매출 증가율** | 3Q26 YoY 채권 **+57.1%** vs 매출 +50.9%. DSO 28.3일 → 31.7(2Q26) → 29.4(3Q26). 연간(FY2025)으로는 채권 +3.6% vs 매출 +31.6% | yfinance "Receivables" [계산]. 20-F FY25 재무상태표 | 약한 경계. 상위 10개 고객이 채권의 84%를 차지한다 |
| **FCF < 순이익 지속** | FCF/순이익: FY2021 0.46, FY2022 0.53, FY2023 0.34, FY2024 0.75, FY2025 **0.59**(20-F), TTM 0.57, FY2026E **0.50** [계산] | 02 §1, 20-F FY25 | **구조적.** 5년 연속 1 미만이고 2026년에 더 낮아진다. PER(22.3배)과 FCF 수익률(2.58%) 사이 괴리의 원천이다 |
| **잦은 일회성 비용** | 지진 손실(보험 회수 후): 2Q24 약 NT$3B, 1Q25 **NT$5.3B**. 재고평가손실 증가 | 20-F FY25 Risk Factors | 규모는 작다(FY2025 매출의 0.14%). 다만 자연재해 비용이 2년 연속 발생했다 |
| **감사인 변경** | Deloitte & Touche, 1987년부터 감사. 변경 없음 | 20-F FY25 감사보고서 | 신호 없음 |
| **특수관계자 거래** | 관계기업(GUC·VIS·SSMC·Xintec) 매출 15,034.1M(2024) → **33,226.4M(2025, +121%)**, 매출 증가율의 약 4배. 특수관계자 채권 1,404.5M → 2,739.5M(+95%). 거래 조건은 "not significantly different". 관계기업 매출은 전체의 0.87% | 20-F FY25 주석 34 | 규모는 작지만 증가 속도가 이례적이다. VIS는 TSMC 관계기업으로, 이 성장의 내역은 데이터 없음 |
| 핵심 경영진 단기 보상 | NT$4,447.5M → **8,006.8M (+80%)**. 순이익 증가율은 +46.5% | 20-F FY25 주석 34-h | 보상이 이익보다 빨리 늘었다 |
| 기타유동자산 급증 | NT$43.2B → **118.7B (+174%)**(FY2025). 1H26 136~140B, 3Q26 78.6B | 20-F FY25 재무상태표; yfinance | 구성 데이터 없음. 이사회 확인 필요 |
| 이익 기준 혼용 | 분기 보도자료는 TIFRS, 20-F는 IFRS(IASB)다. 성장기에는 TIFRS 순이익이 더 높게 나온다(유보세 인식 시점). FY2025 차이 NT$20.3B | N1 | 팀 전체가 감사받지 않은 TIFRS 수치를 "회사 기준"으로 썼다 |
| 정부보조금 장부가 차감 | 유형자산 보조금 수령액 2023~25 NT$47.5B / 75.2B / 76.3B가 자산에서 차감돼 감가상각을 줄인다. 조건 미충족 시 환수 위험이 있고 본사가 보증한다 | 20-F FY25 회계정책, 현금흐름표, Item 4 | 해외 팹 GM이 보조금에 기대고 있다 |

---

## 5. 프리모템: "2027-11, TSM이 −40%가 됐다. 왜?"

- **−40% 기준선:** 2330은 NT$1,305, ADR은 **US$215.8**.
- **역사적 기준률 [계산, yfinance 수정주가 월말]:**
  - TSM(1997~): 24개월 뒤 총수익률 −40% 이하인 달이 전체의 **4.0%**, 24개월 안에 한 번이라도 −40%에 닿은 달이 **15.6%**다. 해당 구간은 1998, 2000~02, 2022년이다.
  - 2330(2000~): 각각 0.3%, 5.0%다.
- **출발점:** TSM은 이미 52주 고점 US$485.80에서 −26.0% 내려와 있다 [계산].

### 시나리오 1 — AI CAPEX 소화기 + 2022형 멀티플 압축 (확률 **약 10%** [추정])
- **경로:**
  - 2027년 하반기에 하이퍼스케일러의 2028 CAPEX 가이던스가 증가율 10% 미만으로 나온다.
  - CoWoS·N3 공급 부족이 해소되면서 가격·믹스가 되돌려진다. FY2025 성장의 약 절반이 가격·믹스였다(2절).
  - 가동률이 떨어지고, US$60B대 CAPEX의 감가상각이 겹쳐 GM이 FY2023 수준(54~56%)으로 되돌아간다.
  - FY2028 EPS는 약 NT$120으로 FY2027E 149.5 대비 −20%다. 비교 사례는 FY2023 −14.2%다.
  - PER은 11~12배(2022년 말 11.7배)로 내려간다.
- **결과 [계산]:** 2330은 NT$1,320~1,440으로 **−34%~−39%**다. ADR 프리미엄이 9%에서 0으로 줄면 ADR은 US$200~219로 **−39%~−44%**다.
- **근거:**
  - SOX −34%, MSFT CAPEX 하향, DRAM 가격 상승률 둔화, DIO 85.6일 (모두 04).
  - 회사 장기 가이던스가 암시하는 2026~29 CAGR 약 16%(03).
  - 2022년 사례: EPS +67.6%였는데도 TSM은 −57%였다(04 §3-1).
- **확률 근거:** 사이클 후기라는 판단(04)은 이 시나리오를 기준률(4.0%)보다 높게 볼 이유가 된다. 그러나 3Q26 실적과 4Q26 가이던스(YoY +58%)가 아직 꺾이지 않았다. 2년 안에 실적이 −20% 수준까지 떨어지려면 2027년 하반기 전환이 필요하다.

### 시나리오 2 — 무역·지정학 체제 충격으로 할인율 재설정 (확률 **약 5%** [추정])
- **경로:**
  - Proclamation 11002가 예고한 2단계 "significant tariffs"가 시행되는데, 대만 우대(20-F상 "still unclear")가 쿼터 없이 확정되거나 축소된다.
  - Section 301 조사(대만 포함)가 추가 관세로 이어진다.
  - 수출통제 위반 건(2024-10 통보)이 벌금으로 확정된다.
  - 양안 군사훈련·검역형 봉쇄 같은 헤드라인이 반복된다.
  - 외국인 이탈이 계속된다. 외국인 지분율은 이미 73.8%에서 69.2%로 낮아졌고, 2026-11 누적 약 US$10B가 유출됐다(04 §5).
  - 실적은 유지되지만 시장 할인율이 부장 상단(TWD 13.2%)으로 오른다.
- **결과 [계산]:** 대리 기본 시나리오의 현금흐름을 그대로 둬도 가치는 **NT$1,382(−36%)**다. ADR 프리미엄까지 소멸하면 ADR은 US$209.7(**−42%**)이다.
- **근거:**
  - 20-F FY25에 새로 들어간 관세 단락: IEEPA 위헌 판결, 122조, 301조 대만 포함, 232조 25% 관세.
  - 관보 원문의 2단계 예고.
  - 1-2절 민감도.
  - 2022-08 대만해협 긴장기 `[학습데이터, 최신 아님]`.
- **확률 근거:** 2단계 관세 일정은 미정이고, 대만 합의가 우대를 약속한 상태다. 이 시나리오에는 여러 사건이 함께 일어나야 한다.

### 시나리오 3 — 마진·자본집약도 함정 (매출은 컨센서스 달성, 주주 현금은 정체) (확률 **약 5%** [추정])
- **경로:**
  - 매출은 컨센서스 근처를 유지한다.
  - GM은 66%에서 약 57%로 떨어진다. 해외 팹 희석 3~4%p, 감가상각 파도 약 3%p, TWD 강세 반전이 원인이다. USD/TWD가 32.9에서 2025-06 수준인 29.2로 가면 약 −11%이고, 20-F 경험칙 0.3%p/1%를 적용하면 OPM 약 −3.4%p다 [계산].
  - CAPEX가 매출의 40%를 넘으면서 FCF가 3년간 약 NT$1.4T에서 정체한다.
  - 시장이 PER 대신 FCF 수익률로 가격을 매기기 시작한다. FCF 수익률이 2.58%에서 4.5~5%로 오른다. 이는 일관 할인율 11.2%와 성장 둔화를 조합한 수준이다 [추정].
- **결과 [계산·추정]:** FY2028 EPS 약 NT$135 × PER 10~11배 = NT$1,350~1,485로 **−32%~−38%**다. ADR 프리미엄이 소멸하면 **−37%~−43%**다.
- **근거:**
  - FY2026E FCF/순이익 0.50(4절).
  - CAPEX/D&A 2.7배, 내용연수 5년(20-F).
  - 2026~28 CAPEX가 "유의미하게 높을 것"이라는 회사 언급.
  - 20-F의 환율 민감도.
- **확률 근거:** 이 시나리오 하나만으로는 −20~−30%에 머물 가능성이 크다. −40%에 이르려면 금리 상승(미 실질금리 2.92%, 04)이 겹쳐야 한다.

**종합:** 세 시나리오는 서로 겹친다(시나리오 1과 3은 같은 사이클 신호를 공유한다). 2년 안에 −40%로 끝날 확률은 약 **15%** [추정]이다. 이는 TSM의 무조건부 기준률(24개월 종점 4.0%)의 약 4배다. 근거는 다음과 같다. ① 할인율을 일관되게 맞추면 기본 가치가 이미 현재가 아래다. ② 사이클 후기 신호가 있다. ③ 원문으로 확인된 관세·수출통제 리스크가 리포트들에서 과소평가됐다.

---

## 6. 최종

### 매도 논리 강도: **중** (ADR 매수에 한정하면 **강**)

- **강한 부분 (숫자로 확인됨):**
  - 할인율을 일관되게 맞추면(TWD 11.2%) 대리 자신의 현금흐름 가정으로도 기본 가치는 NT$1,712 / US$259.8, 안전마진은 **−27% / −38%**다.
  - 현재가는 매출 US$50B 초과 기업 가운데 **3.9%(대리 할인율) 또는 0.9% 이하(일관 할인율)**만 달성한 10년 성장률을 요구한다.
  - 과장의 관세 전제("쿼터 면세")는 20-F 원문과 관보로 뒷받침되지 않는다.
  - 팀이 쓴 이익 수치는 감사받지 않은 TIFRS 기준이다.
- **약한 부분 (매도 논리의 한계):**
  - 실적 지표(10월 매출 +59.7%, 4Q26 가이던스 YoY +58%)는 아직 꺾이지 않았다.
  - 회계 신호(재고, 특수관계자)는 규모가 작거나 N2 램프로 설명될 여지가 있다.
  - 감사인 변경은 없다.
  - 숫자로 확인된 것은 "비싸다"이지 "실적이 무너진다"가 아니다. 그래서 전체 판정은 "강"이 아니라 "중"이다.

### 이사가 반드시 답해야 할 질문 3개

1. **할인율:** 대리의 NT$ 9.0%(대만 무위험 1.9% + 사실상 고정 환율)와 부장의 일관 환산 11.2% 중 어느 쪽을 채택하는가?
   - 9.0%를 쓴다면, 현금흐름에 금리평가상 TWD 절상(10년 후 USD/TWD 약 24.1)을 넣지 않은 불일치를 어떻게 정당화하는가?
   - 11.2%를 쓴다면 기본 가치는 NT$1,712 / ADR US$259.8이다. 그래도 투자 의견을 낼 근거가 남는가?
2. **성장 지속성:** 시가총액 US$1.7~1.9T 기업이 10년간 실질 약 11~16%의 FCF 성장을 이어 가야 한다. 이는 역사적 상위 3.9%~0.9%에 해당한다. 이를 넘어설 TSMC 고유의 근거는 무엇인가?
   - 그 근거가 가격·믹스 피크(FY2025 웨이퍼 +16.4% vs 매출 +31.6%)와 GM 66%라는 사이클 고점 데이터에서 나온 것이 아니라는 증거는 무엇인가?
   - 과거 평균 마진(FCF 22%)을 쓰는 진짜 약세 시나리오를 넣으면 확률가중 가치는 얼마인가?
3. **정책·법적 리스크의 정량화:** 20-F 원문에 따르면 다음 다섯 가지가 동시에 열려 있다.
   - 232조 25% 관세가 발효 중이고 그 대상이 TSMC 생산 AI 칩이다.
   - 대만 우대의 세부는 "still unclear"다.
   - 대만을 포함한 301조 조사가 진행 중이다.
   - 2024-10 전용(diversion) 통보 건이 미해결이고, 벌금 US$1B 이상 가능성이 보도됐다.
   - 난징 팹은 연간 라이선스에 의존한다.
   - 과장 논리 3의 "쿼터 면세" 전제 없이도 투자 논리가 유지되는가? 이 리스크들에 각각 어떤 확률과 손익을 부여하는가? 부장 권고대로 할인율이 아닌 시나리오 가중치로 반영한다면 그 가중치는 얼마인가?

---

## 부록 A. 재계산 코드 (rt.py, 대리 dcf.py를 재현하고 할인율만 변경)

```python
import numpy as np
def bis(f,a,b,tol=1e-10):
    fa=f(a)
    for _ in range(300):
        m=(a+b)/2; fm=f(m)
        if (fm>0)==(fa>0): a,fa=m,fm
        else: b=m
        if b-a<tol: break
    return (a+b)/2
SH=25932.36; PX=2175.0; MCAP=PX*SH; FX=32.947; ADR_PX=359.69
NETCASH=4094653-1065988
rev26=(5561.8e3+5625.4e3)/2; q4rev=rev26-3898727
q4capex=(19.36+23.36)/2*1e3*FX; q4ocf=q4rev*0.61; fcf_q4=q4ocf-q4capex
T0=0.12
def dcf(growth,ocfm,capexi,g,wacc,det=False,ocf_shift=0.0):
    rev=rev26; pv=fcf_q4/(1+wacc)**(T0/2); rows=[]
    for i,(gr,om,ci) in enumerate(zip(growth,ocfm,capexi)):
        rev*=1+gr; f=rev*(om+ocf_shift-ci); t=T0+i+0.5
        pv+=f/(1+wacc)**t; rows.append((2027+i,rev,f))
    tv=rows[-1][2]*(1+g)/(wacc-g); pvtv=tv/(1+wacc)**(T0+10)
    ev=pv+pvtv; ps=(ev+NETCASH)/SH
    return dict(ps=ps,tv=pvtv/ev,rows=rows) if det else ps
S={ # 02_valuation 4-1 가정 그대로
 "bear":dict(growth=[.15,.05,-.05,.08,.06,.06,.05,.05,.04,.04], ocfm=[.58,.55,.52,.52,.52,.52,.52,.52,.52,.52], capexi=[.34,.33,.30,.29,.28,.28,.28,.28,.28,.28], g=.02),
 "base":dict(growth=[.30,.20,.15,.12,.10,.09,.08,.07,.06,.05], ocfm=[.61,.60,.59,.58,.57,.56,.55,.55,.55,.55], capexi=[.34,.32,.30,.29,.28,.27,.27,.27,.27,.27], g=.03),
 "bull":dict(growth=[.38,.25,.20,.16,.14,.12,.10,.09,.08,.07], ocfm=[.63,.63,.62,.61,.60,.60,.59,.59,.59,.59], capexi=[.33,.31,.29,.27,.26,.25,.25,.25,.25,.25], g=.035)}
ADR_NT=ADR_PX/5*FX
fisher=lambda r:((1+r/100)*(1.0183/1.0221)-1)*100   # 미국 BEI 2.21% vs CBC 2027 CPI 1.83% (04_macro)
print(fisher(11.6), fisher(10.6), fisher(13.6), fisher(11.67))
for nm,w in [("9.0",.09),("10.2",.102),("11.2",.112),("11.6",.116),("13.2",.132)]:
    v={k:dcf(s["growth"],s["ocfm"],s["capexi"],s["g"],w) for k,s in S.items()}
    pw=.25*v["bear"]+.5*v["base"]+.25*v["bull"]
    print(nm, {k:round(x) for k,x in v.items()}, round(pw), (v["base"]-PX)/v["base"], (v["base"]-ADR_NT)/v["base"], v["base"]*5/FX)
def rev_fcf(base,g,w,tgt):
    def f(x):
        pv=0;c=base
        for i in range(10):
            c*=1+x; pv+=c/(1+w)**(T0+i+0.5)
        return pv+c*(1+g)/(w-g)/(1+w)**(T0+10)-tgt
    return bis(f,-0.5,1.0)
for w in [.09,.112]:
    print(w, rev_fcf(1457584,.03,w,MCAP-NETCASH), rev_fcf(1457584,.03,w,ADR_NT*SH-NETCASH), rev_fcf(2274976-1272411,.03,w,MCAP-NETCASH))
print("10y forward USD/TWD (IRP)", 32.947*(1.019/1.0512)**10)
```

부가 계산(동일 세션): 재고·채권 YoY와 DIO/DSO는 yfinance `2330.TW` quarterly balance sheet/income statement로 계산했다(분기 매출원가 3Q25 401,375.5 / 3Q26 501,864.6, NT$M). TSM 2년 낙폭 기준률은 yfinance `history(period='max', auto_adjust=True)` 월말 종가를 썼다.

## 부록 B. 20-F Risk Factors 전년 대비 diff 방법과 결과 (오케스트레이터 공격 포인트 6)

**방법.** 20-F FY24(HTML을 텍스트로 변환, Risk Factors 구간)과 20-F FY25(Risk Factors 구간)를 문장 단위로 나눴다. 연도 숫자는 정규화했다. FY25의 각 문장에 대해 FY24 문장들과의 단어 Jaccard 유사도 최댓값을 구하고, 0.45 미만인 문장을 "신규 또는 대폭 수정"으로 분류했다. FY24 268문장 중 FY25 281문장과 비교해 31문장이 해당됐다.

**실질적인 신규 항목:**
1. **관세 단락 전면 개편:** IEEPA 상호관세 위헌 판결(2026-02), Section 122 대체 관세, **Section 301 조사 2건(대만 포함, 2026-03)**, Section 232 결론(2025-12)과 **25% ad valorem 관세**, 2단계 확대 관세 예고와 오프셋 프로그램, 대만 합의(2026-01, 상호관세 15% 이하, 232조 우대)와 그 세부의 "still unclear".
2. **난징 팹:** VEU 만료(2025-12)와 연간 수출 라이선스 대체, 갱신 보장 없음.
3. **수출통제 검증 한계:** "foundries may not be able to verify independently" → 위반·조사·벌금 가능성. 2024-10 전용 통보 건은 FY24에도 있었고 FY25에도 "cooperating" 상태로 남아 있다.
4. **고객 측:** 제품 출시 주기 단축("accelerated the cadence"), 주요 고객 대상 수출통제가 수요에 미치는 영향.
5. **특허:** 미 특허청의 IPR(무효심판) 접근 제한 → NPE 소송 증가 가능성. 해외 확장에 따른 IP 유출 관리 문제.
6. **재해·인프라:** 핵심 설비·유틸리티(물·전기·가스) 장애 단락 확대, 고객 측 재해로 인한 수요 감소.
7. **거시:** "military conflicts"로 인한 공급망 교란·인플레·규제 불확실성 문장 추가(FY24 3회 → FY25 5회 언급).

**신규가 아닌 항목 (FY24에도 있음):** AI 성장의 "volatile or not sustainable" 문구, 대만 정부의 생산능력 35% 사용권(주석 36).

## 출처 (본 문서에서 새로 쓴 외부 출처)
- SEC 20-F FY2025 (accession 0001628280-26-025362), FY2024 (0001193125-25-083423), 6-K 4Q25 실적 (2026-01-15): 원문 `sources/` 저장본
- Federal Register Vol.91 No.12, Proclamation 11002 (2026-01-14): https://www.govinfo.gov/content/pkg/FR-2026-01-20/pdf/2026-01052.pdf
- Mauboussin, The Base Rate Book (2016): https://josephnoko.com/wp-content/uploads/2024/04/The-Base-Rate-Book-Michael-Mauboussin.pdf
- [Advisor Perspectives — AI Bear Case](https://www.advisorperspectives.com/commentaries/2026/08/03/ai-bear-case-skeptics-right-wrong) · [Futuriom — Hyperscaler AI Spending Doubts](https://www.futuriom.com/articles/news/ctp-is-hyperscaler-ai-spending-sustainable/2026/04)
- [Seeking Alpha — TSMC downgrade (Intel second life)](https://seekingalpha.com/article/4851078-tsmc-wide-moat-remains-intel-just-got-second-life-rating-downgrade) · [Yahoo — TSM Buy/Sell/Hold](https://finance.yahoo.com/markets/stocks/articles/tsm-394-buy-sell-hold-170929641.html)
- [Business Today (Reuters 인용) — TSMC US$1B 벌금 가능성](https://www.businesstoday.in/amp/technology/news/story/tsmc-could-face-over-1-billion-fine-in-us-export-control-probe-linked-to-huawei-reuters-471343-2025-04-09)
- [Tom's Hardware — Intel 14A 고객](https://www.tomshardware.com/tech-industry/semiconductors/intel-says-it-has-two-prospective-customers-for-14a-expects-to-hear-about-commitments-in-second-half-of-2026) · [bits-chips — Intel 14A](https://bits-chips.com/article/intel-signals-external-customer-wins-for-14a-foundry-process/)
- [Stocktwits — Morningstar FV US$534](https://stocktwits.com/news-articles/markets/equity/tsmc-s-leave-no-food-on-the-table-pledge-signals-more-ai-chip-investment/cZxKGj2RBsa) · [Morningstar.ca — FV +45%](https://morningstar.ca/ca/news/250638/tsmc-fair-value-raised-45-on-ai-demand.aspx) · [Webull/Simply Wall St — 13% above fair value](https://www.webull.com/news/15625565074375680)
- Section 232 2차 요약 교차확인: [EY Tax News](https://taxnews.ey.com/news/2026-0209-us-section-232-proclamation-imposes-25-percent-tariff-on-certain-semiconductors), [KPMG](https://kpmg.com/us/en/taxnewsflash/news/2026/01/united-states-imposes-tariff-advanced-computing-chips.html) (WebFetch 차단, 검색 요약만 확인)
