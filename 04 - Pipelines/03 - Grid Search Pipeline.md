# Grid Search Pipeline
## 1. Pipeline
### 1.1 Import Libraries
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import GridSearchCV
### 1.2 Identify Feautures and Target
    X = df.drop(columns='target_column_name') # removes target variable from dataframe
    y = df['target_column_name'] # target
### 1.3 Split Data
[see "Split Data" for different techniques](https://github.com/tbgrun/machine_learning/blob/main/03%20-%20Data%20Splitting/00%20-%20Data%20Splitting.md)
    
    X_train, X_test, y_train, y_test =
### 1.4 Run Pipeline (example)
    grid_pipeline = Pipeline([
        ('scaler', scaling_technique), # scale data
        ('classifier', model) # chose classifier (model)
    ])
    search_parameter = {
        'parameter_1': [x1, x2, x3], # placeholder for nummeric parameter
        'parameter_n': ['x1', 'x1'] # placeholder for string parameter
    }
    grid_search = GridSearchCV(grid_pipeline, search_parameter, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
### 1.5 Evaluation
    y_pred = grid_search.best_estimator_.predict(X_test)
## 2. Search Parameters
### PCA (Principal Component Analysis)
* **pca__n_components:** The number of principal components to keep.
* **values to try:** [2, 3, 4], or a range based on the number of features.
### Logistic Regression
* **classifier__C:** Inverse of regularization strength. Smaller values specify stronger regularization.
  * **values to try:** [0.01, 0.1, 1, 10, 100]
* **classifier__penalty:** The norm used in the penalization (L1 or L2).
  * **values to try:** ['l1', 'l2', 'elasticnet', 'none']
  * **note:** L1 works with liblinear, L2 works with lbfgs or newton-cg.
* **classifier__solver:** Algorithm to use in the optimization problem.
  * **values to try:** ['liblinear', 'lbfgs', 'newton-cg', 'sag', 'saga']
* **classifier__max_iter:** Maximum number of iterations for the solver to converge.
  * **values to try:** [100, 200, 300]
### Random Forest
* **classifier__n_estimators:** The number of trees in the forest.
  * **values to try:** [50, 100, 200, 500]
* **classifier__max_depth:** Maximum depth of the trees.
  * **values to try:** [10, 20, 30, None]
* **classifier__min_samples_split:** Minimum number of samples required to split an internal node.
  * **values to try:** [2, 5, 10]
* **classifier__min_samples_leaf:** Minimum number of samples required to be at a leaf node.
  * **values to try:** [1, 2, 4]
* **classifier__max_features:** The number of features to consider when looking for the best split.
  * **values to try:** ['auto', 'sqrt', 'log2']
### SVC (Support Vector Classifier)
* **classifier__C:** Regularization parameter.
  * **values to try:** [0.1, 1, 10, 100]
* **classifier__kernel:** Specifies the kernel type to be used in the algorithm.
  * **values to try:** ['linear', 'poly', 'rbf', 'sigmoid']
* **classifier__gamma:** Kernel coefficient (used with RBF, poly, sigmoid kernels).
  * **values to try:** [0.001, 0.01, 0.1, 1]
* **classifier__degree:** Degree of the polynomial kernel function (only relevant for poly kernel).
  * **values to try:** [2, 3, 4, 5]
### KNeighborsClassifier
* **classifier__n_neighbors:** Number of neighbors to use.
  * **values to try:** [3, 5, 7, 9]
* **classifier__weights:** Weight function used in prediction.
  * **values to try:** ['uniform', 'distance']
* **classifier__metric:** The distance metric to use for the tree.
  * **values to try:** ['euclidean', 'manhattan', 'minkowski']
