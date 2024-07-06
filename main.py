import streamlit as st
import streamlit.components.v1 as components


st.title("Esto es un titulo")
st.write("Esto es un texto")

st.file_uploader("Esto es para subir un archivo")

st.selectbox("Esto es un select box", ["Opcion 1", "Opcion 2", "Opcion 3"])

boton = st.button("Esto es un boton")
st.write(f'El valor del boton es: {boton}')

st.write('Intentando renderizar una presentacion de Google')
components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRI6PJMC0KnwygrjhoSusvv7sZmyfdZCHRS9JHUwln4XMK-5ePWmV8gY4dd24gM9Q/embed?start=false&loop=false&delayms=3000", height=600, width=800)
