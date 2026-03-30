import pandas as pd
import requests
from io import StringIO
import streamlit as st
st.header("Welcome to the Homepage of the International Shipping Dashboard 🏡")


# Function to load the CSV file
#@st.cache_data(scope="session")
#def load_data(file_dir):
#    data_dir = "https://raw.githubusercontent.com/james-stewart-808/inventory-tracker/main/"
#    return pd.read_csv(data_dir + file_dir)

#country_iso_codes = load_data('datasets/dom_inv_by_vess_type.csv')

country_iso_codes = pd.read_csv(
  "https://raw.githubusercontent.com/james-stewart-808/inventory-tracker/main/datasets/dom_inv_by_vess_type.csv",
  usecols=country_iso_codes_cols, 
  dtype=country_iso_codes_dtype).rename(
  columns=country_iso_codes_renames)
country_iso_codes.loc[country_iso_codes.iso_country == "Namibia", "iso_2"] = "NA"

st.write(country_iso_codes.head())
#
