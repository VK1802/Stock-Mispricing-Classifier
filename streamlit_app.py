import streamlit as st
import pandas as pd

st.title("Stock Mispricing Classifier")

st.write("Predict whether a stock is undervalued or overvalued.")

roa = st.number_input("Return on Assets")
debt_ratio = st.number_input("Debt Ratio")
profit_margin = st.number_input("Profit Margin")
inflation = st.number_input("Inflation Rate")
unemployment = st.number_input("Unemployment Rate")

if st.button("Predict"):

    score = roa + profit_margin - debt_ratio - inflation*0.1 - unemployment*0.05

    if score > 0:
        st.success("Stock appears UNDERVALUED")
    else:
        st.error("Stock appears OVERVALUED")
