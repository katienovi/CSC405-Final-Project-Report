import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model = 'gemini-3.5-flash', temperature = 0.2)

st.title('AI-Assisted Data Science Report -  Exploring Seasonal Patterns in Renewable Energy Consumption')
st.write('This Data Science Report seeks to explore seasonal patterns in renewable energy consumption in the United States from 1973 to 2024.')


@st.cache_data
def load_data(file):
    return pd.read_csv(file)


upload_file = st.file_uploader(
    'Upload your CSV dataset',
    max_upload_size = 150,
    type = 'csv'
)

