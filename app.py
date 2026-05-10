import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("mental_health_model.pkl")

# App title
st.title("🎓 Student Mental Health Risk Detection")

st.write("""
This application predicts the mental health risk level of students
based on academic, lifestyle, and psychological factors.
""")

# User Inputs
age = st.number_input("Age", 16, 35, 20)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

year_of_study = st.selectbox(
    "Year of Study",
    [1, 2, 3, 4]
)

cgpa = st.slider("CGPA", 1.0, 10.0, 7.0)

attendance = st.slider("Attendance Percentage", 0, 100, 75)

study_hours = st.slider("Daily Study Hours", 0, 24, 4)

sleep_hours = st.slider("Sleep Hours", 0, 12, 7)

screen_time = st.slider("Daily Screen Time", 0, 15, 5)

physical_activity_time = st.slider(
    "Physical Activity Hours",
    0,
    10,
    1
)

social_interaction = st.slider(
    "Social Interaction Level",
    1,
    10,
    5
)

stress_level = st.slider("Stress Level", 1, 10, 5)

anxiety_level = st.slider("Anxiety Level", 1, 10, 5)

mood_rating = st.slider("Mood Rating", 1, 10, 5)

loneliness = st.slider("Loneliness Level", 1, 10, 5)

academic_pressure = st.slider(
    "Academic Pressure",
    1,
    10,
    5
)

motivation_level = st.slider(
    "Motivation Level",
    1,
    10,
    5
)

family_support = st.slider(
    "Family Support",
    1,
    10,
    5
)

peer_pressure = st.slider(
    "Peer Pressure",
    1,
    10,
    5
)

backlogs = st.slider("Number of Backlogs", 0, 10, 0)

# Gender Encoding
gender_map = {
    "Male": 0,
    "Female": 1,
    "Other": 2
}

gender = gender_map[gender]

input_data = pd.DataFrame([[
    age,
    gender,
    year_of_study,
    cgpa,
    attendance,
    study_hours,
    backlogs,
    academic_pressure,
    sleep_hours,
    screen_time,
    physical_activity_time,
    social_interaction,
    family_support,
    peer_pressure,
    stress_level,
    anxiety_level,
    mood_rating,
    loneliness,
    motivation_level
]], columns=[
    'age',
    'gender',
    'year_of_study',
    'cgpa',
    'attendance',
    'study_hours',
    'backlogs',
    'academic_pressure',
    'sleep_hours',
    'screen_time',
    'physical_activity_time',
    'social_interaction',
    'family_support',
    'peer_pressure',
    'stress_level',
    'anxiety_level',
    'mood_rating',
    'loneliness',
    'motivation_level'
])

# Prediction
if st.button("Predict Mental Health Risk"):

    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.success("🟢 Low Mental Health Risk")

    elif prediction == 1:
        st.warning("🟡 Medium Mental Health Risk")

    else:
        st.error("🔴 High Mental Health Risk")