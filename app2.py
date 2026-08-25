import streamlit as st

st.set_page_config(
    page_title="Welcome to Student Grade Analyzer",
    page_icon="🎓",
    layout="centered"
)

st.title("Student Grade Analyzer")
st.caption("Streamlit Demo")

st.divider()

name = st.text_input("Student name")

python_score = st.slider("Python", 0, 100, 50)
cloud_score = st.slider("Cloud Computing", 0, 100, 70)
database_score = st.slider("Databases", 0, 100, 70)

scores = {
    "Python": python_score,
    "Cloud Computing": cloud_score,
    "Databases": database_score
}


def calculate_average(student_scores):
    total = sum(student_scores.values())
    return total / len(student_scores)


def get_grade(average):
    if average >= 70:
        return "Distinction"
    elif average >= 60:
        return "Merit"
    elif average >= 40:
        return "Pass"
    else:
        return "Fail"

if st.button("Analyse Results", use_container_width=True):

    if not name:
        st.warning("Please enter a student name.")

    else:
        average = calculate_average(scores)
        grade = get_grade(average)

        st.subheader(f"Results for {name}")

        st.success(f"Name: {name}")
        st.success(f"Average Score: {average:.1f}%")
        st.success(f"Final Grade: {grade}")

    