# 📈 Digital Marketing Ad Revenue Prediction (Polynomial Regression)

This project demonstrates a **Polynomial Regression** model to predict weekly revenue based on ad spending per week.  
It includes the full workflow from data loading and preprocessing to model training, interpretation, evaluation, and deployment via a Streamlit app.

---

## 📖 Project Description

- **Objective:** Predict weekly revenue from digital marketing campaigns  
- **Model Used:** Polynomial Regression (Linear Regression with polynomial features)  
- **Dataset:** A synthetic dataset of weekly ad spending vs. weekly revenue  
- **Feature Preprocessing:**  
  - Added a new column representing the squared term of ad spending (`x^2`) to capture nonlinear trends  
- **Workflow:**  
  1. Data Loading  
  2. Data Exploration
  3. Data Preprocessing & Model Training - Linear Regression
  4. Model Interpretation - Linear Regression 
  5. Model Evaluation - Linear Regression 
  6. Data Preprocessing & Model Training - Polynomial Regression
  7. Model Interpretation - Polynomial Regression 
  8. Model Evaluation - Polynomial Regression  
  9. Model Deployment  

---

## ⚙️ Setup

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/bapiraj/ai-lab-99.git
cd 05_digital_marketing_revenue_prediction
pip install -r requirements.txt
```

Run the streamlit app
```bash
streamlit run app.py
```
