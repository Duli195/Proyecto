import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title('Análisis de vehículos en venta en EE.UU.')

# Cargar los datos desde el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Histograma
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Histograma de odómetro')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Dispersión
if st.checkbox('Mostrar gráfico de dispersión (odómetro vs precio)'):
    st.write('Dispersión: odómetro vs precio')
    fig2 = go.Figure(data=go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers'))
    fig2.update_layout(title='Odómetro vs Precio', xaxis_title='Odómetro', yaxis_title='Precio')
    st.plotly_chart(fig2, use_container_width=True)
