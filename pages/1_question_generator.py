import streamlit as st
import pandas as pd
from io import BytesIO
from pathlib import Path

# =========================
# Page Config
# =========================

st.set_page_config(
    page_title="OPIc 문제 생성",
    layout="wide",
)

DATA_PATH = Path("question_bank.csv")


# =========================
# Data Functions
# =========================

@st.cache_data
def load_data():
    try:
        return pd.read_csv(DATA_PATH, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(DATA_PATH, encoding="utf-8-sig")


def split_text(value):
    if pd.isna(value):
        return []
    return [item.strip() for item in str(value).split("|") if item.strip()]


def join_text(items):
    if isinstance(items, list):
        return "|".join(items)
    return str(items)


def to_excel(dataframe):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        dataframe.to_excel(writer, index=False, sheet_name="OPIc Questions")
    return output.getvalue()


# =========================
# Survey Options
# =========================

JOB_OPTIONS = {
    "사업/회사": "job_business_company",
    "재택근무/재택사업": "job_remote_business",
    "교사/교육자": "job_teacher",
    "군복무": "job_military",
    "일 경험 없음": "no_work_experience",
}

STUDENT_OPTIONS = {
    "네": "student_yes",
    "아니오": "student_no",
}

COURSE_OPTIONS = {
    "학위 과정 수업": "degree_course",
    "전문 기술 향상을 위한 평생 학습": "lifelong_learning",
    "어학 수업": "language_course",
    "수강 후 5년 이상 지남": "course_over_5_years",
}

RESIDENCE_OPTIONS = {
    "개인주택이나 아파트에 홀로 거주": "home",
    "친구나 룸메이트와 함께 주택이나 아파트에 거주": "home_with_roommate",
    "가족과 함께 주택이나 아파트에 거주": "home_with_family",
    "학교 기숙사": "school_dormitory",
    "군대 막사": "military_barracks",
}

LEISURE_OPTIONS = {
    "영화 보기": "movies",
    "클럽/나이트클럽 가기": "clubs",
    "공연 보기": "performances",
    "콘서트 보기": "concerts",
    "박물관 가기": "museums",
    "스포츠 관람": "sports_watching",
    "체스하기": "chess",
    "공원 가기": "parks",
    "해변 가기": "beaches",
    "캠핑하기": "camping",
    "주거 개선": "home_improvement",
    "술집/바에 가기": "bars",
    "카페/커피 전문점에 가기": "coffee_shops",
    "게임하기": "games",
    "당구치기": "billiards",
    "SNS에 글 올리기": "sns_posting",
    "친구들과 문자 대화하기": "texting_friends",
    "시험대비 과정 수강하기": "test_prep_courses",
    "뉴스 보거나 듣기": "news",
    "TV 시청하기": "tv_watching",
    "리얼리티 쇼 시청하기": "reality_shows",
    "요리 관련 프로그램 시청하기": "cooking_shows",
    "차로 드라이브하기": "driving",
    "스파/마사지하기": "spa_massage",
}

INTEREST_OPTIONS = {
    "아이에게 책 읽어주기": "reading_to_children",
    "음악 감상하기": "music",
    "악기 연주하기": "instruments",
    "독서": "reading",
    "혼자 노래 부르거나 합창하기": "singing",
    "춤추기": "dancing",
    "글쓰기(편지, 단문, 시 등)": "writing",
    "그림 그리기": "drawing",
    "요리하기": "cooking",
    "애완동물 기르기": "pets",
    "주식투자하기": "stock_investing",
    "신문읽기": "newspaper_reading",
    "여행 관련 잡지나 블로그 읽기": "travel_blogs",
    "사진 촬영하기": "photography",
}

SPORT_OPTIONS = {
    "농구": "basketball",
    "야구/소프트볼": "baseball_softball",
    "축구": "soccer",
    "미식축구": "american_football",
    "골프": "golf",
    "하키": "hockey",
    "크리켓": "cricket",
    "배구": "volleyball",
    "테니스": "tennis",
    "배드민턴": "badminton",
    "하이킹/트레킹": "hiking",
    "낚시": "fishing",
    "탁구": "table_tennis",
    "수영": "swimming",
    "자전거": "cycling",
    "스키/스노우보드": "skiing_snowboarding",
    "아이스 스케이트": "ice_skating",
    "조깅": "jogging",
    "걷기": "walking",
    "요가": "yoga",
    "헬스": "fitness",
    "태권도": "taekwondo",
    "운동 수업": "exercise_classes",
    "운동을 전혀 하지 않음": "no_exercise",
}

VACATION_OPTIONS = {
    "국내 출장": "domestic_business_trip",
    "해외 출장": "overseas_business_trip",
    "국내 여행": "domestic_travel",
    "해외 여행": "overseas_travel",
    "집에서 보내는 휴가": "staycation",
}

BASIC_TOPIC_KEYS = set(
    list(JOB_OPTIONS.values())
    + list(STUDENT_OPTIONS.values())
    + list(COURSE_OPTIONS.values())
    + list(RESIDENCE_OPTIONS.values())
)


# =========================
# UI Helper Functions
# =========================

def radio_topic(label, options, default_label, key):
    labels = list(options.keys())
    index = labels.index(default_label) if default_label in labels else 0

    selected_label = st.radio(
        label,
        labels,
        index=index,
        key=key,
    )

    return options[selected_label], selected_label


def checkbox_topics(options, default_labels, key_prefix):
    selected_topics = []
    selected_names = []

    for label, topic in options.items():
        checked = label in default_labels

        if st.checkbox(label, value=checked, key=f"{key_prefix}_{topic}"):
            selected_topics.append(topic)
            selected_names.append(label)

    return selected_topics, selected_names


def make_card(no, section, topic, topic_kr, question_type, question_en, vocab_10, grammar_3, phrases_2, strategy_kr):
    return {
        "no": no,
        "section": section,
        "topic": topic,
        "topic_kr": topic_kr,
        "question_type": question_type,
        "question_en": question_en,
        "vocab_10": join_text(vocab_10),
        "grammar_3": join_text(grammar_3),
        "phrases_2": join_text(phrases_2),
        "strategy_kr": strategy_kr,
    }


def render_question_card(card):
    with st.container(border=True):
        st.markdown(f"### Q{card['no']}. {card['topic_kr']} / {card['question_type']}")
        st.caption(card["section"])

        st.markdown("**Question**")
        st.write(card["question_en"])

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Useful Vocabulary**")
            vocab = split_text(card["vocab_10"])
            for idx, word in enumerate(vocab, start=1):
                st.write(f"{idx}. {word}")

        with col2:
            st.markdown("**Useful Grammar**")
            grammar = split_text(card["grammar_3"])
            for item in grammar:
                st.write(f"- {item}")

        st.markdown("**Useful Phrases**")
        phrases = split_text(card["phrases_2"])
        for phrase in phrases:
            st.write(f"- {phrase}")

        st.markdown("**Answer Strategy**")
        st.info(card["strategy_kr"])


def row_to_card(no, section, row, slot_question_type=None):
    question_type = slot_question_type if slot_question_type else row["question_type"]
    return make_card(
        no=no,
        section=section,
        topic=row["topic"],
        topic_kr=row["topic_kr"],
        question_type=question_type,
        question_en=row["question_en"],
        vocab_10=row["vocab_10"],
        grammar_3=row["grammar_3"],
        phrases_2=row["phrases_2"],
        strategy_kr=row["strategy_kr"],
    )


def difficulty_group(level):
    if level <= 2:
        return "low"
    if level <= 4:
        return "mid"
    return "high"


def get_topic_label(topic_key, df, fallback="일반 주제"):
    matched = df[df["topic"] == topic_key]
    if not matched.empty:
        return str(matched.iloc[0]["topic_kr"])
    return fallback


def sample_one(df, topics=None, question_types=None, level=None, used_ids=None):
    pool = df.copy()

    if level is not None:
        pool = pool[(pool["difficulty_min"] <= level) & (pool["difficulty_max"] >= level)]

    if used_ids:
        pool = pool[~pool["id"].isin(used_ids)]

    exact = pool.copy()

    if topics:
        exact = exact[exact["topic"].isin(topics)]

    if question_types:
        exact = exact[exact["question_type"].isin(question_types)]

    if not exact.empty:
        return exact.sample(n=1).iloc[0]

    # Fallback 1: topic only
    fallback = pool.copy()
    if topics:
        fallback = fallback[fallback["topic"].isin(topics)]
    if not fallback.empty:
        return fallback.sample(n=1).iloc[0]

    # Fallback 2: question type only
    fallback = pool.copy()
    if question_types:
        fallback = fallback[fallback["question_type"].isin(question_types)]
    if not fallback.empty:
        return fallback.sample(n=1).iloc[0]

    # Fallback 3: anything available
    if not pool.empty:
        return pool.sample(n=1).iloc[0]

    return None


def self_intro_card():
    return make_card(
        no=1,
        section="1번 - 자기소개",
        topic="self_intro",
        topic_kr="자기소개",
        question_type="Self Introduction",
        question_en="Please introduce yourself. Tell me about your personality, your daily life, and what you usually like to do in your free time.",
        vocab_10=[
            "personality",
            "daily life",
            "free time",
            "usually",
            "recently",
            "comfortable",
            "interested in",
            "enjoy",
            "relax",
            "these days",
        ],
        grammar_3=[
            "Present simple: I usually spend my free time at home.",
            "Like -ing: I like watching movies and listening to music.",
            "Because: I enjoy it because it helps me relax.",
        ],
        phrases_2=[
            "Let me briefly introduce myself.",
            "In my free time, I usually...",
        ],
        strategy_kr="자기소개는 채점 제외로 알려져 있지만, 첫 답변이므로 짧고 자연스럽게 말하는 연습용으로 넣었습니다. 이름보다 성격, 일상, 취미 중심으로 말하세요.",
    )


def roleplay_card(no, role_kind, topic_key, topic_kr):
    if role_kind == "question":
        question = f"I am your friend, and we are planning to do something related to {topic_kr}. Ask me three or four questions to make a specific plan."
        qtype = "Role-play Question"
        section = "11번 - 롤플레이 질문"
        strategy = "상대에게 시간, 장소, 선호, 비용, 준비물 등을 묻는 질문을 3~4개 연속으로 말하세요."
        phrases = ["What time would be convenient for you?", "Do you have any preference for...?"]
    elif role_kind == "alternative":
        question = f"I am sorry, but there is a problem with our plan related to {topic_kr}. Explain the situation and suggest two or three alternatives."
        qtype = "Role-play Alternative"
        section = "12번 - 롤플레이 대안 제시"
        strategy = "문제상황을 인정한 뒤, 대안을 2개 이상 제시하세요. 미안함 표현, 이유 설명, 대안 제시 순서가 좋습니다."
        phrases = ["I am sorry, but something came up.", "Instead, how about...?"]
    else:
        question = f"Tell me about a time when you had a similar problem or had to change your plan related to {topic_kr}. What happened, and how did you handle it?"
        qtype = "Role-play Experience"
        section = "13번 - 롤플레이 관련 경험"
        strategy = "과거 경험 문제처럼 상황, 문제, 행동, 결과, 느낀 점 순서로 답하면 안정적입니다."
        phrases = ["Something similar happened to me before.", "In the end, I was able to..."]

    return make_card(
        no=no,
        section=section,
        topic=topic_key,
        topic_kr=topic_kr,
        question_type=qtype,
        question_en=question,
        vocab_10=[
            "plan",
            "schedule",
            "available",
            "convenient",
            "problem",
            "alternative",
            "suggest",
            "reschedule",
            "handle",
            "situation",
        ],
        grammar_3=[
            "Indirect question: Could you tell me when you are available?",
            "Suggestion: How about meeting around 3 p.m.?",
            "Past tense: I had a similar problem before.",
        ],
        phrases_2=phrases,
        strategy_kr=strategy,
    )


def build_exam_cards(df, selected_topics, first_level, second_level):
    cards = []
    used_ids = set()

    available_topics = sorted(df["topic"].dropna().unique().tolist())
    activity_selected = [t for t in selected_topics if t not in BASIC_TOPIC_KEYS]
    survey_topics = activity_selected if activity_selected else selected_topics

    surprise_topics = [
        t for t in available_topics
        if t not in selected_topics and t not in BASIC_TOPIC_KEYS
    ]
    if not surprise_topics:
        surprise_topics = survey_topics

    first_group = difficulty_group(first_level)
    second_group = difficulty_group(second_level)

    first_plans = {
        "low": [
            (2, "2번 - 서베이 주제", "Survey Description", ["Description"], survey_topics),
            (3, "3번 - 서베이 주제", "Survey Routine", ["Routine"], survey_topics),
            (4, "4번 - 서베이 주제", "Survey Experience", ["Past Experience", "Memorable Event"], survey_topics),
            (5, "5번 - 서베이 또는 돌발", "Survey/Unexpected Description", ["Description"], survey_topics + surprise_topics),
            (6, "6번 - 서베이 또는 돌발", "Survey/Unexpected Routine", ["Routine"], survey_topics + surprise_topics),
            (7, "7번 - 서베이 또는 돌발", "Survey/Unexpected Experience", ["Past Experience", "Memorable Event"], survey_topics + surprise_topics),
        ],
        "mid": [
            (2, "2번 - 서베이 주제", "Survey Description", ["Description"], survey_topics),
            (3, "3번 - 서베이 주제", "Survey Routine", ["Routine"], survey_topics),
            (4, "4번 - 서베이 주제", "Survey Experience", ["Past Experience", "Memorable Event"], survey_topics),
            (5, "5번 - 서베이 또는 돌발", "Survey/Unexpected Description", ["Description"], survey_topics + surprise_topics),
            (6, "6번 - 서베이 또는 돌발", "Survey/Unexpected Routine", ["Routine"], survey_topics + surprise_topics),
            (7, "7번 - 서베이 또는 돌발", "Survey/Unexpected Comparison", ["Comparison", "Change"], survey_topics + surprise_topics),
        ],
        "high": [
            (2, "2번 - 서베이 주제", "Survey Description", ["Description"], survey_topics),
            (3, "3번 - 서베이 주제", "Survey Routine", ["Routine"], survey_topics),
            (4, "4번 - 서베이 주제", "Survey Experience", ["Past Experience", "Memorable Event", "Comparison"], survey_topics),
            (5, "5번 - 서베이 또는 돌발", "Survey/Unexpected Description", ["Description"], survey_topics + surprise_topics),
            (6, "6번 - 서베이 또는 돌발", "Survey/Unexpected Past Experience", ["Past Experience", "Memorable Event"], survey_topics + surprise_topics),
            (7, "7번 - 서베이 또는 돌발", "Survey/Unexpected Comparison", ["Comparison", "Change"], survey_topics + surprise_topics),
        ],
    }

    second_plans = {
        "low": [
            (8, "8번 - 돌발", "Unexpected Description", ["Description"], surprise_topics),
            (9, "9번 - 돌발", "Unexpected Routine", ["Routine"], surprise_topics),
            (10, "10번 - 돌발", "Unexpected Experience", ["Past Experience", "Memorable Event"], surprise_topics),
        ],
        "mid": [
            (8, "8번 - 돌발", "Unexpected Description", ["Description"], surprise_topics),
            (9, "9번 - 돌발", "Unexpected Routine", ["Routine"], surprise_topics),
            (10, "10번 - 돌발", "Unexpected Comparison", ["Comparison", "Change"], surprise_topics),
        ],
        "high": [
            (8, "8번 - 돌발", "Unexpected Description", ["Description"], surprise_topics),
            (9, "9번 - 돌발", "Unexpected Past Experience", ["Past Experience", "Memorable Event"], surprise_topics),
            (10, "10번 - 돌발", "Unexpected Comparison", ["Comparison", "Change"], surprise_topics),
        ],
    }

    cards.append(self_intro_card())

    for no, section, slot_qtype, qtypes, topics in first_plans[first_group]:
        row = sample_one(df, topics=topics, question_types=qtypes, level=first_level, used_ids=used_ids)
        if row is not None:
            used_ids.add(row["id"])
            cards.append(row_to_card(no, section, row, slot_question_type=slot_qtype))

    cards.append(
        make_card(
            no="중간",
            section="중간 난이도 재선택",
            topic="level_change",
            topic_kr="난이도 재선택",
            question_type="Level Check",
            question_en=f"The first part is complete. Your second-half difficulty is set to {second_level}.",
            vocab_10=["difficulty", "level", "continue", "second half", "adjust", "select", "next", "question", "part", "test"],
            grammar_3=[
                "Future: The next questions will be more challenging.",
                "Passive: The level is selected by the user.",
                "Comparison: The second part can be harder than the first part.",
            ],
            phrases_2=["Now, let's move on to the next part.", "The following questions may be more challenging."],
            strategy_kr="실제 시험 흐름을 반영하기 위한 안내 카드입니다. 다운로드에는 포함되지만, 말하기 문제로 연습하지 않아도 됩니다.",
        )
    )

    for no, section, slot_qtype, qtypes, topics in second_plans[second_group]:
        row = sample_one(df, topics=topics, question_types=qtypes, level=second_level, used_ids=used_ids)
        if row is not None:
            used_ids.add(row["id"])
            cards.append(row_to_card(no, section, row, slot_question_type=slot_qtype))

    role_topic_candidates = survey_topics + surprise_topics
    role_topic = role_topic_candidates[0] if role_topic_candidates else "coffee_shops"
    role_topic_kr = get_topic_label(role_topic, df, fallback="선택 주제")

    cards.append(roleplay_card(11, "question", role_topic, role_topic_kr))
    cards.append(roleplay_card(12, "alternative", role_topic, role_topic_kr))

    if second_group in ["mid", "high"]:
        cards.append(roleplay_card(13, "experience", role_topic, role_topic_kr))

    if second_group == "mid":
        for no, qtype_label, qtypes in [
            (14, "General Topic", ["Opinion", "Comparison", "Change"]),
            (15, "General Topic", ["Opinion", "Comparison", "Change"]),
        ]:
            row = sample_one(df, topics=surprise_topics, question_types=qtypes, level=second_level, used_ids=used_ids)
            if row is not None:
                used_ids.add(row["id"])
                cards.append(row_to_card(no, f"{no}번 - 일반 주제", row, slot_question_type=qtype_label))

    if second_group == "high":
        for no, qtype_label, qtypes in [
            (14, "Advanced Analysis", ["Opinion", "Comparison", "Change"]),
            (15, "Advanced Issue", ["Opinion", "Change", "Comparison"]),
        ]:
            row = sample_one(df, topics=surprise_topics, question_types=qtypes, level=second_level, used_ids=used_ids)
            if row is not None:
                used_ids.add(row["id"])
                cards.append(row_to_card(no, f"{no}번 - 어드밴스", row, slot_question_type=qtype_label))

    return cards


# =========================
# Main Title
# =========================

st.title("OPIc 맞춤형 예상문제 생성기")
st.caption("서베이 항목과 난이도를 선택하면 실제 시험 흐름에 가까운 순서로 예상문제를 추천합니다.")


# =========================
# Load CSV
# =========================

if not DATA_PATH.exists():
    st.error("question_bank.csv 파일이 없습니다. app.py와 같은 폴더에 question_bank.csv를 만들어주세요.")
    st.stop()

df = load_data()

required_columns = [
    "id",
    "topic",
    "topic_kr",
    "question_type",
    "difficulty_min",
    "difficulty_max",
    "question_en",
    "vocab_10",
    "grammar_3",
    "phrases_2",
    "strategy_kr",
]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(f"CSV에 필요한 컬럼이 없습니다: {missing_columns}")
    st.stop()


# =========================
# Sidebar Survey UI
# =========================

st.sidebar.header("1. OPIc 서베이 선택")

selected_topics = []
selected_topic_names = []
survey_errors = []

with st.sidebar.expander("1~3. 기본 정보", expanded=True):
    job_topic, job_label = radio_topic(
        "1. 현재 귀하는 어느 분야에 종사하고 계십니까?",
        JOB_OPTIONS,
        "일 경험 없음",
        "job_radio",
    )

    student_topic, student_label = radio_topic(
        "2. 현재 귀하는 학생이십니까?",
        STUDENT_OPTIONS,
        "아니오",
        "student_radio",
    )

    course_topic, course_label = radio_topic(
        "2-1. 최근 어떤 강의를 수강했습니까?",
        COURSE_OPTIONS,
        "수강 후 5년 이상 지남",
        "course_radio",
    )

    residence_topic, residence_label = radio_topic(
        "3. 현재 귀하는 어디에 살고 계십니까?",
        RESIDENCE_OPTIONS,
        "개인주택이나 아파트에 홀로 거주",
        "residence_radio",
    )

    selected_topics.extend([job_topic, student_topic, course_topic, residence_topic])
    selected_topic_names.extend([job_label, student_label, course_label, residence_label])


with st.sidebar.expander("4. 여가 활동", expanded=True):
    leisure_topics, leisure_names = checkbox_topics(
        LEISURE_OPTIONS,
        default_labels=[
            "영화 보기",
            "공연 보기",
            "콘서트 보기",
            "카페/커피 전문점에 가기",
            "공원 가기",
            "해변 가기",
        ],
        key_prefix="leisure",
    )

    selected_topics.extend(leisure_topics)
    selected_topic_names.extend(leisure_names)

    if len(leisure_topics) < 2:
        survey_errors.append("4번 여가 활동은 2개 이상 선택해야 합니다.")


with st.sidebar.expander("5. 취미 / 관심사", expanded=True):
    interest_topics, interest_names = checkbox_topics(
        INTEREST_OPTIONS,
        default_labels=[
            "음악 감상하기",
        ],
        key_prefix="interest",
    )

    selected_topics.extend(interest_topics)
    selected_topic_names.extend(interest_names)

    if len(interest_topics) < 1:
        survey_errors.append("5번 취미 / 관심사는 1개 이상 선택해야 합니다.")


with st.sidebar.expander("6. 운동", expanded=True):
    sport_topics, sport_names = checkbox_topics(
        SPORT_OPTIONS,
        default_labels=[
            "조깅",
            "걷기",
            "운동을 전혀 하지 않음",
        ],
        key_prefix="sport",
    )

    selected_topics.extend(sport_topics)
    selected_topic_names.extend(sport_names)

    if len(sport_topics) < 1:
        survey_errors.append("6번 운동은 1개 이상 선택해야 합니다.")

    if "no_exercise" in sport_topics and len([t for t in sport_topics if t != "no_exercise"]) > 0:
        st.warning("운동 항목과 '운동을 전혀 하지 않음'이 함께 선택되어 있습니다.")


with st.sidebar.expander("7. 휴가 / 출장 경험", expanded=True):
    vacation_topics, vacation_names = checkbox_topics(
        VACATION_OPTIONS,
        default_labels=[
            "국내 여행",
            "해외 여행",
            "집에서 보내는 휴가",
        ],
        key_prefix="vacation",
    )

    selected_topics.extend(vacation_topics)
    selected_topic_names.extend(vacation_names)

    if len(vacation_topics) < 1:
        survey_errors.append("7번 휴가 / 출장 경험은 1개 이상 선택해야 합니다.")


activity_total_count = (
    len(leisure_topics)
    + len(interest_topics)
    + len(sport_topics)
    + len(vacation_topics)
)

if activity_total_count < 12:
    survey_errors.append("4~7번 전체 선택 항목 수가 12개 이상이어야 합니다.")

st.sidebar.caption(f"4~7번 선택 항목 수: {activity_total_count}개 / 최소 12개")


# =========================
# Sidebar Difficulty UI
# =========================

st.sidebar.header("2. 난이도 선택")

first_level = st.sidebar.selectbox(
    "전반 난이도",
    [1, 2, 3, 4, 5, 6],
    index=5,
)

second_level = st.sidebar.selectbox(
    "후반 난이도",
    [1, 2, 3, 4, 5, 6],
    index=5,
)

target_grade = st.sidebar.selectbox(
    "목표 등급",
    ["IM2", "IM3", "IH", "AL"],
    index=2,
)

generation_mode = st.sidebar.radio(
    "출제 방식",
    ["실전 순서형", "랜덤 추천형"],
    index=0,
)

num_questions = st.sidebar.slider(
    "랜덤 추천형 문항 수",
    min_value=3,
    max_value=30,
    value=15,
)

question_types = sorted(df["question_type"].dropna().unique().tolist())

selected_question_types = st.sidebar.multiselect(
    "랜덤 추천형 문제 유형 선택",
    question_types,
    default=question_types,
)

generate = st.sidebar.button("예상문제 생성", type="primary")

st.sidebar.divider()
st.sidebar.caption(f"현재 문제은행 문항 수: {len(df)}개")
st.sidebar.caption(f"선택된 전체 서베이 항목 수: {len(selected_topics)}개")


# =========================
# Main Screen Summary
# =========================

with st.expander("현재 선택한 서베이 항목 보기", expanded=False):
    selected_summary = pd.DataFrame(
        {
            "선택 항목": selected_topic_names,
            "topic_key": selected_topics,
        }
    )
    st.dataframe(selected_summary, width="stretch")

with st.expander("실전 순서형 출제 구조", expanded=True):
    structure_df = pd.DataFrame(
        [
            {"문항": "1", "난이도 1-2": "자기소개", "난이도 3-4": "자기소개", "난이도 5-6": "자기소개"},
            {"문항": "2", "난이도 1-2": "서베이 묘사", "난이도 3-4": "서베이 묘사", "난이도 5-6": "서베이 묘사"},
            {"문항": "3", "난이도 1-2": "서베이 습관", "난이도 3-4": "서베이 습관", "난이도 5-6": "서베이 습관"},
            {"문항": "4", "난이도 1-2": "서베이 경험", "난이도 3-4": "서베이 경험", "난이도 5-6": "서베이 경험/비교"},
            {"문항": "5", "난이도 1-2": "서베이/돌발 묘사", "난이도 3-4": "서베이/돌발 묘사", "난이도 5-6": "서베이/돌발 묘사"},
            {"문항": "6", "난이도 1-2": "서베이/돌발 습관", "난이도 3-4": "서베이/돌발 습관", "난이도 5-6": "서베이/돌발 과거경험"},
            {"문항": "7", "난이도 1-2": "서베이/돌발 경험", "난이도 3-4": "서베이/돌발 비교", "난이도 5-6": "서베이/돌발 비교"},
            {"문항": "중간", "난이도 1-2": "난이도 재선택", "난이도 3-4": "난이도 재선택", "난이도 5-6": "난이도 재선택"},
            {"문항": "8", "난이도 1-2": "돌발 묘사", "난이도 3-4": "돌발 묘사", "난이도 5-6": "돌발 묘사"},
            {"문항": "9", "난이도 1-2": "돌발 습관", "난이도 3-4": "돌발 습관", "난이도 5-6": "돌발 과거경험"},
            {"문항": "10", "난이도 1-2": "돌발 경험", "난이도 3-4": "돌발 비교", "난이도 5-6": "돌발 비교"},
            {"문항": "11", "난이도 1-2": "롤플레이 질문", "난이도 3-4": "롤플레이 질문", "난이도 5-6": "롤플레이 질문"},
            {"문항": "12", "난이도 1-2": "롤플레이 대안", "난이도 3-4": "롤플레이 대안", "난이도 5-6": "롤플레이 대안"},
            {"문항": "13", "난이도 1-2": "출제 안 됨", "난이도 3-4": "롤플레이 경험", "난이도 5-6": "롤플레이 경험"},
            {"문항": "14", "난이도 1-2": "출제 안 됨", "난이도 3-4": "일반 주제", "난이도 5-6": "어드밴스 분석"},
            {"문항": "15", "난이도 1-2": "출제 안 됨", "난이도 3-4": "일반 주제", "난이도 5-6": "어드밴스 이슈"},
        ]
    )
    st.dataframe(structure_df, width="stretch", hide_index=True)


# =========================
# Generate Questions
# =========================

if generate:
    if survey_errors:
        for error in survey_errors:
            st.warning(error)
        st.stop()

    if not selected_topics:
        st.warning("서베이 항목을 최소 1개 이상 선택해주세요.")
        st.stop()

    selected_level = max(first_level, second_level)

    if generation_mode == "실전 순서형":
        cards = build_exam_cards(df, selected_topics, first_level, second_level)
        result_df = pd.DataFrame(cards)

        st.subheader(f"실전 순서형 OPIc 예상문제 {len(result_df[result_df['no'] != '중간'])}개")
        st.write(f"전반 난이도: **{first_level}** / 후반 난이도: **{second_level}** / 목표 등급: **{target_grade}**")

        st.download_button(
            label="엑셀로 다운로드",
            data=to_excel(result_df),
            file_name="opic_exam_style_questions.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

        for card in cards:
            render_question_card(card)

    else:
        if not selected_question_types:
            st.warning("문제 유형을 최소 1개 이상 선택해주세요.")
            st.stop()

        filtered = df[
            (df["topic"].isin(selected_topics))
            & (df["difficulty_min"] <= selected_level)
            & (df["difficulty_max"] >= selected_level)
            & (df["question_type"].isin(selected_question_types))
        ]

        if filtered.empty:
            st.error("선택한 조건에 맞는 문제가 없습니다. question_bank.csv에 문제를 더 추가해주세요.")

            st.markdown("### 선택된 topic key")
            st.write(selected_topics)

            st.markdown("### 현재 CSV에 들어있는 topic 목록")
            st.write(sorted(df["topic"].dropna().unique().tolist()))

            st.stop()

        sampled = filtered.sample(
            n=min(num_questions, len(filtered)),
            random_state=None,
        )

        cards = []
        for i, row in enumerate(sampled.to_dict(orient="records"), start=1):
            cards.append(row_to_card(i, "랜덤 추천형", row))

        result_df = pd.DataFrame(cards)

        st.subheader(f"랜덤 추천형 OPIc 예상문제 {len(result_df)}개")
        st.write(f"선택 난이도: **{first_level}-{second_level}** / 목표 등급: **{target_grade}**")

        st.download_button(
            label="엑셀로 다운로드",
            data=to_excel(result_df),
            file_name="opic_random_questions.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

        for card in cards:
            render_question_card(card)

else:
    st.info("왼쪽 사이드바에서 서베이와 난이도를 선택한 뒤, 예상문제 생성 버튼을 눌러주세요.")

    st.markdown("### 현재 문제은행 미리보기")
    st.dataframe(df.head(10), width="stretch")
