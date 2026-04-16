import pandas as pd
import streamlit as st

# --------------------------------------------------
# SIDEBAR LOGO AND NAVIGATION
# --------------------------------------------------

st.sidebar.image("UCL_Logo_S_1C_B_RGB_Energy-Inst.png", width=200)

st.sidebar.markdown("### International Shipping Dashboard")

st.sidebar.page_link("inventories.py", label="Voyage-based Inventories", icon="🚢")
st.sidebar.page_link("trade.py", label="Merchandise Trade Portfolios", icon="📦")
st.sidebar.page_link("impact_tracking.py", label="Impact Tracking Results", icon="💵")


# --------------------------------------------------
# MAIN PAGE HEADER
# --------------------------------------------------

st.title("Welcome to the International Shipping Dashboard")

st.caption(
    "A platform for analysing global maritime trade flows, shipping inventories, "
    "and impact tracking across countries."
)

st.divider()


# --------------------------------------------------
# LOAD COUNTRY ISO DATA
# --------------------------------------------------

country_iso_codes_c = ["name", "alpha-2", "alpha-3", "country-code"]
country_iso_codes_d = {"alpha-2": str, "alpha-3": str, "country-code": str}
country_iso_codes_r = {
    "name": "iso_country",
    "alpha-2": "iso_2",
    "alpha-3": "iso_3",
    "country-code": "iso_code"
}

country_iso_codes = pd.read_csv(
    "https://raw.githubusercontent.com/james-stewart-808/inventory-tracker/main/datasets/country_iso_codes.csv",
    usecols=country_iso_codes_c,
    dtype=country_iso_codes_d
).rename(columns=country_iso_codes_r)


# Fix Namibia ISO code issue
country_iso_codes.loc[
    country_iso_codes.iso_country == "Namibia", "iso_2"
] = "NA"


# --------------------------------------------------
# COUNTRY SELECTION
# --------------------------------------------------

st.header("Select a Country")

country_choice = st.selectbox(
    "For which country would you like statistics related to international shipping, merchandise trade and MTM impact tracking?",
    country_iso_codes.iso_country.unique(),
    index=2
)


# --------------------------------------------------
# STORE SELECTION IN SESSION STATE
# --------------------------------------------------

st.session_state.iso_country = country_choice

st.session_state.iso_2 = country_iso_codes[
    country_iso_codes.iso_country == country_choice
].iso_2.values[0]

st.session_state.iso_3 = country_iso_codes[
    country_iso_codes.iso_country == country_choice
].iso_3.values[0]

st.session_state.iso_code = country_iso_codes[
    country_iso_codes.iso_country == country_choice
].iso_code.values[0]


# --------------------------------------------------
# DASHBOARD DESCRIPTION
# --------------------------------------------------

st.divider()

st.header("Explore the Dashboard")

st.write(
    """
    Use the navigation menu on the left to explore different components of the dashboard:

    🚢 **Voyage-based Inventories**  
    Track shipping voyages and inventory movements.

    📦 **Merchandise Trade Portfolios**  
    Explore import and export trade flows by commodity and partner country.

    💵 **Impact Tracking Results**  
    Analyse economic impacts and trade-related metrics.
    """
)
