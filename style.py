import streamlit as st


def apply_global_style():
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 3rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }

        [data-testid="stSidebar"] {
            background-color: #f8fafc;
            border-right: 1px solid #e5e7eb;
        }

        [data-testid="stSidebar"] * {
            color: #111827;
        }

        h1 {
            font-size: 2.5rem !important;
            font-weight: 800 !important;
            letter-spacing: -0.04em;
            color: #111827;
        }

        h2, h3 {
            letter-spacing: -0.03em;
            color: #111827;
        }

        p, li, div {
            line-height: 1.65;
        }

        .hero-box {
            padding: 2.2rem 2.4rem;
            border-radius: 24px;
            background: linear-gradient(135deg, #eef4ff 0%, #f8fafc 55%, #ffffff 100%);
            border: 1px solid #e5e7eb;
            margin-bottom: 1.5rem;
        }

        .hero-title {
            font-size: 2.4rem;
            font-weight: 850;
            color: #111827;
            letter-spacing: -0.05em;
            margin-bottom: 0.5rem;
        }

        .hero-subtitle {
            font-size: 1.05rem;
            color: #4b5563;
            max-width: 760px;
        }

        .section-label {
            font-size: 0.85rem;
            font-weight: 700;
            color: #2563eb;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.4rem;
        }

        .feature-card {
            padding: 1.4rem 1.5rem;
            border-radius: 18px;
            border: 1px solid #e5e7eb;
            background-color: #ffffff;
            min-height: 170px;
            box-shadow: 0 8px 22px rgba(15, 23, 42, 0.04);
        }

        .feature-card-title {
            font-size: 1.1rem;
            font-weight: 750;
            color: #111827;
            margin-bottom: 0.45rem;
        }

        .feature-card-text {
            color: #4b5563;
            font-size: 0.95rem;
        }

        .info-card {
            padding: 1.2rem 1.4rem;
            border-radius: 16px;
            border: 1px solid #dbeafe;
            background-color: #eff6ff;
            color: #1e3a8a;
            margin-top: 1rem;
        }

        .question-card {
            padding: 1.6rem 1.7rem;
            border-radius: 20px;
            border: 1px solid #e5e7eb;
            background-color: #ffffff;
            box-shadow: 0 10px 26px rgba(15, 23, 42, 0.05);
            margin-bottom: 1.2rem;
        }

        .question-title {
            font-size: 1.35rem;
            font-weight: 800;
            color: #111827;
            margin-bottom: 0.2rem;
        }

        .question-meta {
            font-size: 0.9rem;
            color: #6b7280;
            margin-bottom: 1rem;
        }

        .question-text {
            font-size: 1rem;
            color: #111827;
            background-color: #f9fafb;
            border-left: 4px solid #2563eb;
            padding: 0.9rem 1rem;
            border-radius: 12px;
            margin-bottom: 1rem;
        }

        .small-muted {
            color: #6b7280;
            font-size: 0.9rem;
        }

        .footer-box {
            margin-top: 2.5rem;
            padding: 1.2rem 1.4rem;
            border-radius: 16px;
            background-color: #f9fafb;
            border: 1px solid #e5e7eb;
            color: #4b5563;
        }

        div[data-testid="stButton"] > button {
            border-radius: 12px;
            border: 1px solid #2563eb;
            background-color: #2563eb;
            color: white;
            font-weight: 700;
            padding: 0.55rem 1rem;
        }

        div[data-testid="stDownloadButton"] > button {
            border-radius: 12px;
            border: 1px solid #d1d5db;
            background-color: #ffffff;
            color: #111827;
            font-weight: 700;
            padding: 0.55rem 1rem;
        }

        [data-testid="stMetric"] {
            background-color: #ffffff;
            border: 1px solid #e5e7eb;
            padding: 1rem;
            border-radius: 16px;
            box-shadow: 0 8px 20px rgba(15, 23, 42, 0.04);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )