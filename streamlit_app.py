import streamlit as st
import joblib
import pandas as pd
import json

st.title("Clasificador de mascotas")
st.write("Este es un clasificador de mascotas que utiliza un modelo de machine learning para predecir la raza de la mascota")
st.image("img/mascotas.jpg")

# Carga el modelo entrenado y las asignaciones para el color de ojos y el largo del pelo
model = joblib.load("model/pets_model.joblib")
with open("model/category_mapping.json") as f:
    category_mapping = json.load(f)

# Extraemos los valores categóricos 
eye_color_values = category_mapping["eye_color"]
fur_length_values = category_mapping["fur_length"]

# Creamos un formulario para que el usuario ingrese los datos de la mascota
weight = st.number_input("Peso (kg)", min_value=0.0, max_value=100.0, value=0.0)
height = st.number_input("Altura (cm)", min_value=10.0, max_value=100.0, value=10.0)
eye_color = st.selectbox("Color de ojos",["Azul", "Marrón", "Gris", "Verde"])
fur_length = st.selectbox("Largo del pelo", ["Largo", "Medio", "Corto"])

# Mapea la selección de color de ojos y largo del pelo al español
eye_color_map = {"Marrón": "Brown", "Azul": "Blue", "Gris": "Gray", "Verde": "Green"}
fur_length_map = {"Largo": "Long", "Medio": "Medium", "Corto": "Short"}

selected_eye_color = eye_color_map[eye_color]
selected_fur_length = fur_length_map[fur_length]

# Genera las columnas binarias para eye_color y fur_legth
# eye_color_binary = [int(color == selected_eye_color) for color in eye_color_values]
eye_color_binary = [(color == selected_eye_color) for color in eye_color_values]
fur_length_binary = [(length == selected_fur_length) for length in fur_length_values]

# Crea un DataFrame con los datos de la mascota
input_data = [weight, height] + eye_color_binary + fur_length_binary
columns = ["weight_kg", "height_cm"] + [f"eye_color_{color}" for color in eye_color_values] + [f"fur_length_{length}" for length in fur_length_values]
input_df = pd.DataFrame([input_data], columns=columns)

# Realiza la predicción
prediction = model.predict(input_df)[0]

if st.button("Clasifica la mascota"):
    prediction = model.predict(input_df)[0]
    prediction_map = {"dog": "Perro", "cat": "Gato", "rabbit": "Conejo"}
    st.success(f"La mascota es un {prediction_map[prediction]}", icon="✅")