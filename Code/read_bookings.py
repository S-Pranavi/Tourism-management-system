import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_bookings
from datetime import date, timedelta

def read_bookings():
    result = view_all_bookings()
    # st.write(result)
    df = pd.DataFrame(result, columns=['BookingId','PackageId','UserId','Class','NumberOfPersons'])
    with st.expander("View all Bookings"):
        st.dataframe(df)
    with st.expander("Number of bookings"):
        task_df = df['PackageId'].value_counts().to_frame()
        task_df = task_df.reset_index()
        st.dataframe(task_df)
        p2 = px.pie(task_df, names='index', values='PackageId')
        st.plotly_chart(p2)