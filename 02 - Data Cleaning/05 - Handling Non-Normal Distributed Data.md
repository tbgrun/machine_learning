# Handling Non-Normal Distributed Data
## 1. Log Transformation
### 1.1 Requirements
* No zeros [klick here to handle zeros]
* No negative values [klick here to handle negative values]
### 1.2 Import Libraries
    import numpy as np
### 1.3 Run Log-Transformation
    data_transformed = np.log(data)
## 2. BoxCox Transformation SCIPY
### 2.1 Requirements
* Zeros allowed
* No negative values [klick here to handle negative values]
### 2.2 Import Libraries
    from scipy.stats import boxcox
### 2.3 Run BoxCox-Transformation
    data_transformed, lambda = boxcox(data)
  * lambla = 1: no transformation (baseline)
  * lambda = 0: log transformation (positively skewed data with large range)
  * lambda = .5: square root transformation (moderately skewed data, counts)
  * lambda = 2: square transformation (centers on large values)
  * lambda = negative: inverts transformation
  * lambda = optimal_lambda: internally calculates maximum likelihood estimation (best approximation)
### 2.4 Reverse BoxCox Transformation
    from scipy.special import inv_boxcox
    data, lambda = inv_boxcox(data_transformed)
## 3. BoxCox Transformation SCIKIT-LEARN
  * Pipeline compatible
  * standardize=True: transform to data with a mean of 0 and variance of 1
      * Improves model performance
      * Reduces sensitivity to outliers
      * Good if fed into distance based models (e.g., KNN and SVM)
### 3.1 Requirements
* Zeros allowed
* No negative values [klick here to handle negative values]
### 3.2 Import Libraries
    from sklearn.preprocessing import PowerTransformer
### 3.3 Run BoxCox-Transformation
    pt_standardized = PowerTransformer(method='box-cox', standardize=True)
    transformed_data_standardized = pt_standardized.fit_transform(data.reshape(-1, 1)) 
## 4. Yeo-Johnson Transformation
### 4.1 Requirements
* Zeros allowed
* Negative values allowed
### 4.2 Import Libraries
    from sklearn.preprocessing import PowerTransformer
### 4.3 Run Yeo-Johnson Transformation
    pt = PowerTransformer(method='yeo-johnson')
    data_transformed = pt.fit_transform(data.reshape(-1, 1))
