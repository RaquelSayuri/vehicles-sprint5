import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

st.header('Dashboard Vehicles Sprint 5') # Criar um cabeçalho

hist_button = st.button('Criar histograma') # criar um botão
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

disper_button = st.button('Criar Gráfico de Dispersão') # criar um botão
if disper_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um Gráfico de Dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
