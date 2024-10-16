# Train-Test Splitting
### 1. Import Libraries
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
### 2. Identify Feautures and Target
    X = df.drop(columns='target_column_name') # removes target variable from dataframe
    y = df['target_column_name'] # target
### 3. Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
* **test_size:** defines the fraction of the test set. E.g., 0.2 = 20% of data is test set (therefore 80% is used for training). 0.2 is standard.
* **random_state:** ensures reproducibility.
### 4. Run Model
    model =
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
### 5. Validation
    accuracy = accuracy_score(y_test, y_pred)
