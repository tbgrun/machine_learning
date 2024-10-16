# Scaling
## 1. Min-Max Scaling (Normalization)
### 1.1 Import Libraries
    from sklearn.preprocessing import MinMaxScaler
### 1.2 Scaling
    scaler = MinMaxScaler() # initiate MinMaxScaler
    normalized_data = scaler.fit_transform(data)
* Transforms data to be in the range [0, 1]
**Use cases:**
* Model algorithm relies on distance metrics (e.g., k-NN, SVM, K-means)
* Bounded range of data (e.g., percentages)
## 2. Standardization (Z-Score Normalization)
### 2.1 Import Libraries
    import numpy as np
    from sklearn.preprocessing import StandardScaler
### 2.2 Scaling
    scaler = StandardScaler() # initiata StandardScaler
    standardized_data = scaler.fit_transform(data)
* Transforms data to have a mean of 0 and a standard deviation of 1
**Use cases:**
* Model algorithm relies on normally distributed data (e.g., regressions, PCA)
* Features with different Units (e.g., percentages)
