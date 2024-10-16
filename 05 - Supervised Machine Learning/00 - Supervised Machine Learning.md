# Supervised Machine Learning
Supervised machine learning involves training a model on a labeled dataset, where the target variable is known. The goal is to predict the target variable for unseen data.

## Workflow

### 1. Data Requirements
#### 1.1 Labeled Data
Supervised learning requires a dataset with input features (X) and a target variable (y). For classification tasks, the target variable should be categorical.
#### 1.2 No Missing Values (NaN)
Machine learning algorithms do not handle missing values well, they need to be eliminated:
  - **Removing** rows or columns with missing values.
  - **Imputing** missing values using techniques like mean, median, mode, or more advanced methods like KNN imputation.
#### 1.3 Balanced Data
For classification, it's important to have a balanced dataset, where each class is equally represented. If the dataset is imbalanced, use a stratified approach in the model, or use:
  - **Resampling techniques:** Over-sampling the minority class (e.g., SMOTE) or under-sampling the majority class.
  - **Adjusting model evaluation metrics:** Metrics like accuracy might be misleading with imbalanced data, so metrics like Precision, Recall, F1-Score, and ROC-AUC are more appropriate.
#### 1.4 Normalized/Standardized Data
  - **Normalization:** Scaling features to a range, typically [0,1].
  - **Standardization:** Centering features around mean 0 with standard deviation 1.
  - **When to normalize/standardize:** Algorithms like k-NN, SVM, and neural networks benefit from normalization/standardization, whereas tree-based methods like Random Forest or Decision Trees generally don't require it.

---

### 2. Exploratory Data Analysis (EDA)
#### 2.1.	Descriptive Statistics
  - **Summary statistics** like mean, median, mode, variance, skewness, and kurtosis for numerical features.
  - **Frequency counts** for categorical features.
#### 2.2.	Data Visualization
  - **Univariate Analysis:** Histograms, box plots, and density plots to understand the distribution of individual features.
  - **Bivariate Analysis:** Scatter plots, pair plots, and correlation matrices to identify relationships between features.
  - **Multivariate Analysis:** Techniques like PCA (Principal Component Analysis) to understand the relationships between multiple features.
#### 2.3.	Identifying Outliers
  - **Box plots**
  - **z-scores**
#### 2.4.	Correlation Analysis
  - **Correlation** matrices to identify multicollinearity between features.
  - **Heatmaps** to visualize correlations.
  - **Note:** For highly correlated features, consider removing one to reduce multicollinearity.

---

### 3. Data Cleaning
#### 3.1.	Handling Missing Data
  - **Remove**: Drop rows or columns with a high percentage of missing values.
  - **Impute:** Replace missing values with statistical measures like mean, median, or mode, or use more advanced techniques like KNN or MICE imputation.
#### 3.2.	Outlier Treatment
  - **Removal:** Remove extreme outliers if they are due to data entry errors.
  - **Transformation:** Apply transformations like log, square root, or box-cox to reduce the impact of outliers.
#### 3.3.	Encoding Categorical Variables
  - **Label Encoding:** Assign a unique number to each category (suitable for ordinal data).
  - **One-Hot Encoding:** Convert categorical variables into binary columns (suitable for nominal data).
#### 3.4.	Feature Engineering:
  - **Interaction Terms:** Create new features by combining existing ones (e.g., multiplication, division).
  - **Polynomial Features:** Create polynomial combinations of features to capture non-linear relationships.
  - **Binning:** Grouping continuous variables into discrete bins.

---

### 4. Choosing the Correct Model
#### 4.1 [**Linear Regression**](https://github.com/tbgrun/machine_learning/blob/main/05%20-%20Supervised%20Machine%20Learning/01.01%20-%20Linear%20Regression.md)
  - **Best for**: When the relationship between features and the target is linear.
  - **Pros**: Simple, interpretable.
  - **Cons**: Sensitive to outliers, assumes linearity.
#### 4.2 **Polynomial Regression**
  - **Best for**: When the relationship is non-linear but can be represented as a polynomial.
  - **Pros**: Captures non-linear relationships.
  - **Cons**: Prone to overfitting with high-degree polynomials.
#### 4.3.	Logistic Regression
  - **Use case:** When the relationship between the features and the target variable is approximately linear.
  - **Pros:** Simple to implement, interpretable coefficients.
  - **Cons:** Assumes linearity, sensitive to outliers.
#### 4.4.	Decision Trees
  - **Use case:** When you need an interpretable model that can capture non-linear relationships.
  - **Pros:** Easy to interpret, handles both numerical and categorical data.
  - **Cons:** Prone to overfitting, especially with deep trees.
