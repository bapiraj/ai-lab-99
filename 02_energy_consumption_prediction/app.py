import streamlit as st

def predict_energy_consumption(temperature, humidity):
    return 3.40772114 * temperature + 2.00133069 * humidity + 53.02343025491177

st.title("⚡ Predict Energy Consumption")
st.markdown("""Enter the temperature (°C) and humidity (%) to predict the energy consumption""")

temperature = st.number_input("Temperature (°C)", min_value=-50.0, max_value=60.0, value=25.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0, step=0.1)

if st.button("Predict"):
    prediction = predict_energy_consumption(temperature, humidity)
    st.success(f"🔋 Predicted Energy Consumption: **{prediction:.2f} kWh**")

