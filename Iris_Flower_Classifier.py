import streamlit as st

import os
import joblib


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'iris_model.pkl')
model = joblib.load(model_path)

st.set_page_config(
    page_title="Welcome to Iris Flower Classifier",
    page_icon="🌸",
    layout="centered"
)

st.title("Iris Flower Classifier")
st.caption("Streamlit Demo Ex2")

st.divider()

Sepal_length=st.number_input("Sepal Length (cm)", min_value=1.0, max_value=50.0)
Sepal_width=st.number_input("Sepal Width (cm)", min_value=1.0, max_value=50.0)

Petal_length=st.number_input("Petal Length (cm)", min_value=1.0, max_value=50.0)
Petal_width=st.number_input("Petal Width (cm)", min_value=1.0, max_value=50.0)


button=st.button("Predict Species")

if button:
    input_data=[[Sepal_length, Sepal_width, Petal_length, Petal_width]]
    y=model.predict(input_data)
    values={ 0 : "Setosa",1 : "Versicolor",2 : "Virginica"}
    st.write("The type of iris flower is: {}".format(values[y[0]]))
else:
    st.write("Please enter the values and click on the 'Predict Species' button to see the flower species .")
