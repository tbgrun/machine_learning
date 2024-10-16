# K-Fold Cross-Validation
### 1. Import Libraries
    import numpy as np
    from sklearn.model_selection import KFold
    from sklearn.metrics import accuracy_score
### 2. Identify Feautures and Target
    X = df.drop(columns='target_column_name') # removes target variable from dataframe
    y = df['target_column_name'] # target
### 3. Split
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
### 4. Run Model
    model =
### 5. Coss-Validation
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
