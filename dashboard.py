import streamlit as st
import pandas as pd

df = pd.read_csv("student_placement_career_success_dataset_2026.csv")

st.title("Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Students", len(df))
col2.metric("Placement Rate",
            f"{(df['Placement_Status'].value_counts(normalize=True).max()*100):.1f}%")

col3.metric("Average Salary",
            round(df["Salary_LPA"].mean(),2))

col4.metric("Highest Salary",
            round(df["Salary_LPA"].max(),2))
