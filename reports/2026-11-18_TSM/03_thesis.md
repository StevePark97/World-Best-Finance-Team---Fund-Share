# 03_thesis — TSMC (NYSE: TSM ADR / TWSE: 2330)

- **작성:** 과장(미장 섹터 애널리스트) · **작성일:** 2026-11-18
- **데이터 기준일:** 재무 3Q26(2026-09-30)까지, 월매출 2026년 10월분(2026-11-10 공시), 주가 TSM 2026-11-17 / 2330.TW 2026-11-18 종가, 컨센서스 2026-11-18 조회. 1차 입력은 `01_data.md`. 그 밖의 숫자는 웹검색으로 확인했고 출처 URL을 달았다.
- **조사 제약:** `www.sec.gov`, `www.webull.com`, `finance.technews.tw`, `www.trendforce.com`은 WebFetch에서 DNS가 차단됨. 20-F 원문, 어닝콜 트랜스크립트 원문, TrendForce 원문은 직접 열지 못함. 이 숫자들은 **웹검색 결과 요약(원문 인용 포함)** 으로 확인했고 `[2차출처]`로 표시. 이 세션에서 위 도메인을 허용하면 재검증 가능.
- **태그:** `[계산]` 출처 숫자로 산술 계산 / `[추정]` 과장 가정이 들어간 수치 / `[2차출처]` 회사 원문 아님 / `[학습데이터, 최신 아님]` / `[미검증]` 단일 보도, 회사 미확인.
- **회계 메모:** TSMC는 IFRS로만 보고하고 Non-GAAP 지표를 쓰지 않음 → 이 문서의 이익 수치는 모두 IFRS 보고치(GAAP 상당).

---

## 1. 사업 구조

