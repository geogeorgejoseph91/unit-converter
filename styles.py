import streamlit as st

brand_color = '#1b5a9d'

def css_styles():
    st.markdown(
        f"""
        <style>
        body .main-title {{
            text-align: left;
            color: {brand_color};
            font-size: 60px;
            font-weight: 500;
            border-bottom: 1px solid #dbdbdb;
            margin-bottom: 50px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )