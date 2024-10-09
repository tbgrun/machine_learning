# Handling Multi-Colinearity
### 1. Identify Highly Correlated Features
* Pearson Correlation
* Correlation Matrix (e.g., via [Heatmap]())
### 2. Decide which feature is more important
### 3. Remove one feature
#### 3.1 Import Libraries
    import pandas as np
#### 3.2 Drop Selected Feature
    df = df.drop(['colum_name'], axis=1)
