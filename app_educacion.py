import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

st.title("Análisis de Datos de Educación en Colombia")

# #Leer archivo
# df = pd.read_csv("./static/educacion.csv")

uploaded_file = st.file_uploader("Cargar archivo 'educacion.csv'", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

#Mostrar la tabla de datos en Streamlit:
st.dataframe(df)

#Agregar widgets para filtrar los datos:
st.sidebar.header("Filtros")
nivel_educativo = st.sidebar.multiselect(
    "Nivel educativo", df["Nivel educativo"].unique()
)
carrera = st.sidebar.multiselect("Carrera", df["Carrera"].unique())
institucion = st.sidebar.multiselect("Institución", df["Institución"].unique())

#Filtrar el DataFrame con base en los filtros seleccionados:

df_filtrado = df.copy()
if nivel_educativo:
    df_filtrado = df_filtrado[df_filtrado["Nivel educativo"].isin(nivel_educativo)]
if carrera:
    df_filtrado = df_filtrado[df_filtrado["Carrera"].isin(carrera)]
if institucion:
    df_filtrado = df_filtrado[df_filtrado["Institución"].isin(institucion)]

#Mostrar el DataFrame filtrado:
st.dataframe(df_filtrado)

#Calcular y mostrar estadísticas descriptivas de los datos filtrados:
st.subheader("Estadísticas Descriptivas")
st.write(df_filtrado.describe())

# Conteo de estudiantes por nivel educativo
st.subheader("Conteo de Estudiantes por Nivel Educativo")
st.bar_chart(df_filtrado["Nivel educativo"].value_counts())

# #Visualizar la distribución de la edad con un histograma:
#st.subheader("Distribución de la Edad")
# st.pyplot(df_filtrado["Edad"], bins=10)

#st.histogram(df_filtrado["Edad"], bins=10)



 # Graficar el histograma
st.subheader("Distribución de la Edad")
plt.hist(df_filtrado["Edad"], bins=30, color='blue', alpha=0.7)  # Histograma
plt.title('Histograma de Valores')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
st.pyplot(plt)  # Mostrar el gráfico en Streamlit
plt.clf()  # Limpiar la figura para evitar que se muestre más de una vez