#### 4.5.	Random Forest
  - **Use case:** When you need a robust, high-performance model that handles non-linear relationships.
  - **Pros:** Reduces overfitting by averaging multiple trees, handles missing data well.
  - **Cons:** Less interpretable, computationally expensive.
#### 4.6.	Support Vector Machines (SVM)
  - **Use case:** When your data has clear margins of separation between classes.
  - **Pros:** Effective in high-dimensional spaces, robust to overfitting with proper regularization.
  - **Cons:** Computationally expensive, especially with large datasets.
#### 4.7.	k-Nearest Neighbors (k-NN)
  - **Use case:** When you have a small dataset and don't require interpretability.
  - **Pros:** Simple, no training phase.
  - **Cons:** Sensitive to noisy data, computationally expensive during prediction.
#### 4.8.	Naive Bayes
  - **Use case:** When your features are independent, or in text classification problems.
  - **Pros:** Fast, works well with small datasets and text data.
  - **Cons:** Assumes feature independence, which is often unrealistic.
#### 4.9.	Ensemble Methods
  - **Bagging** (e.g., Random Forest): Combines multiple weak models (like decision trees) to reduce variance.
  - **Boosting** (e.g., AdaBoost, XGBoost, Gradient Boosting): Focuses on correcting the errors of previous models by adding models sequentially.
  - **Stacking:** Combines multiple models by training a meta-model on the predictions of the base models.
  - **Use case:** When you need to improve model performance by combining the strengths of multiple models. Pros: Often leads to superior performance, reduces bias or variance depending on the method. Cons: Complex, harder to interpret.

---

### 5. Model Training
#### 5.1.	Splitting the Data
  - **Training Set:** 70-80% of the data for training the model.
  - **Validation Set:** 10-15% of the data for tuning hyperparameters.
  - **Test Set:** 10-15% of the data for evaluating the model's final performance.
#### 5.2.	Model Training
  - **Fit the model** on the training data.
  - **Use cross-validation** (e.g., k-fold cross-validation) to ensure the model generalizes well to unseen data.
  - **Tune hyperparameters** on the validation set.
    - Grid Search
    - Random Search
    - Bayesian Optimization
#### 5.3.	Evaluate
  - Evaluate each combination using cross-validation.

---

### 6. Performance Metrics
#### 6.1.	Accuracy
  - The proportion of correct predictions out of the total predictions.
  - **Limitation:** Misleading with imbalanced data.
#### 6.2.	Precision, Recall, and F1-Score
  - **Precision:** The proportion of true positive predictions out of all positive predictions.
  - **Recall:** The proportion of true positives out of all actual positives.
  - **F1-Score:** The harmonic mean of Precision and Recall, providing a balance between them.
#### 6.3.	ROC-AUC (Receiver Operating Characteristic - Area Under Curve)
  - **ROC Curve:** Plots True Positive Rate (Recall) against False Positive Rate.
  - **AUC:** The area under the ROC curve. A value close to 1 indicates a good model.
#### 6.4.	Confusion Matrix
  - A table showing the counts of true positives, true negatives, false positives, and false negatives.
#### 6.5.	Log Loss
  - Measures the uncertainty of the predictions. Lower values indicate better performance.
#### 6.6.	Cohen’s Kappa
  - Measures the agreement between the predicted and actual labels, adjusted for chance.

---

### 7. Feature Interpretation
#### 7.1.	Feature Importance
  - For tree-based models like Random Forest, feature importance scores can be extracted to understand which features contribute most to the model.
#### 7.2.	SHAP Values (SHapley Additive exPlanations)
  - Provides a consistent way to interpret the impact of features on the predictions. SHAP values show how much each feature contributes to pushing the model’s prediction from the baseline.
#### 7.3.	Partial Dependence Plots (PDPs)
  - Visualizes the relationship between a feature and the predicted outcome, holding other features constant.
#### 7.4.	LIME (Local Interpretable Model-agnostic Explanations)
  - Explains individual predictions by approximating the model locally with an interpretable model.

----

### 8. Model Validation and Testing
#### 8.1.	Test Set Evaluation
  - Apply the trained model to the test set and evaluate using the chosen performance metrics.
#### 8.2.	Overfitting Check
  - Compare the performance on the training and test sets. Significant differences indicate overfitting.
  - Techniques to mitigate overfitting include regularization (L1, L2), pruning (for decision trees), and early stopping (for boosting models).

---

### 9. Model Deployment
#### 9.1.	Serialization
  - Save the trained model using libraries like joblib or pickle in Python for later use.
#### 9.2.	Integration
  - Integrate the model into production systems via APIs, batch processing, or real-time prediction systems.
#### 9.3.	Monitoring
  - Continuously monitor the model's performance in production to detect any drift in data or decrease in performance over time.
  - Retrain the model periodically with new data if necessary.
