import streamlit as st

def predict_revenue_usd_polynomial_regression(ad_spend_usd):
    return -4.21948692e-04 * (ad_spend_usd)**2 + 6.51043749e+00 * ad_spend_usd + 8123.725871275172

# Streamlit app layout
st.title("📊 Predict Revenue from Ad Spend")

# User input
ad_spend_input = st.number_input("Enter Ad Spend (USD)", min_value=0.0, value=1000.0, step=100.0)

# Submit button
if st.button("Predict"):
    predicted_revenue = predict_revenue_usd_polynomial_regression(ad_spend_input)
    st.markdown("### 💰 Predicted Revenue")
    st.metric(label="Estimated Revenue (USD)", value=f"${predicted_revenue:,.2f}")
