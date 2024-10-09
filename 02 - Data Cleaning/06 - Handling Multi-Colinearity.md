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
PCA automatically linear combines correlated features.
#### 3.1.1 Import Libraries
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    import pandas as pd
#### 3.1.2 Seperate Feature from Target
    X = df.drop('target_column', axis=1)  # removing target variable results in features dataframe
    y = df['target_column']  # target variable
#### 3.1.3 Standardize Features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
#### 3.1.4 Run PCA
    pca = PCA(n_components=n)  # reduces data to n components
    dimension_reduced_df = pca.fit_transform(Xscaled) # scaled dataframe reduced to n components
#### 3.1.5 Feature Importance
    loadings = pca.components_ # shows the importance of each feature
    loadings_df = pd.DataFrame(loadings.T, columns=[f'PC{i+1}' for i in range(loadings.shape[0])], index=X.columns)
    explained_variance = pca.explained_variance_ratio_ # calculates how much variance each principal component explains
    
