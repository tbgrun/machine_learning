# Stratified Splitting
### 1. Import Libraries
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
### 2. Identify Features and Target
    X = df.drop(columns='target_column_name') # removes target variable from dataframe
    y = df['target_column_name'] # target
### 3. Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
### 4. Run Model
    model =
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
### 5. Validation
    accuracy = accuracy_score(y_test, y_pred)
