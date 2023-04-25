# football_app
https://football-app-2v24.onrender.com

This Python code imports necessary libraries such as Streamlit, Pandas, and Plotly Express. Then, it reads two CSV files, one named "wr_data.csv" and the other named "wr_fantasy_points.csv". The code then renames some columns in the "wr_data" dataset to make them more readable, and merges both datasets into a new dataset named "app_data".

Afterwards, it creates a Streamlit app with a header titled "WR Correlation App" and a dropdown menu to select a column from the "app_data" dataset. Then, it creates two interactive plots using Plotly Express, a histogram and a scatter plot, where the selected column is used as the X-axis and the "Fantasy_Points" column is used as the Y-axis. These plots are displayed using Streamlit's "plotly_chart" function.

Overall, this code generates a Streamlit app that displays the correlation between a selected column and fantasy points for a dataset of wide receivers (WR) in American football.