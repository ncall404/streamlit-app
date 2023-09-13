import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_kart = pd.read_csv('data/kart_stats.csv')
df_kart = df_kart[['Body', 'Acceleration', 'On-Road traction', 'Mini-Turbo', 'Ground Speed', 'Ground Handling']]

st.dataframe(df_kart.style
             .highlight_max(color='lightgreen', axis=0, subset=['Acceleration', 'On-Road traction', 'Mini-Turbo', 'Ground Speed', 'Ground Handling'])
             .highlight_min(color='red', axis=0, subset=['Acceleration', 'On-Road traction', 'Mini-Turbo', 'Ground Speed', 'Ground Handling']))

st.write("Relationship of Acceleration and Mini-Turbo")
st.line_chart(df_kart, x='Mini-Turbo', y='Acceleration')

st.write("Relationship of Ground Speed and Ground Handling")
st.area_chart(df_kart, x='Ground Handling', y='Ground Speed')

st.write("Check a Kart's Stats")
kart_choice = st.selectbox('Choose a Kart', df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body'] == kart_choice]
df_single_kart = df_single_kart.drop(columns=['Body'])
df_unp_kart = df_single_kart.unstack().rename_axis(['category', 'row number']).reset_index().drop(columns='row number').rename({0: 'strength'}, axis=1)

st.bar_chart(df_unp_kart, x='category', y='strength')