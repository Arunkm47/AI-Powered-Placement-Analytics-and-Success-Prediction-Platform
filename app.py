import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CareerLens",
    page_icon="🎯",
    layout="wide"
)

df = pd.read_csv("student_placement_career_success_dataset_2026.csv")

st.title("🎯 CareerLens")
st.subheader("AI-Powered Placement Analytics & Career Success Platform")

col1, col2, col3, col4 = st.columns(4)

placement_rate = (
    (df["Placement_Status"] == "Placed").mean() * 100
)

col1.metric("Students", len(df))
col2.metric("Placement Rate", f"{placement_rate:.1f}%")
col3.metric("Average Salary", f"{df['Salary_LPA'].mean():.2f} LPA")
col4.metric("Highest Salary", f"{df['Salary_LPA'].max():.2f} LPA")
