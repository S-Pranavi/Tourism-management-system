import datetime
import pandas as pd
import streamlit as st
from database import view_all_data, view_only_package_names, get_package, edit_package_data
from datetime import date, timedelta

def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['PackageId','PackageName','PackageType','PackageLocation','PackagePrice','PackageFeatures','PackageDetails','PackageImage','NumberOfDays','Creationdate'])
    with st.expander("Current packages"):
        st.dataframe(df)
    list_of_packages = [i[0] for i in view_only_package_names()]
    selected_package = st.selectbox("Package to Edit", list_of_packages)
    selected_result = get_package(selected_package)
    # st.write(selected_result)
    if selected_result:
        PackageId=selected_result[0][0]
        PackageName=selected_result[0][1]
        PackageType=selected_result[0][2]
        PackageLocation=selected_result[0][3]
        PackagePrice=selected_result[0][4]
        PackageFeatures=selected_result[0][5]
        PackageDetails=selected_result[0][6]
        PackageImage=selected_result[0][7]
        NumberOfDays=selected_result[0][8]
        Creationdate=selected_result[0][9]
       

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_PackageId= st.text_input("PackageId:", PackageId)
            new_PackageName=st.text_input("PackageName:", PackageName)
        with col2:
            new_PackageLocation= st.text_input("PackageLocation:", PackageLocation)
            new_PackagePrice= st.text_input("PackagePrice",PackagePrice)  
        new_NumberOfDays=st.text_input("NumberOfDays:",NumberOfDays)
        new_PackageType= st.selectbox(PackageType, ["Couple", "Family", "Religious"])
        new_PackageFeatures= st.text_input("PackageFeatures:",PackageFeatures)
        new_PackageDetails=st.text_input("PackageDetails",PackageDetails)
        new_PackageImage=st.text_input("PackageImage",PackageImage)
        new_Creationdate=st.text_input("Creationdate:",Creationdate)
        if st.button("Update Packages"):
            edit_package_data(new_PackageId,new_PackageName,new_PackageType,new_PackageLocation,new_PackagePrice,new_PackageFeatures,new_PackageDetails,new_PackageImage,new_NumberOfDays,new_Creationdate,PackageId,PackageName,PackageType,PackageLocation,PackagePrice,PackageFeatures,PackageDetails,PackageImage,NumberOfDays,Creationdate)
            st.success("Successfully updated:: {} to ::{}".format(PackageName, new_PackageName))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['PackageId','PackageName','PackageType','PackageLocation','PackagePrice','PackageFeatures','PackageDetails','PackageImage','NumberOfDays','Creationdate'])
    with st.expander("Updated data"):
        st.dataframe(df2)