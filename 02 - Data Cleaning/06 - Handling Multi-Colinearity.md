# Handling Multi-Colinearity
## 1. Remove Feature
### 1.1. Identify Highly Correlated Features
* Pearson Correlation
* Correlation Matrix (e.g., via [Heatmap](https://github.com/tbgrun/machine_learning/blob/main/01%20-%20Explorative%20Data%20Analysis/07%20-%20Correlations.md#2-heatmap))
### 1.2. Decide which feature is more important
### 1.3. Remove one feature
#### 1.3.1 Import Libraries
    import pandas as np
#### 1.3.2 Drop Selected Feature
    df = df.drop(['colum_name'], axis=1)
## 2. Feature Engineering
### 2.1. Identify Highly Correlated Features
* Pearson Correlation
* Correlation Matrix (e.g., via [Heatmap](https://github.com/tbgrun/machine_learning/blob/main/01%20-%20Explorative%20Data%20Analysis/07%20-%20Correlations.md#2-heatmap))
### 2.2 Combine features via [Feature Engineering](https://github.com/tbgrun/machine_learning/blob/main/02%20-%20Data%20Cleaning/08%20-%20Feature%20Engineering.md)
## 3. Dimension Reduction
### 3.1. Principal Component Analysis
PCA automatically combines correlated features
#### 3.1.1 Import Libraries
    from sklearn.decomposition import PCA
#### 3.1.2 Run PCA
    pca = PCA(n_components=n)  # reduces data to n components
    dimension_reduced_df = pca.fit_transform(df) # dataframe reduced to n components
