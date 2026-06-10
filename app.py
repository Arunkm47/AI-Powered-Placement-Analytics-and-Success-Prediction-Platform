import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="CareerLens",
    page_icon="🎯",
    layout="wide"
)

# Load Data
df = pd.read_csv("student_placement_career_success_dataset_2026.csv")

# Sidebar Filters
st.sidebar.header("Filters")

tier = st.sidebar.multiselect(
    "College Tier",
    df["College_Tier"].unique(),
    default=df["College_Tier"].unique()
)

spec = st.sidebar.multiselect(
    "Specialization",
    df["Specialization"].unique(),
    default=df["Specialization"].unique()
)

filtered_df = df[
    (df["College_Tier"].isin(tier)) &
    (df["Specialization"].isin(spec))
]

# Title
st.title("🎯 CareerLens")
st.subheader("AI-Powered Placement Analytics & Career Success Platform")

# KPIs
placement_rate = (
    (filtered_df["Placement_Status"] == "Placed").mean() * 100
)

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("Students", len(filtered_df))
col2.metric("Placement Rate", f"{placement_rate:.1f}%")
col3.metric("Average Salary", f"{filtered_df['Salary_LPA'].mean():.2f} LPA")
col4.metric("Highest Salary", f"{filtered_df['Salary_LPA'].max():.2f} LPA")
col5.metric("Average CGPA", round(filtered_df["CGPA"].mean(), 2))
col6.metric("Average Internships", round(filtered_df["Internships"].mean(), 2))

st.markdown("---")

# Row 1
col1, col2 = st.columns(2)

with col1:
    fig = px.histogram(
        filtered_df,
        x="CGPA",
        nbins=20,
        title="CGPA Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.histogram(
        filtered_df,
        x="Salary_LPA",
        nbins=20,
        title="Salary Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

# Row 2
col1, col2 = st.columns(2)

with col1:
    fig = px.box(
        filtered_df,
        x="Placement_Status",
        y="CGPA",
        title="CGPA vs Placement"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.scatter(
        filtered_df,
        x="Internships",
        y="Salary_LPA",
        color="Placement_Status",
        title="Internships vs Salary"
    )
    st.plotly_chart(fig, use_container_width=True)
