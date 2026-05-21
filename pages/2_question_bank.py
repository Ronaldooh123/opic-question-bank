import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from style import apply_global_style
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="문제은행 미리보기",
    layout="wide",
)
apply_global_style()

DATA_PATH = Path("question_bank.csv")

st.title("문제은행 미리보기")
st.caption("현재 등록된 OPIc 문제은행 데이터를 확인합니다.")

if not DATA_PATH.exists():
    st.error("question_bank.csv 파일이 없습니다.")
    st.stop()

try:
    df = pd.read_csv(DATA_PATH, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(DATA_PATH, encoding="utf-8-sig")

st.metric("전체 문항 수", len(df))

col1, col2, col3 = st.columns(3)

with col1:
    selected_topic = st.selectbox(
        "주제 선택",
        ["전체"] + sorted(df["topic_kr"].dropna().unique().tolist()),
    )

with col2:
    selected_type = st.selectbox(
        "문제 유형 선택",
        ["전체"] + sorted(df["question_type"].dropna().unique().tolist()),
    )

with col3:
    selected_level = st.selectbox(
        "난이도 선택",
        ["전체", 1, 2, 3, 4, 5, 6],
    )

filtered = df.copy()

if selected_topic != "전체":
    filtered = filtered[filtered["topic_kr"] == selected_topic]

if selected_type != "전체":
    filtered = filtered[filtered["question_type"] == selected_type]

if selected_level != "전체":
    filtered = filtered[
        (filtered["difficulty_min"] <= selected_level)
        & (filtered["difficulty_max"] >= selected_level)
    ]

st.write(f"검색 결과: {len(filtered)}개")

st.dataframe(filtered, width="stretch")