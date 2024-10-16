# Data Splitting
## 1. Train-Test Splitting
### 1.1 Import Libraries
    import numpy as np
    from sklearn.model_selection import train_test_split
### 1.2 Identify Feautures and Target
    X = df.drop(columns='target_column_name') # removes target variable from dataframe
    y = df['target_column_name'] # target
### 1.3 Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
