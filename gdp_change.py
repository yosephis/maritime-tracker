import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(layout='wide')
st.title('National Macroeconomic Effects of Climate Scenarios')

st.divider()

st.markdown("Using Data from Kahn et al. (2021) and Mohaddes and Raissi (2024) we are able to show country-specific annual GDP per-capita losses by country from global warming")  
df_profile = 'gdp_change'
df_1 = pd.read_csv("https://raw.githubusercontent.com/yosephis/maritime-tracker/main/datasets/portfolios/{0}/{1}.csv".format(st.session_state.iso_code, df_profile))


filtered_df1 = df_1[df_1['year'].isin([2030,2040,2050,2060,2070,2080,2090,2100])]

df_world = pd.read_csv("https://raw.githubusercontent.com/yosephis/maritime-tracker/main/datasets/world_gdp_change.csv")

# First segmented control
chart_choice = st.segmented_control(
    label="Would you like to view your country or global GDP losses?",
    options=["Country", "World"],
    default="Country"
)

# Second segmented control
chart_type = st.segmented_control(
    label="Select chart type",
    options=["Bar", "Line"],
    default="Bar"
)

# COUNTRY CHARTS
if chart_choice == "Country":

    # Grouped bar chart (filtered data)
    if chart_type == "Bar":
        fig = px.bar(
            filtered_df1,
            x='year',
            y='gdp_per_c',
            color='Scenario',
            barmode='group'
        )

    # Line chart (full data)
    else:
        fig = px.line(
            df_1,
            x='year',
            y='gdp_per_c',
            color='Scenario',
            markers=True
        )

# WORLD CHARTS
else:

    # Grouped bar chart
    if chart_type == "Bar":
        fig = px.bar(
            df_world,
            x='Year',
            y='gdp_change',
            color='Scenario',
            barmode='group'
        )

    # Line chart
    else:
        fig = px.line(
            df_world,
            x='Year',
            y='gdp_change',
            color='Scenario',
            markers=True
        )

# Common formatting
fig.update_xaxes(showgrid=True)

# Display chart
st.plotly_chart(fig, width='stretch')      
#width='content'

st.divider()

df_2 = pd.read_csv("https://raw.githubusercontent.com/yosephis/maritime-tracker/main/datasets/country_gdp.csv")
ssp_1 = df_2[df_2['Scenario'] == 'SSP1-2.6']
ssp_2 = df_2[df_2['Scenario'] == 'SSP2-4.5']  
ssp_3 = df_2[df_2['Scenario'] == 'SSP3-7.0']  
ssp_5 = df_2[df_2['Scenario'] == 'SSP5-8.5']  

comparison_countries = st.multiselect(
    "Compare countries",
    options=sorted(df_2['country'].unique()),
    default=[st.session_state.iso_country]
)
selected_data = df_2[
    df_2['country'].isin(comparison_countries)
]

max_abs = max(
    abs(selected_data['gdp_per_c'].min()),
    abs(selected_data['gdp_per_c'].max())
)

def make_scenario_chart(data, scenario):

    filtered = data[
        (data['country'].isin(comparison_countries)) &
        (data['Scenario'] == scenario)
    ]

    fig = px.line(
        filtered,
        x='year',
        y='gdp_per_c',
        color='country',
        #markers=True,
        title=scenario
    )

    fig.update_layout(
        height=350,
        margin=dict(l=20, r=20, t=50, b=20),
        legend_title='Country'
    )

    fig.update_yaxes(
        title='% GDP change',
        ticksuffix='%',
        dtick=2,
        range=[-max_abs, max_abs]
    )

    return fig

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        make_scenario_chart(df_2, 'SSP1-2.6'),
        width='stretch'
    )

with col2:
    st.plotly_chart(
        make_scenario_chart(df_2, 'SSP2-4.5'),
        width='stretch'
    )

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(
        make_scenario_chart(df_2, 'SSP3-7.0'),
        width='stretch'
    )

with col4:
    st.plotly_chart(
        make_scenario_chart(df_2, 'SSP5-8.5'),
        width='stretch'
    )

st.divider()

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
                    range_color = [-9.5,4],
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
st.plotly_chart(fig_2,width='stretch')
#margin=dict(l=20,r=0,b=0,t=70,pad=0)
#height= 700

#width='stretch'        
