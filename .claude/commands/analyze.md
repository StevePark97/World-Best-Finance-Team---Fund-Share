---
description: 애널리스트 팀 전체 파이프라인으로 종목 분석 (사원→대리·과장·부장→차장→이사)
argument-hint: <종목명 또는 티커> (예: 삼성전자, 005930, NVDA)
---

종목 `$ARGUMENTS`에 대해 애널리스트 팀 파이프라인을 실행한다. CLAUDE.md의 절대 규칙을 따른다.

1. 종목을 식별한다: 국장이면 6자리 종목코드와 `.KS`/`.KQ` 티커, 미장이면 티커. 모호하면 사용자에게 묻는다.
   폴더 `reports/<오늘 날짜>_<티커>/`를 만든다.
2. **사원** `associate-data` 에이전트를 실행해 `01_data.md`를 만든다. 완료될 때까지 기다린다.
3. 다음 3명을 **병렬로** 실행한다 (한 메시지에 3개 Agent 호출):
   - **대리** `valuation-analyst` → `02_valuation.md`
   - **과장** 국장이면 `sector-analyst-kr`, 미장이면 `sector-analyst-us` → `03_thesis.md`
   - **부장** `macro-strategist` → `04_macro.md`
4. **차장** `redteam-risk` 실행 → `05_redteam.md`
5. **이사** `investment-committee` 실행 → `06_ic_memo.md`, `README.md`
6. 사용자에게 이사의 결론(의견·확신도·진입조건·핵심리스크)을 10줄 이내로 보고하고, 데이터 품질 문제가 있었다면 함께 알린다.

각 에이전트에게는 폴더 경로, 종목 식별 정보, 오늘 날짜를 반드시 전달한다.
