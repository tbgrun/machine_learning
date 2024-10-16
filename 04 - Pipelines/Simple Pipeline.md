# Simple Pipeline
### 1. Import Libraries
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
### 2. Identify Feautures and Target
    X = df.drop(columns='target_column_name') # removes target variable from dataframe
    y = df['target_column_name'] # target
### 3. Split Data
[see "Split Data" for different techniques](https://github.com/tbgrun/machine_learning/blob/main/03%20-%20Data%20Splitting/00%20-%20Data%20Splitting.md)
    X_train, X_test, y_train, y_test =
### 4. Run Pipeline
    pipeline = Pipeline([
        ('scaler', scaling_technique), # scale data
        ('classifier', model_name) # fit model
    ])
    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)
### 5. Evaluation
    accuracy = pipeline.score(X_test, y_test)
