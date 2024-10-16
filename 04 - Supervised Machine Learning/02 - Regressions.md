# Regression Overview

## Workflow

### 1. **Data Requirements**

#### 1.1 **Data Quality**
- **Missing Values (NaN)**: 
  - Missing values can bias the model or reduce its performance.
  - Options: Impute missing values (mean, median, mode) or drop rows/columns with too many missing values.

#### 1.2 **Balanced Data**
- **Class Balance**: 
  - For regression, ensure that the range of the target variable is well-represented.

#### 1.3 **Outliers**
- **Outlier Handling**: 
  - Outliers can significantly affect regression models, especially linear regression.
  - Options: Transform data or drop rows with outliers

#### 1.4 **Normalization/Standardization**
- **Feature Scaling**: 
  - Many models (e.g., SVM, logistic regression) perform better when features are on a similar scale.
  - **Normalization**: Re-scale data to a [0,1] range.
  - **Standardization**: Re-scale data to have a mean of 0 and a standard deviation of 1.

#### 1.5 **Co-linearity**
- **Multi Co-linearity**: 
  - High correlation between features can cause instability in the model.
  - Options: Use variance inflation factor (VIF) to detect multi co-linearity and remove correlated features.

---

### 2. **Exploratory Data Analysis (EDA)**

#### 2.1 **Descriptive Statistics**
- **Mean, Median, Mode**: Understand the central tendency.
- **Variance, Standard Deviation**: Measure the spread of the data.
- **Skewness, Kurtosis**: Assess the distribution of the data.

#### 2.2 **Data Visualization**
- **Histograms**: Visualize the distribution of individual features.
- **Box Plots**: Detect outliers and understand the spread.
- **Scatter Plots**: Explore relationships between features and the target variable.
- **Pair Plots**: For multivariate relationships.

#### 2.3 **Correlation Analysis**
- **Heatmaps**: Visualize correlations between features.
- **Correlation Coefficient (Pearson, Spearman)**: Quantify the strength of relationships.

---

### 3. **Data Cleaning**

Data cleaning is essential for ensuring that the dataset is ready for model training.

#### 3.1 **Handling Missing Values**
- **Imputation**: Fill missing values using statistical methods like mean, median, mode, or more sophisticated methods like K-Nearest Neighbors (KNN) imputation.
- **Dropping**: If the amount of missing data is substantial, consider dropping those rows or columns so that the results are not biased by too much imputation.

#### 3.2 **Removing Duplicates**
- **Check for Duplicate Entries**: Ensure there are no repeated rows that might skew the analysis.

#### 3.3 **Outlier Treatment**
- **Transformation**: Apply logarithmic or square root transformations to reduce the impact of outliers.
- **Removal**: In some cases, removing extreme outliers is necessary.

#### 3.4 **Encoding Categorical Variables**
- **One-Hot Encoding**: For nominal categorical variables.
- **Label Encoding**: For ordinal categorical variables.

#### 3.5 **Feature Engineering**
- **Polynomial Features**: Create interaction or polynomial terms if relationships between features and the target are non-linear.
- **Binning**: Convert continuous variables into categorical bins if necessary.
- **Feature Selection**: Use techniques like LASSO, Ridge, or Recursive Feature Elimination (RFE) to select important features.

---

### 4. **Choosing the Correct Model**

#### 4.1 [**Linear Regression**](https://github.com/tbgrun/machine_learning/blob/main/04%20-%20Supervised%20Machine%20Learning/02.01%20-%20Linear%20Regression.md)
- **Best for**: When the relationship between features and the target is linear.
- **Pros**: Simple, interpretable.
- **Cons**: Sensitive to outliers, assumes linearity.

#### 4.2 **Polynomial Regression**
- **Best for**: When the relationship is non-linear but can be represented as a polynomial.
- **Pros**: Captures non-linear relationships.
- **Cons**: Prone to overfitting with high-degree polynomials.

#### 4.3 **Logistic Regression**
- **Best for**: Binary classification problems, not strictly regression.
- **Pros**: Good for binary outcomes.
- **Cons**: Assumes a linear relationship between the features and the log-odds of the outcome.

