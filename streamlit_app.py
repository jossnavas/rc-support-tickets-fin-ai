import streamlit as st
import pandas as pd

# Include your logo at the top right using the image URL
st.set_page_config(layout="wide")
col1, col2 = st.columns([4, 1])
with col1:
    st.title("Question and Answer Table")
with col2:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRx1eoyIn1KclLg8BeRImrb58PyIXqnh1WesQ&s", width=150)

# Initialize the session state for storing table data
if "table_data" not in st.session_state:
    st.session_state.table_data = []

# Input fields with limited width
input_col1, input_col2, input_col3 = st.columns([1, 2, 1])
with input_col2:
    date_input = st.date_input("Date")
    question_input = st.text_area("Question", height=100, key="question_input", help="Enter your question here.")
    answer_input = st.text_area("Answer", height=150, key="answer_input", help="Enter the answer here.")

# Button to add the input to the table
if st.button("Add to Table"):
    # Append the new entry to the session state table data
    st.session_state.table_data.append({
        "Date": date_input,
        "Question": question_input,
        "Answer": answer_input
    })

# Display the table
if st.session_state.table_data:
    df = pd.DataFrame(st.session_state.table_data)
    st.write("### Table of Entries")
    st.dataframe(df)
