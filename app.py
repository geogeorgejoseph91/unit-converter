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

# MAIN PAGE
st.markdown(
    "<h1 class='main-title'>Unit Converter</h1>",
    unsafe_allow_html=True
)

with st.container(border=True,key="form-container"):

  category_col, = st.columns(1)
  with category_col:
      st.markdown("<strong>Category</strong>", unsafe_allow_html=True)
      selected_category = st.selectbox(
          "From unit:", ALL_CATEGORIES, key="category", label_visibility="collapsed"
      )

  units = get_units_for_category(selected_category)

  col1, col2 = st.columns(2)
  with col1:
      st.markdown("<strong>From</strong>", unsafe_allow_html=True)
      from_unit = st.selectbox(
          "From unit:", units, key="from_unit", label_visibility="collapsed"
      )

  with col2:
      st.markdown("<strong>To</strong>", unsafe_allow_html=True)
      # Default the "to" dropdown to the second unit (so it differs from "from")
      default_to_index = 1 if len(units) > 1 else 0
      to_unit = st.selectbox(
          "To unit:",
          units,
          index=default_to_index,
          key="to_unit",
          label_visibility="collapsed",
      )

  col3, = st.columns(1)

  with col3:
      st.markdown("<strong>Enter value</strong>", unsafe_allow_html=True)
      value = st.number_input(
          "", value=1.0, format="%.6f", key="value",label_visibility="collapsed"
      )

  result = convert(value, from_unit, to_unit, selected_category)   

  if result is not None:
      st.markdown(
          f"**{value:g} {from_unit}  =  {result:g} {to_unit}**"
      )  