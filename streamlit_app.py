import streamlit as st
import pandas as pd

# Initialize the session state for storing table data
if "table_data" not in st.session_state:
    st.session_state.table_data = []

# App title
st.title("Question and Answer Table")

# Input fields
date_input = st.date_input("Date")
question_input = st.text_input("Question")
answer_input = st.text_area("Answer")

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
