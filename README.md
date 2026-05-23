# Strictly Properties Price Predictor
**Linear Regression Model for Real Estate Valuation | Nigeria**

## 📌 Project Overview
This repository contains the predictive pricing engine developed for **Strictly Properties**, a Nigerian real estate firm specializing in residential and commercial property transactions. The model estimates accurate market values using location, floor space, room count, property age, and local economic indicators, replacing manual appraisals with data-driven valuations.

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **Libraries:** pandas, numpy, scikit-learn, matplotlib, seaborn
- **Deployment:** Flask API integrated into internal CRM
- **Environment:** Google Colab → Local Development → Production Server

## 📊 Key Features
- Automated data cleaning & feature engineering
- Ridge/Lasso/Linear Regression comparison with cross-validation
- Feature importance visualization for stakeholder transparency
- API endpoint for instant price prediction during client consultations

## 🚀 How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run the model
python src/property_price_model.py  
