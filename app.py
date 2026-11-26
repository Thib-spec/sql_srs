import streamlit as st
import pandas as pd
import duckdb as duckdb

st.write("""
# SQL CRS
Space Repetition System SQL Practice
""")

option = st.selectbox(
    "What would you like to review",
    ["Joins","Group by","Windows Function"],
    index=None,
    placeholder="Select a theme"
)

st.write('You selected:', option)

data = {"a":[1,2,3], "b":[4,5,6]}
df = pd.DataFrame(data)

tab1,tab2,tab3 = st.tabs(['cat','dog','owl'])

with tab1:
    st.header("Cat")
    input_text = st.text_area(label="Enter your query")
    st.write(f"Vous avez entrez la requête {input_text}")
    query = duckdb.sql(input_text).df()
    #st.write(input_text)
    st.dataframe(query)