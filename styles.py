import streamlit as st

brand_color = '#1b5a9d'

def css_styles():
    st.markdown(
        f"""
        <style>
        body .main-title {{
            text-align: left;
            color: {brand_color};
            font-size: 48px;
            font-weight: 500;
            border-bottom: 1px solid #dbdbdb;
            margin-bottom: 50px;
        }}
        .st-key-sidebar_menu label input:checked+*{{
          color: {brand_color};
        }}
        .st-key-sidebar_menu div[role="radiogroup"] > label{{
          padding:5px 0;
        }}
         .st-key-sidebar_menu div[role="radiogroup"] > label:hover input+*{{
          color: {brand_color};
         }}
        </style>
        """,
        unsafe_allow_html=True
    )