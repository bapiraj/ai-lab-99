import streamlit as st

def predict_monthly_revenue(weekly_time_spent, avg_watch_duration, is_plan_basic, is_plan_standard, is_plan_premium):
    return (
        4.10199046 * weekly_time_spent +
        1.51112169 * avg_watch_duration +
        -5.48127685 * is_plan_basic +
        0.79409922 * is_plan_standard +
        4.68717763 * is_plan_premium +
        18.064934735340273
    )

st.title("📺 Streaming Revenue Predictor")

st.markdown("""Estimate a user's **monthly revenue** based on their viewing habits and plan type.""")

weekly_time_spent = st.number_input("🕒 Weekly Time Spent (in **hours**)", min_value=0.0, step=0.5, value=10.0)
avg_watch_duration = st.number_input("🎬 Average Watch Duration per Session (in **minutes**)", min_value=0.0, step=1.0, value=45.0)

plan = st.selectbox("📦 Subscription Plan", ["Basic", "Standard", "Premium"])

is_plan_basic = int(plan == "Basic")
is_plan_standard = int(plan == "Standard")
is_plan_premium = int(plan == "Premium")

if st.button("Predict Revenue"):
    predicted_revenue = predict_monthly_revenue(
        weekly_time_spent,
        avg_watch_duration,
        is_plan_basic,
        is_plan_standard,
        is_plan_premium
    )
    st.success(f"💰 Estimated Monthly Revenue: **${predicted_revenue:.2f}**")
