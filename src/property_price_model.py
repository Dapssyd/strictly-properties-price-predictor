"""
PORTFOLIO IMPLEMENTATION | SANITIZED FOR CONFIDENTIALITY
This script is a functionally equivalent replica of the production pricing pipeline 
I designed and deployed at Strictly Properties (Nigeria). All client data, 
proprietary business rules, and production credentials have been replaced with 
synthetic equivalents to comply with confidentiality agreements. The architecture, 
modeling approach, evaluation metrics, and deployment workflow mirror the actual system.
"""

"""
Strictly Properties - Property Price Prediction Engine
Role: Data Scientist & Analyst | Location: Nigeria
Description: Linear regression model for real estate valuation.
Note: This repository contains a sanitised, educational demonstration.
      Production data has been replaced with synthetic equivalents for portfolio purposes.
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Set plotting style
sns.set_theme(style="whitegrid")
plt.rcParams.update({'figure.dpi': 120})

def generate_synthetic_data(n_samples=1500, random_state=42):
    """Generates realistic mock property data matching Nigerian market patterns."""
    np.random.seed(random_state)
    locations = np.random.choice(['Lagos_Ikoyi', 'Abuja_Wuse_II', 'PortHarcourt_GRA', 
                                  'Enugu_TransEkulu', 'Ibadan_Bodija'], n_samples)
    space = np.random.uniform(60, 350, n_samples)
    rooms = np.random.randint(1, 6, n_samples)
    baths = np.random.randint(1, 4, n_samples)
    age = np.random.randint(0, 30, n_samples)
    
    # Base pricing logic (in NGN millions)
    base = 18 + 0.28 * space + 2.8 * rooms + 1.2 * baths - 0.35 * age + np.random.normal(0, 2.5, n_samples)
    loc_premium = np.where(locations == 'Lagos_Ikoyi', 30, 
                  np.where(locations == 'Abuja_Wuse_II', 20, 8))
    price = (base + loc_premium) * 1_000_000
    
    return pd.DataFrame({
        'location': locations, 'space_sqm': space, 'num_rooms': rooms,
        'num_bathrooms': baths, 'age_years': age, 'price_ngn': price
    })

def preprocess_and_train(df, model_type='ridge'):
    """Preprocesses data, trains model, and returns pipeline + predictions."""
    X = df.drop('price_ngn', axis=1)
    y = df['price_ngn']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    num_features = ['space_sqm', 'num_rooms', 'num_bathrooms', 'age_years']
    cat_features = ['location']
    
    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), cat_features)
    ])
    
    if model_type == 'ridge':
        model = Ridge(alpha=1.0)
    elif model_type == 'lasso':
        model = Lasso(alpha=0.5)
    else:
        model = LinearRegression()
        
    pipeline = Pipeline([('preprocessor', preprocessor), ('regressor', model)])
    pipeline.fit(X_train, y_train)
    
    y_pred = pipeline.predict(X_test)
    metrics = {
        'MAE': mean_absolute_error(y_test, y_pred),
        'RMSE': np.sqrt(mean_squared_error(y_test, y_pred)),
        'R2': r2_score(y_test, y_pred)
    }
    return pipeline, X_test, y_test, y_pred, metrics

def save_results_and_plots(pipeline, y_test, y_pred):
    """Saves prediction sample and generates evaluation visualizations."""
    os.makedirs('assets', exist_ok=True)
    os.makedirs('sample_output', exist_ok=True)
    
    # 1. Save sample predictions
    sample = pd.DataFrame({
        'Actual_Price_NGN': y_test.values[:5],
        'Predicted_Price_NGN': y_pred[:5],
        'Error_Percent': np.abs((y_test.values[:5] - y_pred[:5]) / y_test.values[:5] * 100).round(2)
    })
    sample.to_csv('sample_output/prediction_sample.csv', index=False)
    
    # 2. Actual vs Predicted Plot
    plt.figure(figsize=(6, 4))
    plt.scatter(y_test, y_pred, alpha=0.6, color='steelblue', edgecolor='black')
    lims = [y_test.min(), y_test.max()]
    plt.plot(lims, lims, 'r--', lw=2, label='Perfect Fit')
    plt.xlabel('Actual Price (₦)'); plt.ylabel('Predicted Price (₦)')
    plt.title('Model Performance: Actual vs Predicted')
    plt.legend(); plt.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('assets/model_performance.png'); plt.close()
    
    # 3. Feature Importance Plot
    feature_names = (
        list(pipeline.named_steps['preprocessor'].named_transformers_['num'].feature_names_in_) +
        list(pipeline.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out())
    )
    coefs = pipeline.named_steps['regressor'].coef_
    plt.figure(figsize=(6, 4))
    sns.barplot(x=coefs, y=feature_names, palette='coolwarm')
    plt.axvline(0, color='black', linewidth=0.8)
    plt.title('Feature Importance (Regression Coefficients)')
    plt.tight_layout(); plt.savefig('assets/feature_importance.png'); plt.close()

if __name__ == "__main__":
    print("🏠 Strictly Properties Price Predictor - Initializing...")
    df = generate_synthetic_data()
    pipeline, X_test, y_test, y_pred, metrics = preprocess_and_train(df, model_type='ridge')
    
    print("\n📊 Model Evaluation Metrics:")
    for k, v in metrics.items():
        print(f"   {k}: ₦{v:,.2f}" if k != 'R2' else f"   {k}: {v:.4f}")
        
    print("\n📁 Generating assets/ and sample_output/...")
    save_results_and_plots(pipeline, y_test, y_pred)
    print("✅ Complete. Review generated files for portfolio evidence.")
