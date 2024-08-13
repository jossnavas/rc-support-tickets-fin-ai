import streamlit as st
import pandas as pd

# Set page layout
st.set_page_config(layout="wide")

# Centered logo and title
st.markdown("<div style='text-align: center;'><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRx1eoyIn1KclLg8BeRImrb58PyIXqnh1WesQ&s' width='150'/></div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Question and Answer Table</h1>", unsafe_allow_html=True)

# Initialize session state for input fields and table data
if "table_data" not in st.session_state:
    st.session_state.table_data = []
if "question_input" not in st.session_state:
    st.session_state.question_input = ""
if "answer_input" not in st.session_state:
    st.session_state.answer_input = ""

# Input fields with limited width
input_col1, input_col2, input_col3 = st.columns([1, 2, 1])
with input_col2:
    date_input = st.date_input("Date")
    question_input = st.text_area("Question", height=100, value=st.session_state.question_input, key="question_input", help="Enter your question here.")
    answer_input = st.text_area("Answer", height=150, value=st.session_state.answer_input, key="answer_input", help="Enter the answer here.")
