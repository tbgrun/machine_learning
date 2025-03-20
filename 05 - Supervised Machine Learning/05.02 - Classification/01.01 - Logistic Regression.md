# Logistic Regression
### 1. Import Libraries
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, roc_auc_score
### 2. Identify Feature and Target Variables
    X = df.drop(columns='target_column_name') # features
    y = df['target_column_name'] # target
### 3. Split Data into Train and Test Sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
### 4. Process Data
    scaler = StandardScaler() # initiate StandardScaler
### 5. Train Data
    X_train_scaled = scaler.fit_transform(X_train) # fit and transform train data
    X_test_scaled = scaler.transform(X_test) # transform test data
### 6. Run Linear Regression Model
    log_reg = LogisticRegression() # initiate regression model
    log_reg.fit(X_train_scaled, y_train) # train model
    y_pred = log_reg.predict(X_test_scaled) # predict data
### 7. Fine Tuning
    log_reg_tuned = LogisticRegression(max_iter=200, penalty='l2', C=1.0, solver='lbfgs')
    log_reg_tuned.fit(X_train_scaled, y_train)
    y_pred_tuned = log_reg_tuned.predict(X_test_scaled)
* **max_iter:** maximum number of iterations.
* **penalty:** defines type of regularization. Options: l1, l2, elastic, none. l2 is default.
* **C:** controls the strength of regularization. Lower values (c=0.1) apply stronger regularization (reduce model complexity, prevent overfitting). Higher values (c=100) apply less regularization (capture more complex data, prone to overfitting).
* **solver:** defines the algorithm used for search. Options: lbfgs, liblinear, sag, saga. Default is lbfgs.
### 8. Hyperparameter Tuning
    parameter_grid = { # define hyperparameter
        'C': [0.1, 1, 10, 100],
        'penalty': ['l2'],
        'solver': ['lbfgs', 'liblinear'],
        'max_iter': [100, 200, 300]
    }
    grid_search = GridSearchCV(LogisticRegression(), parameter_grid, cv=5, scoring='accuracy') # initiate gridsearch cv
    grid_search.fit(X_train_scaled, y_train) # train model
    print("Best Hyperparameters: ", grid_search.best_params_) # identify best hyperparameter
    best_model = grid_search.best_estimator_ # run model with best hyperparameter
    y_pred_best = best_model.predict(X_test_scaled) # predict values
### 9. Evaluate Model
[klick here to get to "Performance Metrics Overview"](https://github.com/tbgrun/machine_learning/blob/main/99%20-%20Supplementary%20Materials/01%20-%20Performance%20Metrics%20Overview.md)

    y_pred = best_model.predict(X_test_scaled) # evaluates on grid search model (best_model.predict). Use log_reg.predict for untuned model and log_reg_tuned for tuned model
##### 9.1 Accuracy
    accuracy = accuracy_score(y_test, y_pred)
##### 9.2 Confusion Matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:\n", conf_matrix)
     plt.figure(figsize=(6, 4))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()
##### 9.3 Precision, Recall, F1-Score
    class_report = classification_report(y_test, y_pred)
    print("Classification Report:\n", class_report)
##### 9.4 ROC / AUC Score
    y_pred_proba = best_model.predict_proba(X_test_scaled)[:, 1]  # probabilities for positive class
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
    auc_score = roc_auc_score(y_test, y_pred_proba)
    plt.figure(figsize=(6, 4))
    plt.plot(fpr, tpr, color='orange', label=f'ROC curve (AUC = {auc_score:.4f})')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--', label='No Skill')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend()
    plt.show()
    print(f"AUC Score: {auc_score:.4f}")
### 10. Feature Importance Analysis
    coefficients = best_model.coef_[0] # Returns feature importance coefficients. evaluates on grid search model (best_model.predict)
    for i, v in enumerate(coefficients):
        print(f"Feature: {X.columns[i]}, Score: {v}")
- Features with higher coefficients are more important
