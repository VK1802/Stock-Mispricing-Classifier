import os

# Load model if it exists, otherwise run in demo mode
if os.path.exists("models/final_model.pkl"):
    model = pickle.load(open("models/final_model.pkl", "rb"))
else:
    model = None

st.title("Stock Mispricing Classifier")

st.write("Predict if a stock is undervalued or overvalued.")

# User inputs
roa = st.number_input("Return on Assets")
debt_ratio = st.number_input("Debt Ratio")
profit_margin = st.number_input("Profit Margin")
inflation = st.number_input("Inflation Rate")
unemployment = st.number_input("Unemployment Rate")

if st.button("Predict"):

    data = pd.DataFrame([[roa, debt_ratio, profit_margin, inflation, unemployment]],
                        columns=["roa","debt_ratio","profit_margin","inflation","unemployment"])

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.success("Stock appears UNDERVALUED")
    else:
        st.error("Stock appears OVERVALUED")
