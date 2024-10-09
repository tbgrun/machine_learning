# Handling Multi-Colinearity
### 1. Identify Highly Correlated Features
* Pearson Correlation
* Correlation Matrix (e.g., via [Heatmap](https://github.com/tbgrun/machine_learning/blob/main/01%20-%20Explorative%20Data%20Analysis/07%20-%20Correlations.md#2-heatmap))
### 2. Decide which feature is more important
### 3. Remove one feature
#### 3.1 Import Libraries
    import pandas as np
#### 3.2 Drop Selected Feature
    df = df.drop(['colum_name'], axis=1)
