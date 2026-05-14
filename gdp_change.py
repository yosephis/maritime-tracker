import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(layout='wide')
st.title('National Macroeconomic Effects of Climate Scenarios')

df_profile = 'gdp_change'
df_1 = pd.read_csv("https://raw.githubusercontent.com/yosephis/maritime-tracker/main/datasets/portfolios/{0}/{1}.csv".format(st.session_state.iso_code, df_profile))

filtered_df1 = df_1[df_1['year'].isin([2030,2040,2050,2060,2070,2080,2090,2100])]

fig=px.bar(filtered_df1, x='year',
           y='gdp_per_c', 
           color='Scenario',
           barmode='group',
           )
fig=fig.update_xaxes(showgrid=True)
# Render the interactive chart inside Streamlit
st.plotly_chart(fig, width='stretch')
#width='content'

df_2 = pd.read_csv("https://raw.githubusercontent.com/yosephis/maritime-tracker/main/datasets/country_gdp.csv")
ssp_1 = df_2[df_2['Scenario'] == 'SSP1-2.6']
ssp_2 = df_2[df_2['Scenario'] == 'SSP2-4.5']  
ssp_3 = df_2[df_2['Scenario'] == 'SSP3-7.0']  
ssp_5 = df_2[df_2['Scenario'] == 'SSP5-8.5']  

options = ['SSP1-2.6','SSP2-4.5','SSP3-7.0','SSP5-8.5']
ssp_selection = st.segmented_control(
           "Which scenario would you like to explore", 
           options,
           default = 'SSP1-2.6')

ssp = df_2[df_2['Scenario'] == ssp_selection]

fig_2 = px.choropleth(ssp, locations="iso",
                    color='gdp_per_c',
                    hover_name="country",
                    hover_data={'year': True,'gdp_per_c': ':.2f'},
                    #locationmode="country names",
                    animation_frame='year',
                    range_color = [-9.5,2],
                    #color_continuous_midpoint = 0,
                    color_continuous_scale=px.colors.diverging.RdYlGn)
fig_2=fig_2.update_layout(paper_bgcolor="white",title_text = 'Annual GDP Per Capita % Change',height= 600, width=400,font_size=18)
fig_2 = fig_2.update_geos(
    showcoastlines=True,
    coastlinecolor="Black",
    showland=True,
    showcountries=True,
    countrycolor="gray",
    fitbounds="locations"
)

#margin=dict(l=20,r=0,b=0,t=70,pad=0)
#height= 700
st.plotly_chart(fig_2,width='stretch')

#width='stretch'        
