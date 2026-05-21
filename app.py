import streamlit as st
from style import apply_global_style

st.set_page_config(
    page_title="OPIc 맞춤형 예상문제 생성기",
    layout="wide",
)

apply_global_style()

st.markdown(
    """
    <div class="hero-box">
        <div class="section-label">OPIc Practice Web Service</div>
        <div class="hero-title">OPIc 맞춤형 예상문제 생성기</div>
        <div class="hero-subtitle">
            사용자의 Background Survey와 난이도 선택값을 기반으로
            자체 문제은행에서 실전형 오픽 예상문제와 학습자료를 추천합니다.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-card-title">서베이 기반 추천</div>
            <div class="feature-card-text">
                직업, 거주 형태, 여가, 취미, 운동, 여행 항목을 반영해
                개인별 맞춤 예상문제를 제공합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-card-title">실전 순서형 출제</div>
            <div class="feature-card-text">
                자기소개, 서베이, 돌발, 롤플레이, 어드밴스 문제 흐름을 반영하여
                실제 시험에 가까운 연습이 가능합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-card-title">학습자료 자동 제공</div>
            <div class="feature-card-text">
                문제별 단어 10개, 문법 3개, 예시구문 2개,
                한국어 답변 전략을 함께 제공합니다.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

st.markdown("## 사용 방법")

st.markdown(
    """
    1. 왼쪽 메뉴에서 `1 question generator` 페이지로 이동합니다.
    2. OPIc 서베이 항목을 선택합니다.
    3. 전반 난이도와 후반 난이도를 선택합니다.
    4. 출제 방식을 선택한 뒤 예상문제를 생성합니다.
    5. 생성된 문제를 확인하고 필요하면 엑셀로 다운로드합니다.
    """
)

st.markdown(
    """
    <div class="info-card">
        이 서비스는 API 과금 없이 동작하는 문제은행 기반 웹앱입니다.
        문제 품질을 직접 관리할 수 있고, 배포 환경에서도 빠르고 안정적으로 작동합니다.
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

st.markdown("## 서비스 구성")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        - 문제 생성 페이지
        - 문제은행 미리보기
        - 문제은행 리포트
        - 서비스 소개
        """
    )

with col2:
    st.markdown(
        """
        - Python
        - Streamlit
        - Pandas
        - CSV Question Bank
        - OpenPyXL
        """
    )

st.markdown(
    """
    <div class="footer-box">
        왼쪽 사이드바에서 문제 생성 페이지를 선택하면 바로 오픽 예상문제를 생성할 수 있습니다.
    </div>
    """,
    unsafe_allow_html=True,
)