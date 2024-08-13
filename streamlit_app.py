import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets credentials and open the sheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet (you can use sheet name or URL)
sheet = client.open("Your Google Sheet Name").sheet1

# Set page layout
st.set_page_config(layout="wide")

# Centered logo and title
st.markdown("<div style='text-align: center;'><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRx1eoyIn1KclLg8BeRImrb58PyIXqnh1WesQ&s' width='150'/></div>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Question and Answer Table</h1>", unsafe_allow_html=True)

# Input fields with limited width
input_col1, input_col2, input_col3 = st.columns([1, 2, 1])
with input_col2:
    date_input = st.date_input("Date")
    question_input = st.text_area("Question", height=100, help="Enter your question here.")
    answer_input = st.text_area("Answer", height=150, help="Enter the answer here.")
    
    # Centered "Add to Table" button
    if st.button("Add to Table"):
        # Add the data to Google Sheets
        sheet.append_row([str(date_input), question_input, answer_input])
        st.success("Row added to the global table!")

# Fetch and display the global data from Google Sheets
data = sheet.get_all_records()
if data:
    df = pd.DataFrame(data)
    output_col1, output_col2, output_col3 = st.columns([1, 2, 1])
    with output_col2:
        st.write("### Global Table of Entries")
        st.dataframe(df)
