import streamlit as st
from conversions import ALL_CATEGORIES, convert, get_units_for_category
import pandas as pd
import numpy as np

from styles import *

st.set_page_config(
    page_title="Unit Converter",
    page_icon="",
    layout="centered",
    initial_sidebar_state="expanded"
)

css_styles()

# sidebar

# ---------------------------------------------------------------------------
# SIDEBAR - quick info
# ---------------------------------------------------------------------------
with st.sidebar:
    st.subheader("About")
    st.write(
        "This Unit Converter supports 9 categories with 60+ units total."
    )
    st.divider()
    st.subheader("Categories")
    with st.container(key="sidebar_menu"):
      st.markdown('<div class="sidebar-links">', unsafe_allow_html=True)
      selected_category = st.radio(
          "Choose Category",
          ALL_CATEGORIES
      )
      st.markdown('</div>', unsafe_allow_html=True)
    st.divider()
    st.caption("Built with Python + Streamlit")


# MAIN PAGE
st.markdown(
    "<h1 class='main-title'>Unit Converter</h1>",
    unsafe_allow_html=True
)
# Dynamic subtitle
st.subheader(f"{selected_category} Converter")

units = get_units_for_category(selected_category)


col1, col2 = st.columns(2)

with col1:
    st.subheader("From")
    from_unit = st.selectbox(
        "From unit:", units, key="from_unit", label_visibility="collapsed"
    )
    value = st.number_input(
        "Enter value:", value=1.0, format="%.6f", key="value"
    )

with col2:
    st.subheader("To")
    # Default the "to" dropdown to the second unit (so it differs from "from")
    default_to_index = 1 if len(units) > 1 else 0
    to_unit = st.selectbox(
        "To unit:",
        units,
        index=default_to_index,
        key="to_unit",
        label_visibility="collapsed",
    )

result = convert(value, from_unit, to_unit, selected_category)    

if result is not None:
    st.divider()
    st.markdown(
        f"### {value:g} {from_unit}  =  **{result:g} {to_unit}**"
    )  