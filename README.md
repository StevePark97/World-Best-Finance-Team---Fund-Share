# AI 애널리스트 팀 (국장·미장 / 가치+성장)

Claude Code 에이전트 7명으로 구성된 주식 리서치 팀. 운영 규칙은 [CLAUDE.md](CLAUDE.md).

## 사용법
Claude Code에서 이 저장소를 열고:
```
/analyze 삼성전자
/analyze NVDA
```
결과는 `reports/<날짜>_<티커>/`에 단계별로 저장됩니다.

## 조직
사원(데이터) → 대리(밸류에이션) · 과장(국장/미장 논리) · 부장(매크로) → 차장(레드팀) → 이사(투자위원회)

## 필요한 키 (무료)
| 환경변수 | 발급처 | 없으면 |
|---|---|---|
| `DART_API_KEY` | https://opendart.fss.or.kr | 국장 재무를 웹검색으로 대체 (정확도 하락) |
| `ECOS_API_KEY` | https://ecos.bok.or.kr/api/ | 국내 금리·환율을 웹검색으로 대체 |

SEC EDGAR, FRED, Yahoo Finance는 키 불필요.

## 한계
- AI 생성 리서치이며 투자 권유가 아님. 모든 숫자는 출처 링크로 직접 검증할 것.
- Yahoo Finance는 레이트리밋이 잦음.
- `tools/ecos.py`의 통계코드는 키 발급 후 실제 응답으로 검증 필요.
