# OPIc Survey-Based Question Bank Generator

OPIc 서베이 항목과 난이도 선택값을 기반으로 맞춤형 예상문제를 추천하는 Streamlit 웹앱입니다.

## 주요 기능

- OPIc 서베이 항목 선택
- 전반/후반 난이도 선택
- 실전 순서형 문제 출제
- 랜덤 추천형 문제 출제
- 문제별 단어 10개 제공
- 문제별 문법 3개 제공
- 문제별 예시구문 2개 제공
- 답변 전략 제공
- 엑셀 다운로드
- 문제은행 미리보기
- 문제은행 리포트 제공

## 기술 스택

- Python
- Streamlit
- Pandas
- OpenPyXL
- CSV 기반 문제은행

## 실행 방법

```bash
pip install -r requirements.txt
streamlit run app.py