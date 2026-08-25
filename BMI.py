import streamlit as st

st.set_page_config(
    page_title="Welcome to BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

st.title("BMI Calculator")
st.caption("Streamlit Demo")

st.divider()

weight=st.number_input("Weight (kg)", min_value=1.0, max_value=200.0, value=70.0, step=0.1)
height=st.number_input("Height (cm)", min_value=1.0, max_value=250.0, value=170.0, step=0.1)

if st.button("Calculate the BMI"):
    bmi=weight/(height/100)**2


    
    if bmi<18.5:
        category= ("You are underweight.")
    elif bmi<24.9:
        category= ("You have a normal weight.")
    elif 25<=bmi<29.9:
        category= ("You are overweight.")
    else:
        category= ("You are obese.")

    st.write(f"Your BMI is: {bmi:.2f} - {category}")

