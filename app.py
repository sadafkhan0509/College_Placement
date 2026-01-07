import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="College Placement Salary Predictor",
    page_icon="💼",
    layout="centered"
)

# -----------------------------
# Load trained pipeline model
# -----------------------------
@st.cache_resource
def load_model():
    with open("salary_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# -----------------------------
# Helper function
# -----------------------------
def to_float(value):
    """
    Converts empty string to None, else to float
    """
    if value is None:
        return None
    value = str(value).strip()
    return float(value) if value != "" else None

# -----------------------------
# UI Header
# -----------------------------
st.title("💼 Salary Prediction App")
st.caption("Predict expected salary based on academic and personal details")
st.info("ℹ️ All fields are optional. You may leave any field empty.")

st.divider()

# -----------------------------
# Input layout
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    cgpa = st.text_input("CGPA (0–10)")
    iq = st.text_input("IQ (70-145)")
    experience = st.text_input("Years of Experience")

with col2:
    dependents = st.text_input("Number of Dependents")
    expenses = st.text_input("Monthly Expenses (INR)")

gender = st.selectbox("Gender", ["", "Male", "Female"])
marital_status = st.selectbox("Marital Status", ["", "Single", "Married"])

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict Salary"):

    input_data = pd.DataFrame([{
        "CGPA": to_float(cgpa),
        "IQ": to_float(iq),
        "Year_of_Experience": to_float(experience),
        "Dependents": to_float(dependents),
        "Expenses": to_float(expenses),
        "Gender": gender if gender != "" else None,
        "Marital_Status": marital_status if marital_status != "" else None
    }])

    with st.spinner("Predicting salary..."):
        prediction = model.predict(input_data)[0]
        

     # Prevent negative salary
        prediction = max(prediction, 0)


    st.success(f"💰 Estimated Salary: ₹ {prediction:,.0f} per month")

    st.balloons()
