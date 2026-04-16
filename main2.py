import pandas as pd
import streamlit as st

# --------------------------------------------------
# SIDEBAR: LOGO AT THE TOP
# --------------------------------------------------

#st.sidebar.image("UCL_Logo_S_1C_B_RGB_Energy-Inst.png", width=200)

st.sidebar.markdown("---")

# Single navigation section
#st.sidebar.page_link("inventories.py", label="Voyage-based Inventories", icon="🚢")
#st.sidebar.page_link("trade.py", label="Merchandise Trade Portfolios", icon="📦")
#st.sidebar.page_link("impact_tracking.py", label="Impact Tracking Results", icon="💵")


# --------------------------------------------------
# MAIN PAGE HEADER
# --------------------------------------------------

st.title("International Shipping Dashboard")

st.caption(
    "Explore global maritime shipping, merchandise trade portfolios, "
    "and economic impact tracking across countries."
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


# Fix Namibia ISO issue
country_iso_codes.loc[
    country_iso_codes.iso_country == "Namibia", "iso_2"
] = "NA"


# --------------------------------------------------
# COUNTRY SELECTOR
# --------------------------------------------------

st.header("Select a Country")

country_choice = st.selectbox(
    "For which country would you like statistics related to international shipping, merchandise trade and MTM impact tracking?",
    country_iso_codes.iso_country.unique(),
    index=2
)


# --------------------------------------------------
# STORE COUNTRY IN SESSION STATE
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
# HOMEPAGE DESCRIPTION
# --------------------------------------------------

st.divider()

st.write(
"""
Use the sidebar to explore the different components of the dashboard.

🚢 **Voyage-based Inventories** – Track shipping movements and inventories.

📦 **Merchandise Trade Portfolios** – Analyse import/export flows by commodity and partner.

💵 **Impact Tracking Results** – Monitor trade impacts and economic metrics.
"""
)
