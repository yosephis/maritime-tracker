import streamlit as st
import pandas as pd

# Inject logo at the top of sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"]::before {
        content: "";
        display: block;
        margin: 20px auto 20px auto;
        height: 120px;
        width: 180px;
        background-image: UCL_Logo_S_1C_B_RGB_Energy-Inst.png;
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define pages
main = st.Page("main2.py", title="Home", icon="🏡")
inventories = st.Page("inventories.py", title="Voyage-based Inventories", icon="🚢")
trade = st.Page("trade.py", title="Merchandise Trade Portfolios", icon="📦")
impact_tracking = st.Page("impact_tracking.py", title="Impact Tracking Results", icon="💵")

# Navigation
pg = st.navigation([main, inventories, trade, impact_tracking])

pg.run()
