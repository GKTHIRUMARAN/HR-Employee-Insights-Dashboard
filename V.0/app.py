# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ---------------------------
# App Config
# ---------------------------
st.set_page_config(page_title="HR Employee Insights Dashboard", layout="wide")
st.title("📊 HR Employee Insights Dashboard")
st.write("Upload, explore, and analyze HR datasets with flexible mapping and instant KPIs.")

DATA_FILE = "Day 1-HR-Employee-Attrition.csv"

# ---------------------------
# Helper Functions
# ---------------------------
@st.cache_data
def load_data(file_path=DATA_FILE):
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame()
    return df

def save_data(df, file_path=DATA_FILE):
    df.to_csv(file_path, index=False)

def get_required_columns():
    return [
        'Age','Attrition','Department','JobRole','JobLevel','MonthlyIncome',
        'OverTime','YearsAtCompany','JobSatisfaction','EnvironmentSatisfaction',
        'PerformanceRating','WorkLifeBalance','Gender','MaritalStatus','EducationField'
    ]

# ---------------------------
# Load Initial Data
# ---------------------------
df = load_data()

# ---------------------------
# Sidebar: Data Management
# ---------------------------
st.sidebar.header("⚙️ Data Management")

uploaded_file = st.sidebar.file_uploader("Upload Employee Data (CSV)", type=["csv"])
clear_data = st.sidebar.button("🗑️ Clear Dataset (Reset)")

# Clear dataset
if clear_data:
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    df = pd.DataFrame()
    st.sidebar.warning("Dataset cleared. Upload a new CSV to start fresh.")

# Handle file upload with column mapping
if uploaded_file is not None:
    temp_df = pd.read_csv(uploaded_file)
    required_cols = get_required_columns()

    st.sidebar.subheader("📝 Column Mapping")
    mapping = {}
    for req in required_cols:
        # Dropdown lets user map their column to required schema
        mapping[req] = st.sidebar.selectbox(
            f"Map to '{req}'", options=["--None--"] + list(temp_df.columns), index=0
        )

    if st.sidebar.button("✅ Apply Mapping & Save"):
        # Rename columns based on mapping
        rename_dict = {v: k for k, v in mapping.items() if v != "--None--"}
        temp_df = temp_df.rename(columns=rename_dict)

        # Ensure all required columns exist
        for col in required_cols:
            if col not in temp_df.columns:
                temp_df[col] = pd.NA

        # Decide if we are replacing or merging
        if df.empty:
            df = temp_df[required_cols]
        else:
            df = pd.concat([df, temp_df[required_cols]], ignore_index=True)

        save_data(df)
        st.sidebar.success("✅ Data uploaded & saved successfully!")

# ---------------------------
# Stop if no data
# ---------------------------
if df.empty:
    st.info("No data available. Please upload a dataset to get started.")
    st.stop()

# ---------------------------
# Step 1: KPIs
# ---------------------------
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)

total_emp = df.shape[0]
attrition_rate = df['Attrition'].value_counts(normalize=True).get('Yes', 0) * 100
avg_income = df['MonthlyIncome'].mean()

col1.metric("Total Employees", total_emp)
col2.metric("Attrition Rate (%)", round(attrition_rate, 2))
col3.metric("Avg Monthly Income", f"${round(avg_income,0)}")

# ---------------------------
# Step 2: Sidebar Filters
# ---------------------------
st.sidebar.header("🔍 Filters")
department = st.sidebar.multiselect("Department", df['Department'].dropna().unique())
gender = st.sidebar.multiselect("Gender", df['Gender'].dropna().unique())

df_filtered = df.copy()
if department:
    df_filtered = df_filtered[df_filtered['Department'].isin(department)]
if gender:
    df_filtered = df_filtered[df_filtered['Gender'].isin(gender)]

# ---------------------------
# Step 3: Tabs for Navigation
# ---------------------------
tab1, tab2, tab3, tab4 = st.tabs(["📌 Overview", "📉 Attrition", "😊 Satisfaction", "📂 Data Access"])

# --- Overview ---
with tab1:
    st.subheader("Workforce Overview")
    fig = px.histogram(df_filtered, x="Department", color="Gender", barmode="group", title="Employees by Department & Gender")
    st.plotly_chart(fig, use_container_width=True)

    fig = px.box(df_filtered, x="Department", y="MonthlyIncome", color="Attrition", title="Income Distribution by Department & Attrition")
    st.plotly_chart(fig, use_container_width=True)

# --- Attrition ---
with tab2:
    st.subheader("Attrition Analysis")
    fig1 = px.bar(df_filtered, x="Department", color="Attrition", title="Attrition by Department")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.bar(df_filtered, x="JobRole", color="Attrition", title="Attrition by Job Role")
    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.histogram(df_filtered, x="Age", color="Attrition", nbins=20, title="Attrition by Age")
    st.plotly_chart(fig3, use_container_width=True)

    fig4 = px.box(df_filtered, x="Attrition", y="MonthlyIncome", title="Monthly Income vs Attrition")
    st.plotly_chart(fig4, use_container_width=True)

# --- Satisfaction ---
with tab3:
    st.subheader("Employee Satisfaction & Work-Life Balance")
    fig5 = px.histogram(df_filtered, x="JobSatisfaction", color="Attrition", barmode="group", title="Job Satisfaction vs Attrition")
    st.plotly_chart(fig5, use_container_width=True)

    fig6 = px.histogram(df_filtered, x="WorkLifeBalance", color="Attrition", barmode="group", title="Work-Life Balance vs Attrition")
    st.plotly_chart(fig6, use_container_width=True)

    fig7 = px.histogram(df_filtered, x="EnvironmentSatisfaction", color="Attrition", barmode="group", title="Environment Satisfaction vs Attrition")
    st.plotly_chart(fig7, use_container_width=True)

# --- Data Access ---
with tab4:
    st.subheader("Filtered Data Access")

    if st.checkbox("Show Filtered Data"):
        st.dataframe(df_filtered)

    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Current View as CSV",
        data=csv,
        file_name="HR_filtered_data.csv",
        mime="text/csv",
    )
