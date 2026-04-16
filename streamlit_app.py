import streamlit as st
import pandas as pd
st.sidebar.image("UCL_Logo_S_1C_B_RGB_Energy-Inst.png", width=200)

st.sidebar.markdown("---")

# Define the pages
main = st.Page("main2.py", title="Home", icon="🏡")
inventories = st.Page("inventories.py", title="Voyage-based Inventories", icon="🚢")
trade = st.Page("trade.py", title="Merchandise Trade Portfolios", icon="📦")
impact_tracking = st.Page("impact_tracking.py", title="Impact Tracking Results", icon="💵")

# Set up navigation
pg = st.navigation([main, inventories, trade, impact_tracking])

# Run the selected page
pg.run()
