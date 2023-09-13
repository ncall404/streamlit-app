import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_kart = pd.read_csv('data/kart_stats.csv')
df_kart = df_kart[['Body', 'Weight', 'Acceleration', 'Mini-Turbo', 'Ground Speed', 'Ground Handling']]

st.dataframe(df_kart.style
             .highlight_max(color='lightgreen', axis=0, subset=['Weight', 'Acceleration', 'Mini-Turbo', 'Ground Speed', 'Ground Handling'])
             .highlight_min(color='red', axis=0, subset=['Weight', 'Acceleration', 'Mini-Turbo', 'Ground Speed', 'Ground Handling']))