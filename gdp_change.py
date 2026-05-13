import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.title('National Macroeconomic Effects of Climate Scenarios')

df_profile = 'gdp_change'
df_1 = pd.read_csv("https://raw.githubusercontent.com/yosephis/maritime-tracker/main/datasets/portfolios/{0}/{1}.csv".format(st.session_state.iso_code, df_profile),index_col=2)

filtered_df1 = df_1[df_1['year'].isin(['2030','2040','2050','2060','2070','2080','2090','2100'])]

fig=px.bar(filtered_df1, x='year',
           y='gdp_per_c', 
           color='Scenario',
           barmode='group',
           text_auto=True)

# Render the interactive chart inside Streamlit
st.plotly_chart(fig, width='stretch')
#width='content'
