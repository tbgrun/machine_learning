# Train-Validation-Test Splitting
### 1. Import Libraries
    import numpy as np
    from sklearn.model_selection import train_test_split
### 2. Identify Feautures and Target
    X = df.drop(columns='target_column_name') # removes target variable from dataframe
    y = df['target_column_name'] # target
### 3. Split Data
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)  # 40% test set (temp), 60% training set
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)  # splits test set (temp) from above further into 20% validation and 20% test
* **test_size:** defines the fraction of the test set. E.g., 0.2 = 20% of data is test set (therefore 80% is used for training). 0.2 is standard.
* **random_state:** ensures reproducibility.
### 4. Run Model
    model =
    model.fit(X_train, y_train)
    y_val_pred = model.predict(X_val)
    y_test_pred = model.predict(X_test)
### 5. Validation
    val_accuracy = accuracy_score(y_val, y_val_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
