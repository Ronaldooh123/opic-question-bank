import streamlit as st

st.set_page_config(
    page_title="OPIc 맞춤형 예상문제 생성기",
    layout="wide",
)

st.title("OPIc 맞춤형 예상문제 생성기")
st.subheader("서베이와 난이도를 기반으로 나만의 오픽 예상문제를 추천합니다.")

st.markdown(
    """
    이 서비스는 OPIc Background Survey와 난이도 선택값을 바탕으로  
    문제은행에서 맞춤형 예상문제를 추천하는 학습 도우미입니다.
    """
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 서베이 기반 추천")
    st.write("직업, 거주 형태, 취미, 운동, 여행 항목을 반영해 개인화된 문제를 추천합니다.")

with col2:
    st.markdown("### 난이도 반영")
    st.write("전반 난이도와 후반 난이도 1~6 선택값에 따라 문제 유형을 조정합니다.")

with col3:
    st.markdown("### 학습자료 제공")
    st.write("문제별 단어 10개, 문법 3개, 예시구문 2개, 답변 전략을 함께 제공합니다.")

st.divider()

st.markdown("## 주요 기능")

st.markdown(
    """
    - OPIc 서베이 항목 기반 예상문제 추천
    - 전반 난이도와 후반 난이도 선택
    - 목표 등급별 학습 전략 제공
    - 문제별 단어, 문법, 예시구문 제공
    - 문제은행 기반 빠른 추천
    - 엑셀 다운로드 지원
    """
)

st.markdown("## 사용 방법")

st.markdown(
    """
    1. 왼쪽 메뉴에서 `1 question generator` 페이지로 이동합니다.
    2. OPIc 서베이 항목을 선택합니다.
    3. 전반 난이도와 후반 난이도를 선택합니다.
    4. 예상문제 생성 버튼을 누릅니다.
    5. 생성된 문제를 확인하고 필요하면 엑셀로 다운로드합니다.
    """
)

st.success("왼쪽 사이드바에서 문제 생성 페이지를 선택해 시작하세요.")