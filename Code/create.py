import streamlit as st
from database import add_data
from datetime import date, timedelta

def create():
    col1, col2 = st.columns(2)
    with col1:
        PackageId= st.text_input("PackageId:")
        PackageName = st.text_input("PackageName:")
    with col2:
        PackageLocation= st.text_input("PackageLocation:")
        PackagePrice= st.text_input("PackagePrice:")
    NumberOfDays=st.text_input("NumberOfDays:")
    PackageType= st.selectbox("PackageType", ["Couple", "Family", "Religious"])
    PackageFeatures= st.text_input("PackageFeatures:")
    PackageDetails=st.text_input("PackageDetails")
    PackageImage=st.text_input("PackageImage")
    Creationdate=st.text_input("Creationdate:")
    if st.button("Add Package"):
        add_data(PackageId,PackageName,PackageType,PackageLocation,PackagePrice,PackageFeatures,PackageDetails,PackageImage,NumberOfDays,Creationdate)
        st.success("Successfully added Package: {}".format(PackageName))