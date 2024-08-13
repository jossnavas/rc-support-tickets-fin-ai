import streamlit as st
import pandas as pd

# Set page layout
st.set_page_config(layout="wide")

# Centered logo and title
st.markdown("<div style='text-align: center;'><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRx1eoyIn1KclLg8BeRImrb58PyIXqnh1WesQ&s' width='150'/></div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Question and Answer Table</h1>", unsafe_allow_html=True)

# Initialize the session state for storing table data
if "table_data" not in st.session_state:
    st.session_state.table_data = []

# Input fields with limited width
input_col1, input_col2, input_col3 = st.columns([1, 2, 1])
with input_col2:
    date_input = st.date_input("Date")
    question_input = st.text_area("Question", height=100, key="question_input", help="Enter your question here.")
    answer_input = st.text_area("Answer", height=150, key="answer_input", help="Enter the answer here.")
    
    # Centered "Add to Table" button
    if st.button("Add to Table"):
        # Append the new entry to the session state table data
        st.session_state.table_data.append({
            "Date": date_input,
            "Question": question_input,
            "Answer": answer_input
        })

# Centered output table and clear button
if st.session_state.table_data:
    output_col1, output_col2, output_col3 = st.columns([1, 2, 1])
    with output_col2:
        df = pd.DataFrame(st.session_state.table_data)
        st.write("### Table of Entries")
        st.dataframe(df)

        # Button to clear table contents
        if st.button("Clear Table"):
            # Clear the table data
            st.session_state.table_data = []
            st.success("Table contents cleared.")
