import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("mental_health_model.pkl")

# Page Config
st.set_page_config(
    page_title="Student Mental Health Risk Detection",
    page_icon="🎓",
    layout="wide"
)

# Title
st.title("🎓 Student Mental Health Risk Detection")

st.markdown("""
This application predicts the **mental health risk level** of students
based on academic, lifestyle, and psychological factors.
""")

# Sidebar
st.sidebar.title("📌 About Project")

st.sidebar.info("""
This project uses Machine Learning to analyze:
- Academic factors
- Lifestyle habits
- Psychological indicators

and predicts student mental health risk.
""")

st.sidebar.markdown("---")
st.sidebar.write("Built using:")
st.sidebar.write("• Python")
st.sidebar.write("• Scikit-Learn")
st.sidebar.write("• Streamlit")

# Layout
col1, col2, col3 = st.columns(3)

# Column 1
with col1:

    st.subheader("📚 Academic Factors")

    age = st.number_input("Age", 16, 35, 20)

    year_of_study = st.selectbox(
        "Year of Study",
        [1, 2, 3, 4]
    )

    cgpa = st.slider("CGPA", 1.0, 10.0, 7.0)

    attendance = st.slider(
        "Attendance Percentage",
        0,
        100,
        75
    )

    study_hours = st.slider(
        "Daily Study Hours",
        0,
        24,
        4
    )

    academic_pressure = st.slider(
        "Academic Pressure",
        1,
        10,
        5
    )

    backlogs = st.slider(
        "Number of Backlogs",
        0,
        10,
        0
    )

# Column 2
with col2:

    st.subheader("🌿 Lifestyle Factors")

    sleep_hours = st.slider(
        "Sleep Hours",
        0,
        12,
        7
    )

    screen_time = st.slider(
        "Daily Screen Time",
        0,
        15,
        5
    )

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

# Column 3
with col3:

    st.subheader("🧠 Psychological Factors")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    stress_level = st.slider(
        "Stress Level",
        1,
        10,
        5,
        help="1 = Very Low Stress, 10 = Extremely High Stress"
    )

    anxiety_level = st.slider(
        "Anxiety Level",
        1,
        10,
        5
    )

    mood_rating = st.slider(
        "Mood Rating",
        1,
        10,
        5
    )

    loneliness = st.slider(
        "Loneliness Level",
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

# Gender Encoding
gender_map = {
    "Male": 0,
    "Female": 1,
    "Other": 2
}

gender = gender_map[gender]

# Create Input DataFrame
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

# Analysis Scores
mental_risk = (
    stress_level +
    anxiety_level +
    (10 - mood_rating) +
    loneliness
)

mental_risk_percent = (mental_risk / 40) * 100

lifestyle_score = (
    sleep_hours +
    physical_activity_time +
    (10 - screen_time)
)

lifestyle_percent = (lifestyle_score / 32) * 100

academic_score = (
    academic_pressure +
    backlogs +
    (10 - motivation_level)
)

academic_percent = (academic_score / 30) * 100

social_score = (
    family_support +
    social_interaction +
    (10 - peer_pressure)
)

social_percent = (social_score / 30) * 100

# Prediction
if st.button("🔍 Predict Mental Health Risk"):

    prediction = model.predict(input_data)[0]

    st.markdown("---")

    st.subheader("📊 Analysis Report")

    st.write("🧠 Mental Risk")
    st.progress(int(mental_risk_percent))
    st.write(f"{mental_risk_percent:.1f}%")

    st.write("🌿 Lifestyle Health")
    st.progress(int(lifestyle_percent))
    st.write(f"{lifestyle_percent:.1f}%")

    st.write("📚 Academic Pressure")
    st.progress(int(academic_percent))
    st.write(f"{academic_percent:.1f}%")

    st.write("🤝 Social Wellbeing")
    st.progress(int(social_percent))
    st.write(f"{social_percent:.1f}%")

    st.markdown("---")

    if prediction == 0:
        st.success("🟢 Low Mental Health Risk")

    elif prediction == 1:
        st.warning("🟡 Medium Mental Health Risk")

    else:
        st.error("🔴 High Mental Health Risk")

    # Recommendations
    st.subheader("💡 Recommendations")

    if mental_risk_percent > 70:
        st.info("Consider reducing stress and improving emotional wellbeing.")

    if sleep_hours < 5:
        st.info("Try maintaining a healthier sleep schedule.")

    if screen_time > 10:
        st.info("Reducing screen time may improve mental wellbeing.")

    if physical_activity_time < 1:
        st.info("Regular physical activity can improve mental health.")

# Footer
st.markdown("---")
st.caption("Built using Machine Learning and Streamlit")
