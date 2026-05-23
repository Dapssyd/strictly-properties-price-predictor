# Theoretical and Technical Explanation

## Data Preprocessing Pipeline
Real estate features vary significantly in scale (e.g., area in square meters vs. the absolute number of rooms). To ensure numerical stability and accurate coefficient optimization during gradient descent, the numerical attributes are isolated and transformed via a Z-score normalization standardizer:

$$z = \frac{x - \mu}{\sigma}$$

Categorical neighborhood parameters (`location`) are transformed into numerical feature spaces via dummy encoding (One-Hot Encoding), dropping the first structural column to avoid severe multicollinearity issues, often termed the **Dummy Variable Trap**.

## Algorithmic Strategy & Regularization
While standard ordinary least squares (OLS) linear regression functions adequately, the production script defaults to **Ridge Regression** to optimize predictive accuracy. Real estate datasets frequently exhibit multi-collinearity (e.g., square footage often correlates strongly with the number of bedrooms). 

Ridge regression introduces an $L_2$ regularization penalty term to the cost function to restrict the size of the model coefficients, stabilizing predictions against localized market variances:

$$\text{Cost Function} = \sum_{i=1}^{n} \left( y_i - \hat{y}_i \right)^2 + \alpha \sum_{j=1}^{p} w_j^2$$

## Model Performance Metrics
The system outputs three key statistical evaluation parameters:
1. **Mean Absolute Error (MAE):** Quantifies average prediction error in absolute Naira, mapping directly to average consumer savings.
2. **Root Mean Squared Error (RMSE):** Penalizes larger outlier prediction errors heavily, ensuring the company does not drastically misprice luxury properties.
3. **Coefficient of Determination ($R^2$ Score):** Measures the proportion of variance in property cost that is predictable from the independent input features.
