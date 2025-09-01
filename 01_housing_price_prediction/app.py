import streamlit as st

def predict_housing_price(area):
    return 670.33282313*area + 122632.82090315572

st.title("🏡 Housing Price Prediction")

st.write("Enter the area of the house (in sqft) to estimate its price")

area = st.number_input("Area (sqft):", min_value=0.0, step=10.0)

if st.button("Submit"):
    if area <= 0:
        st.error("Please enter a valid area.")
    else:
        price = predict_housing_price(area)
        st.success(f"Estimated Price: ${price:,.2f}")

