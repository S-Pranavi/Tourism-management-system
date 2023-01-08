import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data
from datetime import date, timedelta

def read():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['PackageId','PackageName','PackageType','PackageLocation','PackagePrice','PackageFeatures','PackageDetails','PackageImage','NumberOfDays','Creationdate'])
    with st.expander("View all Packages"):
        st.dataframe(df)
    with st.expander("Types of packages"):
        task_df = df['PackageType'].value_counts().to_frame()
        task_df = task_df.reset_index()
        st.dataframe(task_df)
        p1 = px.pie(task_df, names='index', values='PackageType')
        st.plotly_chart(p1)