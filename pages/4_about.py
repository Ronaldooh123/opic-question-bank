import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from style import apply_global_style
import streamlit as st

st.set_page_config(
    page_title="서비스 소개",
    layout="wide",
)
apply_global_style()

st.title("서비스 소개")

st.markdown(
    """
    ## 프로젝트 개요

    이 프로젝트는 OPIc 학습자가 자신의 서베이 항목과 난이도에 맞는
    예상문제를 빠르게 확인할 수 있도록 만든 문제은행 기반 학습 서비스입니다.

    ## 개발 목적

    기존 오픽 학습자는 본인이 선택한 서베이 항목에 맞는 문제를 직접 찾아야 했습니다.
    이 서비스는 사용자가 서베이와 난이도를 선택하면 조건에 맞는 문제를 자동으로 추천합니다.

    ## 핵심 기능

    - OPIc 서베이 항목 기반 문제 추천
    - 전반 난이도와 후반 난이도 반영
    - 목표 등급 선택
    - 문제별 단어 10개 제공
    - 문제별 문법 3개 제공
    - 문제별 예시구문 2개 제공
    - 답변 전략 제공
    - 엑셀 다운로드 지원

    ## 기술 구성

    - Python
    - Streamlit
    - Pandas
    - CSV 기반 문제은행
    - OpenPyXL

    ## 장점

    - API 비용이 들지 않음
    - 인터넷 API 연결 없이 안정적으로 실행 가능
    - 문제 품질을 직접 관리할 수 있음
    - 대회 시연 중 응답 속도가 빠름
    - 문제은행을 계속 확장할 수 있음

    ## 향후 개선 방향

    - 문제은행 확대
    - 목표 등급별 답변 전략 고도화
    - 학습 모드와 시험 모드 분리
    - 사용자 답변 녹음 기능 추가
    - 답변 평가 기능 추가
    """
)