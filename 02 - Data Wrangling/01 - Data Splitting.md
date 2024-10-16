# Data Splitting
## 1. Train-Test
### 1.1 Import Libraries
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
### 1.2 Identify Feautures and Target
    X = df.drop(columns='target_column_name') # removes target variable from dataframe
    y = df['target_column_name'] # target
### 1.3 Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
* **test_size:** defines the fraction of the test set. E.g., 0.2 = 20% of data is test set (therefore 80% is used for training). 0.2 is standard.
* **random_state:** ensures reproducibility.
## 2. Train-Validation-Test
### 2.1 Import Libraries
    import numpy as np
    from sklearn.model_selection import train_test_split
### 2.2 Identify Feautures and Target
    X = df.drop(columns='target_column_name') # removes target variable from dataframe
    y = df['target_column_name'] # target
### 2.3 Split
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)  # 40% test set (temp), 60% training set
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)  # splits test set (temp) from above further into 20% validation and 20% test
* **test_size:** defines the fraction of the test set. E.g., 0.2 = 20% of data is test set (therefore 80% is used for training). 0.2 is standard.
* **random_state:** ensures reproducibility.
## 3. K-Fold Cross-Validation
### 3.1 Import Libraries
    import numpy as np
    from sklearn.model_selection import KFold
    from sklearn.metrics import accuracy_score
### 3.2 Identify Feautures and Target
    X = df.drop(columns='target_column_name') # removes target variable from dataframe
    y = df['target_column_name'] # target
### 3.3 Split
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
### 3.4 Run Model
    model =
### 3.5 Perform Cross-Validation
    fold_accuracies = []
    fold = 1
    for train_index, test_index in kf.split(X): # split data into training and test sets for the current fold
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        model.fit(X_train, y_train) # train model
        y_pred = model.predict(X_test) # prediction on test set
        accuracy = accuracy_score(y_test, y_pred) # calculate accuracy
        fold_accuracies.append(accuracy)
        print(f"Fold {fold}: Accuracy = {accuracy:.4f}") # print accuracies
        fold += 1
    mean_accuracy = np.mean(fold_accuracies) # calculate mean accuracy across all folds
    std_accuracy = np.std(fold_accuracies) # calculate standard deviation for accuracy across all folds
