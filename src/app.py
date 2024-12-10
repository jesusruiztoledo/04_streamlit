import streamlit as st

st.title("Esta es mi calculadora")
st.write("Ingrese dos números para sumarlos")
numero1 = st.number_input("Ingrese el primer número")
numero2 = st.number_input("Ingrese el segundo número")
suma = numero1 + numero2
st.write(f"La suma de los dos números es: {suma}")