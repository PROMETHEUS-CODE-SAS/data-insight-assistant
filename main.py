import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# Configuración general
st.set_page_config(page_title="Data Insight Assistant", layout="wide")

# Logo
logo = Image.open("logo.png")
st.sidebar.image(logo, width=200)
st.sidebar.title("📁 Menú de navegación")
section = st.sidebar.radio("Ir a:", ["Inicio", "Carga de datos", "Análisis", "Visualizaciones"])

st.title("🧠 Data Insight Assistant")
st.markdown("> Tu compañero inteligente para análisis de datos exploratorios")

if section == "Inicio":
    st.subheader("🚀 Bienvenido")
    st.write("""
        Este asistente está diseñado para ayudarte a explorar tus datos de forma sencilla, rápida y visual.
        Sube un archivo CSV y obtén estadísticas, gráficos y patrones útiles sin escribir una sola línea de código.
    """)

elif section == "Carga de datos":
    st.subheader("📤 Subir archivo CSV")
    uploaded_file = st.file_uploader("Elige tu dataset", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state['df'] = df
        st.success("✅ Archivo cargado correctamente")
        st.dataframe(df.head())

elif section == "Análisis":
    if 'df' in st.session_state:
        df = st.session_state['df']
        st.subheader("📈 Estadísticas Descriptivas")
        st.write(df.describe())
        st.subheader("🔍 Información general")
        buffer = df.info(buf=None)
    else:
        st.warning("Por favor, carga un archivo primero en la sección anterior.")

elif section == "Visualizaciones":
    if 'df' in st.session_state:
        df = st.session_state['df']
        st.subheader("📊 Mapa de Calor de Correlación")
        corr = df.corr(numeric_only=True)
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

        st.subheader("📈 Histogramas por variable")
        num_cols = df.select_dtypes(include=['float64', 'int64']).columns
        for col in num_cols:
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            st.pyplot(fig)
    else:
        st.warning("Por favor, carga un archivo primero en la sección de 'Carga de datos'.")
