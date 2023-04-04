import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv("C:/Users/patba/Downloads/practicum resources/notebooks/wr_data.csv", header=1)
renamed_columns = {'AY.1': 'AY%', 'TAR.1':'TAR%', 'YDS.1':'YAC', 'AVG':'YAC_AVG'}
data = data.rename(columns=renamed_columns)
f_points = pd.read_csv('C:/Users/patba/Downloads/practicum resources/notebooks/wr_fantasy_points.csv')
app_data = pd.merge(data, f_points)
app_data


st.header('WR Correlation App')
col = st.selectbox('Select a column', app_data.columns)
fig_hist = px.histogram(app_data, x=col, nbins=30, title=f'{col}')
fig_scatter = px.scatter(app_data, x=col, y='Fantasy_Points', title=f'Fantasy Points vs {col}')
st.plotly_chart(fig_hist)
st.plotly_chart(fig_scatter)

