# Strictly Properties - Property Price Prediction Engine

## Project Overview
This repository contains a production-grade property valuation pipeline designed for the Nigerian real estate market. Developed during my tenure as a **Data Scientist & Analyst** at Strictly Properties, the system transitions corporate operations from subjective, manual real estate appraisals to a scalable, automated framework driven by predictive machine learning algorithms.

By deploying this regression-based framework, we provided highly transparent property valuations based on hard data. This successfully protected our customers from inflated market listings, saving buyers millions of Naira and cementing corporate brand loyalty.

***Note on Data Privacy:** To comply with strict corporate confidentiality agreements, all proprietary client data and live business rules have been sanitized. This repository utilizes a functionally equivalent pipeline running on synthetic data that mirrors real-world Nigerian real estate patterns (including regional premiums across Lagos Ikoyi, Abuja Wuse II, etc.).*

## Tech Stack
- **Language:** Python 3.9+
- **Libraries:** pandas, numpy, scikit-learn, matplotlib, seaborn
- **Deployment:** Flask API integrated into internal CRM
- **Environment:** Google Colab → Local Development → Production Server

## Core Features & Machine Learning Architecture
The pipeline implements an end-to-end data preprocessing and modeling workflow using robust Scikit-Learn design principles:
* **Feature Engineering & Preprocessing:** Automates scaling for numerical metrics (`space_sqm`, `num_rooms`, `num_bathrooms`, `age_years`) using `StandardScaler` and handles categorical neighborhood encoders via `OneHotEncoder`.
* **Robust Pipelines:** Packs preprocessors and algorithmic steps inside an easily exportable `Pipeline` wrapper to prevent data leakage during training and testing.
* **Regularization Options:** Built-in modularity to swap between standard `LinearRegression`, `Ridge`, and `Lasso` regression to control model overfitting.
* **Automated Plot Generation:** Automatically exports model performance plots and relative feature importance metrics to the project directory upon training completion.

## Repository Structure
```text
├── assets/                  # Automatically generated evaluation plots
│   ├── model_performance.png
│   └── feature_importance.png
├── sample_output/           # Serialized predictions for audit/validation
│   └── prediction_sample.csv
├── property_price_model.py  # Production-equivalent pipeline execution script
├── EXPLANATION.md           # Detailed data science methodology & model analysis
└── DEPLOYMENT.md            # Enterprise integration & BI dashboard delivery workflow

How to Execute the Pipeline

 1. Clone the project:
    git clone [https://github.com/Dapssyd/strictly-properties-price-predictor.git](https://github.com/Dapssyd/strictly-properties-price-predictor.git)
    cd strictly-properties-price-predictor

 2. Install the necessary data science stack:
    pip install pandas numpy scikit-learn matplotlib seaborn

 3. Run the engine script:
    python property_price_model.py




