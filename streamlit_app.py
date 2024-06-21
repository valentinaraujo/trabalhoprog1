import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Países_Popul.csv", sep=';')

st.sidebar.header('Filtros')

paises = df['País'].unique()
país_filter = st.sidebar.multiselect('Selecionar Paises:', paises, default=paises)

filtered_data = df[df['País'].isin(país_filter)]

st.write('## Dados Filtrados ##', filtered_data)

st.write('## Gráfico de População ##')
plt.figure(figsize=(10, 6))
plt.bar(filtered_data['País'], filtered_data['População'])
plt.title('População por País')
plt.xlabel('País')
plt.ylabel('População')
plt.xticks(rotation=45)
st.pyplot(plt)

$ streamlit run streamlit_app.py

