import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.title('Vehículos de Estados Unidos')
# Crear un subtítulo
st.header(
    'Número de vehículos que han recorrido una distancia específica', divider=True)

# crear casilla de verificación
hist_check = st.checkbox('Construir histograma')
if hist_check:  # al seleccionar la casilla de verificación
    # escribir mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de vehículos')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un subtítulo
st.header(
    'Relación entre la distancia recorrida por los vehículos y su precio', divider=True)
scatter_check = st.checkbox('Construir gráfico de dispersión')
if scatter_check:  # al seleccionar la casilla de verificación
    # escribir mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de vehículos')

    # crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig2, user_container_width=True)