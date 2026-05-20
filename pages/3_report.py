import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="문제은행 리포트",
    layout="wide",
)

DATA_PATH = Path("question_bank.csv")

st.title("문제은행 리포트")
st.caption("문제은행의 주제, 난이도, 문제 유형 분포를 확인합니다.")

if not DATA_PATH.exists():
    st.error("question_bank.csv 파일이 없습니다.")
    st.stop()

try:
    df = pd.read_csv(DATA_PATH, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(DATA_PATH, encoding="utf-8-sig")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("전체 문항 수", len(df))

with col2:
    st.metric("등록 주제 수", df["topic"].nunique())

with col3:
    st.metric("문제 유형 수", df["question_type"].nunique())

st.divider()

st.markdown("### 주제별 문항 수")
topic_count = df["topic_kr"].value_counts()
st.bar_chart(topic_count)

st.markdown("### 문제 유형별 문항 수")
type_count = df["question_type"].value_counts()
st.bar_chart(type_count)

st.markdown("### 난이도별 사용 가능 문항 수")

level_rows = []

for level in range(1, 7):
    count = len(
        df[
            (df["difficulty_min"] <= level)
            & (df["difficulty_max"] >= level)
        ]
    )
    level_rows.append(
        {
            "난이도": level,
            "문항 수": count,
        }
    )

level_df = pd.DataFrame(level_rows).set_index("난이도")
st.bar_chart(level_df)