import os
os.environ["STREAMLIT_WATCHDOG_USE_POLLING"] = "true"

import streamlit as st

st.title("Elite Sports Betting Model")
st.write("Upload your data and run predictions below")

uploaded_file = st.file_uploader("Choose your file")

if uploaded_file is not None:
    st.success("File uploaded! Model predictions will go here.")
import streamlit as st

st.title("Elite Sports Betting Model")
st.write("Upload your data and run predictions.")

uploaded_file = st.file_uploader("Choose your sports data CSV file")

if uploaded_file is not None:
    st.success("File uploaded! Model predictions would show here.")
