import streamlit as st
import requests

#GLASS UI CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    color: white;
}
.glass-card {
    background: rgba(255,255,255,0.1);
    border-radius: 15px;
    padding: 25px;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-top: 20px;
    text-align: center;
}
h1, h2, h3 {
    text-align: center;
    color: white;
}
.stButton>button {
    background: linear-gradient(45deg, #ff4b2b, ##ff416c);
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

#TITLE
st.title("Diabetes Prediction System")
st.markdown("### AI-Powered Multi-Stage Diagnosis")

#INPUTS
gender = st.selectbox("Gender", ["Male","Female"])
ethnicity = st.selectbox("Ethenicity", ["Asian","White","Black","Other"])
education_level = st.selectbox("Education Level",["Highschool","Bachelors","Masters","PhD"])
income_level = st.selectbox("Income Level", ["Low","Middle","High"])
employment_status = st.selectbox("Employment Status", ["Employed","Unemployed"])
smoking_status = st.selectbox("Smoking Status", ["Never","Former","Current"])

alcohol = st.number_input("Alcohol per week", 0, 20, 1)
physical_activity = st.number_input("Physical activity", 0, 12, 5)
diet_score = st.slider("Diet score", 0, 10, 5)
sleep_hours = st.slider("Sleep hours", 0, 12, 7)
screen_time = st.slider("Screen time (hours/day)", 0, 12, 5)

family_history = st.selectbox("Family history diabetes", [0, 1])
hypertension = st.selectbox("Hypertension history", [0, 1])
cardio = st.selectbox("Cardiovascular history", [0, 1])

waist_hip = st.number_input("Waist to hip ratio", 0.5, 2.0, 0.9)
heart_rate = st.number_input("Heart rate", 40, 200, 75)
cholesterol = st.number_input("Cholesterol total", 40, 200, 75)
triglycerides = st.number_input("Triglycerides", 50, 500, 150)
glucose = st.number_input("Glucose postprandial", 0, 100, 15)
insulin = st.number_input("Insulin level", 0, 100, 15)
hba1c = st.number_input("HbA1c", 3.0, 15.0, 6.5)

risk_score = st.slider("Diabetes risk score", 0.0, 100.0, 50.0)

stage = st.selectbox("Diabetes stage", ["No Diabetes, Prediabtes", "Type1", "Type2"])
bmi = st.selectbox("BMI category", ["Underweight", "Normal", "Overweight", "Obese"])
age_group = st.selectbox("Age Group", ["Normal", "Middle-aged","Old"])
glucose_cat = st.selectbox("Glucose category", ["Normal", "Prediabetic", "Diabetes"])
high_bp = st.selectbox("High BP", [0, 1])

chol_ratio = st.number_input("Cholestrol ratio", 1.0, 10.0, 3.5)
lifestyle_score = st.slider("Lifestyle risk score", 0.0, 1.0, 0.4)

#BUTTON
if st.button("🚀 Predict"):

    data = {
        "gender": gender,
        "ethnicity": ethnicity,
        "education_level": education_level,
        "income_level": income_level,
        "employment_status": employment_status,
        "smoking_status": smoking_status,
        "alcohol_consumption_per_week": alcohol,
        "physical_activity_minutes_per_week": physical_activity,
        "diet_score": diet_score,
        "sleep_hours_per_day": sleep_hours,
        "screen_time_hours_per_day": screen_time,
        "family_history_diabetes": family_history,
        "hypertension_history": hypertension,
        "cardiovascular_history": cardio,
        "waist_to_hip_ratio": waist_hip,
        "heart_rate": heart_rate,
        "cholesterol_total": cholesterol,
        "triglycerides": triglycerides,
        "glucose_postprandial": glucose,
        "insulin_level": insulin,
        "hba1c": hba1c,
        "diabetes_risk_score": risk_score,
        "diabetes_stage": stage,
        "bmi_category": bmi,
        "age_group": age_group,
        "glucose_category": glucose_cat,
        "high_bp": high_bp,
        "cholesterol_ratio": chol_ratio,
        "lifestyle_risk_score": lifestyle_score
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=data)

        if response.status_code == 200:
            result = response.json()

            if result["diabetic"] == 1:
                status = "⚠️ Diabetic"
            else:
                status = "✅ Not Diabetic"

            st.markdown(f"""
            <div class="glass-card">
                <h2>📊 Risk Score: {result['risk_score']:.2f}</h2>
                <h3>🎯 Confidence: {result['confidence']*100:.2f}%</h3>
                <h2>{status}</h2>
                <h3>🩺 Stage: {result['stage']}</h3>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.error("API Error")

    except Exception as e:
        st.error(f"Connection Error: {e}")