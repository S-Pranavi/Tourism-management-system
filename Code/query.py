import streamlit as st
import pandas as pd
from database import view_all


def read_all(query):
    result=view_all(query)
    df=pd.DataFrame(result[2],columns=result[1])
    st.table(df)

def query():
    query=st.text_input("Enter query:")
    if st.button("Query"):
        read_all(query)