#### 4.4 **Decision Trees**
- **Best for**: Non-linear relationships, capturing interactions between variables.
- **Pros**: Easy to interpret, handles both numeric and categorical data.
- **Cons**: Prone to overfitting, especially deep trees.

#### 4.5 **Random Forests**
- **Best for**: Reducing overfitting, improving accuracy over decision trees.
- **Pros**: Robust, handles large datasets well.
- **Cons**: Less interpretable, computationally expensive.

#### 4.6 **Support Vector Machines (SVM)**
- **Best for**: High-dimensional data, non-linear decision boundaries (with kernel trick).
- **Pros**: Effective in high dimensions.
- **Cons**: Requires careful parameter tuning, less interpretable.

#### 4.7 **Ensemble Methods (Bagging, Boosting, Stacking)**
- **Bagging (e.g., Random Forest)**: Reduces variance by averaging multiple models.
- **Boosting (e.g., XGBoost)**: Reduces bias by sequentially correcting errors of previous models.
- **Stacking**: Combines multiple models for a final prediction.

---

### 5. **Model Training and Evaluation**

#### 5.1 **Splitting Data**
- **Train/Test Split**: Typically, 70-80% for training, 20-30% for testing.
- **Cross-Validation**: Use k-fold cross-validation to ensure stability in results.

#### 5.2 **Performance Metrics**
- **R-Squared**: Proportion of variance explained by the model.
- **Mean Squared Error (MSE)**: Average squared difference between observed and predicted values.
- **Root Mean Squared Error (RMSE)**: Square root of MSE, interpretable in the same units as the target variable.
- **Mean Absolute Error (MAE)**: Average absolute difference between observed and predicted values.
- **Adjusted R-Squared**: R-Squared adjusted for the number of predictors in the model, useful in multiple regression.

#### 5.3 **Model Tuning**
- **Hyperparameter Tuning**: Use GridSearchCV, RandomizedSearchCV to find the best hyperparameters.
- **Regularization**: Apply techniques like LASSO (L1) and Ridge (L2) to prevent overfitting by penalizing large coefficients.

---

### 6. **Feature Interpretation**

Understanding the model’s predictions is critical, especially in applications requiring transparency.

#### 6.1 **Coefficient Interpretation (Linear Models)**
- **Linear Regression**: Coefficients represent the change in the target variable for a unit change in the predictor.
- **Logistic Regression**: Coefficients represent the change in the log-odds for a unit change in the predictor.

#### 6.2 **Feature Importance**
- **Tree-Based Models**: Feature importance scores can be obtained to understand which features contribute most to the prediction.
- **SHAP Values**: SHapley Additive exPlanations provide a unified measure of feature importance for any model.

#### 6.3 **Partial Dependence Plots**
- **PDP**: Visualize the relationship between a feature and the predicted outcome, holding other features constant.

#### 6.4 **Residual Analysis**
- **Residual Plots**: Analyze the residuals to check the assumptions of the regression model (e.g., homoscedasticity, independence).
- **Influence Plots**: Identify influential data points that have a disproportionate impact on the model.

---

### 7. **Model Deployment**

Once satisfied with the model’s performance:

#### 7.1 **Saving the Model**
- **Serialization**: Use joblib or pickle to save the trained model for future use.

#### 7.2 **Monitoring and Updating**
- **Model Drift**: Regularly monitor the model’s performance on new data and update if necessary.

---

### 8. **Documentation and Reporting**

Ensure that your analysis is well-documented:

#### 8.1 **Code and Workflow Documentation**
- **Jupyter Notebooks**: Use notebooks for code, visualizations, and explanations.
- **Comments and Markdown**: Ensure that your code is well-commented, and explanations are provided in markdown cells.

#### 8.2 **Reporting Results**
- **Executive Summary**: Provide a high-level overview of findings and model performance.
- **Technical Report**: Include detailed descriptions of the methods, results, and interpretations.

---

### 9. **Common Pitfalls**

#### 9.1 **Overfitting**
- Regularization, cross-validation, and pruning can help prevent overfitting.

#### 9.2 **Data Leakage**
- Ensure that the test data is not used in any form during the training process.

#### 9.3 **Bias and Variance Trade-off**
- Strive for a balance; high bias