### 1-1. 세그먼트
- TSMC의 영업 세그먼트는 **사실상 단일(파운드리)** 이므로 세그먼트별 영업이익은 공시되지 않음 `[학습데이터, 최신 아님 — 20-F 원문 미열람]`. 세그먼트별 영업이익: **데이터 없음.** 아래는 회사가 공시하는 매출 구성(플랫폼·노드·지역)이다.
- 전사 손익 (출처: 01_data.md §3, TSMC 3Q26 보도자료 https://pr.tsmc.com/english/news/3346):

| | 3Q25 | 4Q25 | 1Q26 | 2Q26 | 3Q26 |
|---|---|---|---|---|---|
| 매출 (US$ B) | 33.1 ^1 | 33.73 | 35.90 | 40.20 | 46.72 |
| 매출총이익률 | 59.5% | 62.3% | 66.2% | 67.7% | 66.4% |
| 영업이익률 | 50.6% | 54.0% | 58.1% | 60.3% | 58.7% |
| 순이익 (NT$ B) | 452.3 | 505.7 | 572.5 | 706.6 | 763.1 |

^1 3Q25 US$ 매출: TweakTown, https://www.tweaktown.com/news/108322/tsmc-posts-33-1-billion-for-the-quarter-its-best-in-history-thanks-to-ai-hpc-demand/index.html `[2차출처]` (01_data.md에는 없음)

### 1-2. 플랫폼별 (3Q26, 순매출 비중) — 출처: 01_data.md §5-2 (3Q26 Management Report)
| 플랫폼 | 비중 3Q26 | 비중 2Q26 | 3Q26 매출 환산 (US$ B) [계산] | 2Q26 환산 [계산] | QoQ [계산] |
|---|---|---|---|---|---|
| HPC | 68% | 66% | 31.8 | 26.5 | +19.8% (회사 설명 보도는 +22%, 반올림·통화 기준 차이로 보임) |
| 스마트폰 | 21% | 22% | 9.8 | 8.8 | +10.9% |
| IoT / 자동차 / DCE / 기타 | 4% / 4% / 1% / 2% | 데이터 없음 | 1.9 / 1.9 / 0.5 / 0.9 | — | — |

### 1-3. 공정 노드별 (3Q26, 웨이퍼 매출 비중) — 출처: 01_data.md §5-1
- 2nm 8%(2Q26 3%) / 3nm 33%(30%) / 5nm 28%(33%) / 7nm 10%(11%) → **7nm 이하 79%** (2Q26 77%).

### 1-4. 지역별 (고객 본사 기준) — 출처: 01_data.md §5-3 `[2차출처]`
- 북미 79% / 중국 5%(3Q25 8%) / 일본 3% / 기타(아태·EMEA) 13% [계산, 잔여].

### 1-5. 고객 집중도
| 항목 | 값 | 출처 |
|---|---|---|
| 상위 10개 고객 비중 FY2025 | 78% (FY2024 76%) | 20-F(FY2025) 분석, sec-api.io https://sec-api.io/insights/tsmc-tsm-q3-2026-earnings-nt-1-49tn-revenue-58-7-operating-margin-and-a-us-52-3bn-to-us-54-3bn-q4-outlook-sec-filing-analysis `[2차출처]` |
| 최대 고객 (보도상 Nvidia) FY2025 | 19% (FY2024 약 12%), NT$726.9B | 동상; https://parameter.io/nvidia-nvda-stock-overtakes-apple-as-tsmcs-biggest-customer ; https://www.igorslab.de/en/nvidia-overtakes-apple-at-tsmc-the-ai-powerhouse-is-located-in-taiwan/ `[2차출처]` |
| 2위 고객 (보도상 Apple) FY2025 | 17% (FY2024 22%~24%, 출처마다 다름) | 동상 `[2차출처]` |
| 20-F 원문의 고객 실명 | 20-F는 고객 이름을 밝히지 않음. 실명 매칭은 언론 보도 기반 | — |

**해석:** 상위 2개 고객이 36% [계산], 상위 10개가 78%다. 고객 쪽에서 보면 대체 공급자가 없으므로(2절) 집중도가 협상력 약화로 이어지지는 않았다. 다만 매출이 **Nvidia 한 곳의 AI GPU 사이클**에 묶여 있다는 점이 핵심 리스크다.

---

## 2. 해자 평가

**유형:** ① 공정 기술 리더십(무형자산) + ② 규모의 경제(원가) + ③ 고객 전환비용(설계 IP·PDK 종속, 재설계 비용).
**판정:** 점유율·총마진·수율 격차는 **숫자로 확인되므로 해자 강함.** 단 전환비용 자체(재설계 비용·기간)는 정량 근거가 없어 **"수치로는 불명확"** 으로 둔다.

### 2-1. 근거 숫자
| 지표 | 수치 | 출처 |
|---|---|---|
| 파운드리 매출 점유율 2Q26 | **TSMC 72.5%** (1Q26 72.3%) vs Samsung 5.9%(1Q26 6.5%), SMIC 5.4%, UMC 3.9% | TrendForce 2026-09-09, https://www.trendforce.com/presscenter/news/20260909-13225.html ; https://focustaiwan.tw/business/202609090025 |
| TSMC / Samsung 매출 배수 2Q26 | US$40.2B / US$3.26B = **12.3배** [계산] | 동상 |
| 연간 매출총이익률 | FY2024 56.1% → FY2025 59.9% | 01_data.md §2-1 |
| 분기 매출총이익률 | 3Q25 59.5% → 2Q26 67.7% → 3Q26 66.4% (N2 초기 램프와 해외 팹 희석을 소화한 수치) | 01_data.md §3 |
| ROE (자기자본이익률) | FY2025 35.8% [계산: 1,717.9B / 평균자본 4,799.7B], 3Q26 연환산 45.5% [계산: 763.1B×4 / 평균자본 6,715.2B] | 01_data.md §2-1, §3 |
| 2nm 수율 (보도) | TSMC N2 60~70% vs Samsung SF2 50%대 중반(후공정 포함 실효 수율 약 40%) | TrendForce 2026-04-14, https://www.trendforce.com/news/2026/04/14/news-samsung-2nm-yields-reportedly-at-55-below-mass-production-threshold-qualcomm-may-opt-for-tsmc/ `[2차출처, 미검증 — 회사들은 수율을 공시하지 않음]` |
| 첨단 노드 비중 | 7nm 이하 79% (3Q26) | 01_data.md §5-1 |

### 2-2. 경쟁사 대비 격차
| 경쟁사 | 현황 | 격차 판단 | 출처 |
|---|---|---|---|
| Samsung Foundry (SF2) | 수율 50%대 중반(보도). Apple·Nvidia·AMD 같은 대형 외부 고객은 아직 없음. Tesla AI5/AI6 수주 | 점유율 5.9%로 하락 중 | https://semiwiki.com/semiconductor-manufacturers/intel/367081-global-2nm-supply-crunch-tsmc-leads-as-intel-18a-samsung-and-rapidus-race-to-compete/ ; TrendForce(위) `[2차출처]` |
| Intel Foundry (18A / 14A) | 18A는 주로 자사 제품용이고 "물량이 아직 의미 있지 않음". 14A: 2H27 내부 리스크 생산, 2028 HVM 램프. 외부 고객 확정은 2H26~1H27 예정이며 **2026-11-18 현재 실명 공개된 확정 고객 없음** | 대량 외부 공급까지 2년 이상 | https://www.tomshardware.com/tech-industry/semiconductors/intel-says-it-has-two-prospective-customers-for-14a-expects-to-hear-about-commitments-in-second-half-of-2026 ; https://borecraft.com/2026/06/17/intels-post-18a-roadmap-hangs-on-landing-14a-foundry-customers/ `[2차출처]` |
| Rapidus (2nm) | 2027년 전후 양산 목표, 상업 실적 없음 | 검증 전 | Tom's Hardware 로드맵 https://www.tomshardware.com/tech-industry/semiconductors/leading-edge-foundry-roadmaps-for-tsmc-intel-and-samsung-outlining-the-path-to-1-4nm-nodes-and-beyond `[2차출처]` |
| TSMC 로드맵 | N2 HVM 4Q25 → N2P/A16 → A14(2027 리스크, 2028 양산) | — | https://www.webull.com/news/15751044230423552 (검색 요약) ; https://www.trendforce.com/news/2026/04/16/news-tsmc-n3-tightens-on-ai-demand-arizona-2nd-fab-3nm-volume-production-in-2h27-kumamoto-in-2028/ `[2차출처]`. **A16 2H26 양산 여부는 미확인** |

### 2-3. 해자 위협 (반대 증거)
- CoWoS가 병목이 되면서 Intel EMIB 같은 대체 패키징이 거론됨 (https://www.trendforce.com/news/2026/04/16/news-tsmc-says-cowos-offers-industrys-largest-reticle-size-packaging-amid-intel-emib-rivalry-copos-advances/ `[2차출처]`). 실제 고객 이탈 숫자는 **데이터 없음.**
- 미국 정부가 "미국 내 생산"을 유도함 → 해자가 기술이 아니라 **입지(정치)** 로 일부 훼손될 수 있음. Intel 14A 외부 고객이 확정되면 처음으로 숫자로 확인되는 신호가 됨.

---

## 3. 성장 동인 3개 (+ 가격 인상)

### 동인 1 — AI 가속기(HPC) 수요
| 구분 | 수치 | 출처 |
|---|---|---|
| **매출로 확인된 부분** | AI 가속기 = FY2025 매출의 "high-teens %" → **약 US$19.6B~23.3B** [계산: 16~19% × US$122.42B] | 4Q25 콜 요약, https://vectorshift.ai/research/companies/taiwan-semiconductor-manufacturing-co/earnings/2025-q4 ; https://www.fool.com/investing/2026/03/26/1-compelling-reason-to-buy-taiwan-semiconductor/ `[2차출처]` |
| 확인 | HPC 매출 3Q26 약 US$31.8B (전체의 68%), 2Q26 대비 +19.8% [계산]. 단 HPC에는 CPU·네트워크 등 AI 외 제품이 섞여 있음 | 01_data.md §5-2 |
| 확인 | 최대 고객(보도상 Nvidia) 비중 FY2024 약 12% → FY2025 19% | 1-5절 |
| 확인 | 2026년 1~10월 매출 +43.3% YoY, 10월 +59.7% | 01_data.md §4 |
| **기대 부분** | 회사 가이던스: AI 가속기 매출 2024~2029 CAGR **"mid-to-high 50s %"** (2025년 1월 mid-40s에서 상향, 2026-10 재확인, CEO는 "보수적일 수 있다"고 언급) | https://futurumgroup.com/insights/tsmc-q3-fy-2026-earnings-beat-and-raise-on-ai-and-hpc-demand/ ; https://www.crnasia.com/news/2026/components-and-peripherals/tsmc-third-quarter-revenue-tops-guidance-as-ceo-says-ai-dema `[2차출처]` |
| 기대 | 2025 기준점(약 US$21B)에 연 55%를 4년 단순 적용하면 2029년 **약 US$120B 내외** [추정] — 회사가 2029년 금액으로 제시한 숫자는 아님 | [추정] |
| 기대 | 전사 매출 CAGR 2024~2029 "approach 25%"(2026-01). FY2024 US$90.1B [계산: 122.42/1.359]에 적용하면 2029년 US$275B [계산]. FY2026이 이미 US$175~177B로 예상되므로 남은 2026~2029 암시 CAGR은 **약 16%** [계산]. 회사 장기 가이던스가 실적에 뒤처져 있다는 뜻이고, 2027년 1월 갱신 여부가 촉매 | https://rallies.ai/news/tsmc-shares-rally-58-weekly-445-after-hours-following-q4-growth-outlook `[2차출처]` |

### 동인 2 — N2(2nm) 램프 (A16은 미확인)
| 항목 | 수치 | 출처 |
|---|---|---|
| N2 HVM 시작 | 4Q25, 신주·가오슝에서 단계적 램프 | 3Q26 콜 요약, https://www.webull.com/news/15751044230423552 `[2차출처]` |
| N2 웨이퍼 매출 비중 | 2Q26 3% → **3Q26 8%** | 01_data.md §5-1 |
| N2 매출 환산 3Q26 | 약 US$3.7B [추정: 8% × 전체 매출 46.72B. 웨이퍼 매출 기준 비중을 전체 매출에 곱했으므로 과대 추정 가능] | [추정] |
| 2027 생산능력 | N2 계열 연간 생산능력이 2027년 **2배 이상** | 3Q26 콜 요약(위) `[2차출처]` |
| 마진 비용 | N2 초기 램프의 GM 희석: FY2026 2~3%p(2026-04 가이던스), 2H26 3~4%p(2026-07 가이던스) | https://www.itiger.com/news/1103082639 ; TSMC 1Q26·2Q26 트랜스크립트(검색 요약) https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/547d1696765e05ce3adb81c108ce1c8c1682b80c/TSMC%202Q26%20Transcript.pdf `[2차출처]` |
| 웨이퍼 단가 | N2는 N3(약 US$20,000)보다 50% 이상 비싼 US$30,000 이상 (TrendForce 과거 추정) | `[2차출처, 오래된 추정 — 미검증]` |
| 정량 효과 | N2 비중이 2Q26 3%에서 3Q26 8%로 오르는 동안 GM은 67.7%에서 66.4%로 1.3%p 하락. 희석이 줄어드는 2027~28년에는 GM이 다시 오를 여지 [추정] | 01_data.md §3 |

### 동인 3 — CoWoS 등 첨단 패키징 증설
| 항목 | 수치 | 출처 |
|---|---|---|
| **확인:** 첨단 패키징 매출 비중 | FY2025 약 8% → **약 US$9.8B** [계산: 8% × 122.42B] | Commercial Times 인용 TrendForce `[2차출처]` https://www.trendforce.com/news/?p=55914 (검색 요약) |
| **기대:** 2026 비중 | 10% 초과 → **US$17.5B 이상** [추정: 10% × FY2026 가이던스 암시 매출 US$175~177B] | 동상 `[2차출처]` |
| CoWoS 월 생산능력 | 2026년 12만~14만 장(말 기준 약 13만 장) → 2027년 17만~23만 장(기관마다 다름) → 2028년 말 약 26만 장(2배) | https://www.trendforce.com/news/2026-09-14/news-tsmc-reportedly-targets-22-2nm-16-3nm-capacity-boost-by-mid-2027-cowos-to-double-by-2028/ ; KGI https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/tsmc_2330-tt_09032026e.pdf `[2차출처, 회사 미공시]` |
| 수급 | CoWoS 수급 부족률이 2026년 말 약 20%에서 10%로 축소 예상(보도). 회사는 "AI 수요가 공급을 초과" | https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands ; CRN Asia(위) `[2차출처]` |
| CAPEX 배분 | CAPEX의 10~20%를 첨단 패키징·테스트·마스크에 배정 (2Q26 콜) | https://www.fool.com/earnings/call-transcripts/2026/07/16/tsm-tsm-q2-2026-earnings-call-transcript/ `[2차출처]` |

### (보조 동인) 가격 인상
| 항목 | 수치 | 출처 |
|---|---|---|
| 2027 첨단 노드 단가 | 인상률 +3~6%(보도) / +5~10%(Nomura, Morgan Stanley 추정). 2027년 초 적용, 4분기 중 확정 | https://www.kucoin.com/blog/tsmc-reportedly-plans-3-6-wafer-price-hike-in-2027-as-ai-demand-pushes-orders-to-2030 ; https://www.tomshardware.com/tech-industry/semiconductors/tsmc-eyes-price-hikes-of-up-to-25-percent-on-chip-production-services-in-2027-report-claims-plans-to-raise-baseline-prices-by-5-percent-to-10-percent-on-advanced-nodes `[2차출처]` |
| 회사 입장 | **TSMC는 2027 인상 보도를 확인하지 않음** | https://www.taiwanplus.com/news/taiwan-news/business/260722011/tsmc-declines-to-confirm-report-of-2027-price-hikes |
| CoWoS 단가 | 약 20% 인상 검토 보도 | https://trendforce.com/news/2026/10/27/news-tsmc-reportedly-eyes-20-cowos-price-hike-skips-equipment-price-renegotiations-amid-ai-demand-surge `[미검증]` |
| 민감도 | 7nm 이하(웨이퍼 매출의 79%)에 +5%를 적용하면 매출 약 +4% [추정]. FY2027 컨센서스 매출 NT$7,691B 기준 약 NT$300B [추정]. 대부분 매출총이익으로 직결된다고 가정 | 01_data.md §8, [추정] |
| 25% 인상 보도 | 이상치로 취급(CEO가 급격한 인상을 부인) | Tom's Hardware(위) |

---

## 4. 촉매 (향후 12개월, 2026-11-18 ~ 2027-11)

| 시점 | 이벤트 | 볼 지표 | 출처/근거 |
|---|---|---|---|
| 2026-12-10 | 2Q26 배당 NT$7.00 배당락 (지급 2027-01-07) | — | 01_data.md §7-3 |
| 2026-12-10 전후 | 11월 월매출 공시 (매월 10일경) | 4Q26 가이던스 US$52.3~54.3B 달성 경로. 10월 NT$586.89B | 01_data.md §4 패턴 `[추정 일정]` |
| 2027-01 중순 | **4Q26 실적 + FY2027 매출 성장률·CAPEX·GM 가이던스**, 장기 CAGR(전사 25%, AI 50%대 중후반) 갱신 여부 | FY2027 USD 성장률(컨센서스 매출 NT$7,691B ≈ +37% [계산, vs FY2026E 5,582B]), CAPEX, 해외 팹 희석 | 직전 4Q 발표일 2026-01-15 기준 `[추정 일정]` |
| 2027-01-01 | 2027 단가 인상 적용 (보도) | 1Q27 GM 가이던스에 반영되는지 | 3절 `[미검증]` |
| 2H26~1H27 | Intel 14A 외부 고객 확정 발표 여부 | 대형 팹리스(Apple/Nvidia/AMD/Qualcomm) 이름이 나오는지 | Tom's Hardware(2-2절) |
| 미정 | 미국 Section 232 반도체 관세 2단계(서버·소비자 전자 포함) 및 상무부 보고서 공개 | 대만 우대 쿼터(미국 계획 생산량의 2.5배, 완공 시 1.5배)가 유지되는지 | https://www.morganlewis.com/pubs/2026/02/section-232-investigations-prompt-trade-negotiation ; https://www.geopoliticalmonitor.com/?p=56574 `[2차출처]` |
| 2027-03-11 | 3Q26 배당 NT$9.00 배당락 (지급 2027-04-08) | 배당 인상 지속 여부 | 01_data.md §7-3 |
| 2027-04 중순 | 1Q27 실적, 20-F(FY2026) 제출 (전년 2026-04-16) | 20-F Risk Factors 신규 항목, 상위 고객 비중 | 01_data.md §1 `[추정 일정]` |
| 2027 | Rapidus 2nm 양산 개시 목표, ESMC 드레스덴 생산 개시 | 수율·고객 공개 여부 | 2-2절; 01_data.md §6-2 |
| 2027-07 중순 | 2Q27 실적 | N2 희석 축소, 해외 팹 희석 | `[추정 일정]` |
| 3Q27 | 애리조나 Fab 2 (3nm) 양산 | 해외 팹 GM 희석이 3~4%p로 확대되는 구간 진입 | 01_data.md §6-2 |
| 상시 | 2026-11-17 ADR −3.68% 원인으로 언급된 "미 상무부 파운드리 신규 규정" | **실체 미확인 — 사실로 쓰지 않음** | 01_data.md §11 `[미검증]` |

---

## 5. 미국 시장 요인 (TSMC 특성 반영)

### 5-1. SBC·희석·자사주 (TSMC에는 거의 해당 없음)
- SBC/매출: FY2025 0.033% [계산: 1,246 / 3,809,054], 최근 4분기 0.010% [계산: 513 / 4,944,817] (01_data.md §2-1, §3).
- 주식수: FY2022말 25,930.4M → 3Q26말 25,932.4M주. **사실상 변화 없음(4년간 +0.008%)** [계산]. 자사주 매입 프로그램 없음(SEC XBRL 기준. Yahoo의 소액 기록은 RSA용으로 추정되며 원문 미확인).
- 결론: SBC 차감 후 FCF와 보고 FCF의 차이는 무의미한 수준. 주주환원은 **배당** 중심.

### 5-2. 배당정책
| 항목 | 수치 | 출처 |
|---|---|---|
| 분기 배당 추이 | NT$5.0(2Q25) → 6.0 → 6.0 → 7.0 → 7.0 → **9.0(3Q26, +28.6% QoQ)** | 01_data.md §7-3; https://focustaiwan.tw/business/202611110009 |
| 연환산 / 수익률 | NT$36 → 1.66% (2330.TW 기준) [계산, 01_data] | 01_data.md §7-3 |
| 배당성향 (이익) | 최근 4분기 지급 배당 NT$570.5B / 순이익 NT$2,547.9B = **22.4%** [계산] | 01_data.md §3 |
| FCF 커버리지 | 최근 4분기 FCF NT$1,457.6B / 지급 배당 570.5B = **2.55배** [계산] | 01_data.md §3 |
| 정책 문구 | 2019년부터 분기 배당. 20년 넘게 연간 기준 감액 없음 | https://www.marketbeat.com/articles/what-investors-need-to-know-about-tsmcs-hefty-17-dividend-increase/ `[2차출처]` |
| 미국 ADR 보유자 | 대만 원천징수로 실수령액이 표면 금액보다 약 21% 적음 | 동상 `[2차출처]` |

### 5-3. 해외 팹 총이익률 희석 (회사 제시)
| 시점 | 회사 가이던스 | 출처 |
|---|---|---|
| 2026-04 (1Q26 콜) | 해외 팹 희석: 초기 2~3%p, 후기 3~4%p (향후 수년) | https://www.itiger.com/news/1103082639 ; TSMC 1Q26 트랜스크립트(검색 요약) `[2차출처]` |
| 2026-10 (3Q26 콜) | FY2026은 **2%p에 가까움**, 이후 3~4%p로 확대 | https://futurumgroup.com/insights/tsmc-q3-fy-2026-earnings-beat-and-raise-on-ai-and-hpc-demand/ ; 01_data.md §3-1 |
| 금액 환산 | 2%p × FY2026 암시 매출 NT$5,562~5,625B ≈ **NT$111~113B 매출총이익 감소** [계산]. 3~4%p로 커지면 매출 규모에 따라 2배 안팎 [추정] | [계산]/[추정] |
| 법인별 손익 FY2025 | 애리조나 순이익 NT$16.1B(2024년 −14.3B에서 흑자 전환), 구마모토 −9.77B, ESMC −0.69B, 중국(난징·상하이) +39.2B | TrendForce(TSMC 2025 연차보고서 인용) https://www.trendforce.com/news/2026/03/02/news-tsmcs-2025-overseas-split-china-leads-profits-arizona-turns-profitable-japan-losses-triple/ `[2차출처]` |
| 환율 희석 (참고) | NT$ 1% 절상 시 GM 약 0.4%p 하락(2025-06 회장 발언). 다른 계산으로는 약 0.24%p | https://www.digitimes.com/news/a20250710VL210.html ; https://www.implicator.ai/tsmc-defies-currency-surge-with-record-ai-fueled-profits.md `[2차출처]` |

### 5-4. 경영진 가이던스 vs 실적 (최근 7분기)
| 분기 | 매출 가이던스 (US$B) | 실적 | 판정 | GM 가이던스 | 실적 GM | 판정 | 출처 |
|---|---|---|---|---|---|---|---|
| 1Q25 | 25.0~25.8 | 25.53 | 범위 내 | 57~59% | 58.8% | 범위 내 | SEC 6-K https://www.sec.gov/Archives/edgar/data/1046179/000104617925000035/a1q25e_withguidancexfinal.htm ; https://anysilicon.com/tsmcs-financial-results-2025-q1/ |
| 2Q25 | 28.4~29.2 | 30.07 | **상단 초과** | 57~59% | 58.6% | 범위 내 | https://www.itiger.com/news/2552043221 ; KGI https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/tsmc_2330-tt_18072025e.pdf |
| 3Q25 | 31.8~33.0 | 33.1 | 상단 초과 | 55.5~57.5% | 59.5% | **상단 +2.0%p** (가정 환율 30.6 vs 실제 29.91) | SEC 6-K a3q25e ; https://www.fool.com/earnings/call-transcripts/2025/10/17/tsmc-tsm-q3-2025-earnings-call-transcript |
| 4Q25 | 32.2~33.4 | 33.73 | 상단 초과 | 59~61% | 62.3% | 상단 +1.3%p | https://www.digitimes.com/news/a20260116PD232.html ; https://futurumgroup.com/insights/tsmc-q4-fy-2025-results-and-fy-2026-outlook-signal-ai-led-growth |
| 1Q26 | 34.6~35.8 | 35.90 | 상단 초과 | 63~65% | 66.2% | 상단 +1.2%p | https://www.trendforce.com/news/2026/04/16/news-tsmc-1q26-net-income-soars-58-yoy-to-nt572-5b-record-eps-nt22-08-gross-margin-beats-forecast-at-66-2/ |
| 2Q26 | 39.0~40.2 | 40.20 | 상단 일치 | 65.5~67.5% | 67.7% | 상단 +0.2%p | 01_data.md §3-1 |
| 3Q26 | 44.6~45.8 | 46.72 | 상단 초과 | 65~67% | 66.4% | 범위 내(중간값 상회) | 01_data.md §3-1 |
| 4Q26 | 52.3~54.3 | 발표 예정 | — | 65~67% | — | — | 01_data.md §3-1 |

- **요약:** 7분기 동안 매출·GM 모두 **하회 0회.** 매출은 5회 상단 초과, 1회 상단 일치, 1회 범위 내. GM은 4회 상단 초과, 3회 범위 내 [계산].
- **주의:** GM 초과분 일부는 환율 덕분이다(예: 3Q25 가정 30.6 vs 실제 29.91). 3Q26은 2025년 이후 처음으로 GM이 상단을 넘지 못한 분기이며, 원인은 N2 희석이다.
- **연간 가이던스 상향 이력(FY2026 USD 매출 성장률):** 1월 약 30% → 4월 "30% 초과" → 7월 "40% 초과" → 10월 약 44%. CAPEX는 US$52~56B → 60~64B. 출처: https://www.storagenewsletter.com/2026/05/19/tsmc-fiscal-1q26-financial-results/ ; 01_data.md §3-1, §6-1 `[2차출처 혼재]`.

### 5-5. 20-F Risk Factors 신규 항목
- **20-F(FY2025, 접수 2026-04-16) 원문 Risk Factors: 데이터 없음.** sec.gov가 DNS 차단되어 원문 대조나 FY2024 대비 diff를 하지 못함.
- 2차출처로 확인된 관련 문구(신규 여부 미확인): 수출통제·관세 변화가 매출 손실·평판 훼손·벌금으로 이어질 수 있다는 문구, 칩이 의도하지 않은 최종 사용자에게 흘러가는 것(전용)을 완전히 통제할 수 없다는 문구, 지역 정치 안정성과 지정학적 긴장 — https://www.techrepublic.com/article/news-tsmc-us-chips-china/ `[2차출처]`.
- → 이사회/레드팀 검증용 **미결 항목**으로 남김.

### 5-6. 금리 민감도
- TSMC는 전형적인 "장기 듀레이션 성장주"는 아니다. TTM P/E 22.1배 [계산: 2,175 / 98.26], FY2027E P/E 14.5배 [계산: 2,175 / 149.53], TTM FCF 수익률 2.6% [계산: 1,457.6B / 56,402.9B], 순현금 NT$2.56T (01_data.md §3, §7, §8).
- 다만 주가는 AI 반도체 바스켓과 함께 움직이므로 **멀티플 측면의 금리 민감도는 업종을 따라간다** [추정]. 이자 비용은 순현금 구조라 거의 영향 없음. 금리보다는 **NT$ 환율(GM 0.24~0.4%p/1%)과 AI CAPEX 사이클**이 더 큰 변수다. 상세는 부장(04_macro.md) 담당.

### 5-7. 규제·관세·수출통제·지정학
| 항목 | 현황 | 노출 크기 | 출처 |
|---|---|---|---|
| Section 232 반도체 관세 | 1단계(2026-02): 일부 로직 칩 HS 코드에 25%. 대만 기업은 미국 내 증설 계획 물량의 2.5배(완공 시 1.5배)까지 면세 쿼터(2026-01-15 발효). 2단계(서버·소비자 전자로 확대)는 일정 미정 | 북미 고객 비중 79%. 다만 TSMC는 수출자로서 "간접 영향"(CEO, 2026-03). 애리조나 원가 상승 리스크 | Morgan Lewis(4절); https://finance.yahoo.com/economy/policy/articles/taiwan-says-us-no-timetable-055911200.html ; https://stocktwits.com/news-articles/markets/equity/tsmc-ceo-says-ai-demand-strong-but-trump-s-tariffs-still-a-risk/chkr3sdRbvX `[2차출처]` |
| 수출통제 (중국) | 난징 팹 VEU 철회(2025-12-31 발효), 1년 장비 반입 라이선스(보도). 중국 매출 비중 8%(3Q25) → 5%(3Q26) | 매출 영향은 축소됐지만 중국 팹 이익(FY2025 NT$39.2B)이 노출되어 있음 | 01_data.md §10; TrendForce(5-3절) |
| 대만해협 | 첨단 공정 생산능력의 대부분이 대만에 있음. 해외 생산능력 비중: **데이터 없음** | 정량화 불가, 꼬리 리스크 | 20-F 미래예측 고지(2차출처, 5-5절) |
| 보조금 | 미·일·독·중에서 NT$167.6B 수령(누적 기록치, 기간 미확인) | 해외 팹 희석 일부 상쇄 | 01_data.md §6-2 |
| AI 기업 지분투자 | 이사회 승인: Anthropic PBC 최대 US$500M, OpenAI Group PBC 최대 US$500M | 현금 NT$3.6T 대비 미미. 고객 관계 강화 신호로 해석 [추정] | 01_data.md §11 |

---

## 6. 투자 논리 요약 (3줄) + Kill Criteria

**논리 1 — AI 수요가 "가이던스보다 빠르게" 매출로 확인되고 있다.**
FY2026 USD 성장률 가이던스는 30% → 44%로 세 번 올라갔고, HPC 비중은 68%, 10월 매출은 +59.7% YoY다. AI 가속기는 FY2025에 약 US$20B 수준(확인)이고 2024~29 CAGR은 50%대 중후반(기대)이다. 장기 전사 CAGR 25%는 실적보다 뒤처져 있다.
- **Kill:** ① 2027년 1월 FY2027 USD 매출 성장률 가이던스가 **+20% 미만**, ② 월매출 YoY가 **3개월 연속 +20% 미만**, ③ AI 가속기 CAGR 가이던스가 "mid-50s" 아래로 하향, ④ 분기 HPC 매출(비중×매출)이 **2분기 연속 QoQ 감소**, ⑤ FY2027 CAPEX 가이던스가 FY2026(US$60~64B)보다 낮게 나옴(수요 둔화 신호).

**논리 2 — 해자가 점유율과 마진으로 숫자상 확대되고 있다(N2 희석과 해외 팹 희석을 흡수하고도 GM 66%).**
파운드리 점유율은 72.5%, Samsung 대비 매출 12배다. 경쟁사는 수율 미달(Samsung)이거나 외부 고객 미확정(Intel 14A), 미양산(Rapidus)이다. 2027년에는 단가 인상(보도, 미확인)과 N2 희석 축소가 해외 팹 3~4%p 희석을 상쇄할 것으로 본다 [추정].
- **Kill:** ① 분기 GM 가이던스 중간값이 **60% 미만**(N2·해외 팹 희석으로 설명되지 않는 하락), ② TrendForce 분기 점유율 **65% 미만**, ③ Apple·Nvidia·AMD·Qualcomm 중 1곳이 **주력 제품 첨단 노드 양산을 Intel 14A 또는 Samsung SF2로 이전**한다고 공식 발표, ④ 2027년 단가 인상이 1Q27 GM 가이던스에 반영되지 않음(가이던스 중간값이 4Q26 66%보다 낮음).

**논리 3 — 배당과 CAPEX를 동시에 감당하는 현금창출력에, 지정학·관세 리스크는 아직 숫자로 실현되지 않았다.**
TTM FCF NT$1.46T는 배당의 2.55배이고, 순현금 NT$2.56T, 배당은 4분기 만에 NT$5에서 NT$9로 늘었다. 관세는 대만 쿼터 면세 구조이고, 중국 매출은 5%로 축소됐다.
- **Kill:** ① TTM FCF가 **지급 배당 미만**(CAPEX 강도가 매출의 45%를 넘거나 OCF가 꺾이는 경우), ② 분기 배당 동결이 **2분기 연속** 또는 감액, ③ Section 232 2단계가 TSMC 웨이퍼/모듈에 **쿼터 면세 없이** 적용, ④ 회사가 해외 팹 희석 가이던스를 4%p 초과로 상향, ⑤ 대만해협 봉쇄·검역 등 물리적 공급 차질(정량 지표는 없음. 발생 즉시 논리 폐기).

---

## 출처 및 미결 사항
- 1차 입력: `/home/user/world-best-finance-team---fund-share/reports/2026-11-18_TSM/01_data.md`
- 추가 조사 출처는 각 표의 URL 참조. 회사 원문(6-K, 트랜스크립트, 20-F)은 **검색 요약을 통해서만** 확인함.
- **미결:** 20-F FY2025 Risk Factors 신규 항목(원문 미열람), 세그먼트 영업이익(단일 세그먼트로 추정), 해외 생산능력 비중, A16 양산 시점, 2027 단가 인상 확정 여부, 2026-11-17 "상무부 파운드리 규정"의 실체, 고객 실명별 비중(20-F는 익명).
