import pandas as pd
import streamlit as st
from database import view_all_data, view_only_package_names, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['PackageId','PackageName','PackageType','PackageLocation','PackagePrice','PackageFeatures','PackageDetails','PackageImage','NumberOfDays','Creationdate'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_packages = [i[0] for i in view_only_package_names()]
    selected_package = st.selectbox("Task to Delete", list_of_packages)
    st.warning("Do you want to delete ::{}".format(selected_package))
    if st.button("Delete package"):
        delete_data(selected_package)
        st.success("Package has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['PackageId','PackageName','PackageType','PackageLocation','PackagePrice','PackageFeatures','PackageDetails','PackageImage','NumberOfDays','Creationdate'])
    with st.expander("Updated data"):
        st.dataframe(df2)