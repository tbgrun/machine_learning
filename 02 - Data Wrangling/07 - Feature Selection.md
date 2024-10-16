# Feature Selection
## 1. Low Varianve
### 1.1 Import Libraries
    import pandas as pd
    from sklearn.feature_selection import VarianceThreshold
### 1.2 Remove Low Variance Features
    df = pd.DataFrame(dataframe)
    selector = VarianceThreshold(threshold=x) # e.g., x=.1. Low treshold = removal of constant features
    df_LVF_dropped = selector.fit_transform(df)
## 2. Multi-Colinearity
[see "Handling Multi-Colinearity"](https://github.com/tbgrun/machine_learning/blob/main/02%20-%20Data%20Wrangling/07%20-%20Handling%20Multi-Colinearity.md)
## 3. Principal Component Analysis
### 3.1 Import Libraries
    import pandas as pd
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
### 3.2 Run PCA
    df = pd.DataFrame(dataframe)
    scaler = StandardScaler() # initiate StandardScaler
    df_scaled = scaler.fit_transform(df) # scale data
    pca = PCA(n_components=n) # run PCA, n=number of components
    df_reduced = pca.fit_transform(df_scaled)
## 4. Permutation
### 4.1 Import Libraries
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    from sklearn.inspection import permutation_importance
### 4.2 Run Permutation
    df = pd.DataFrame(data)
    X = data_transformed.drop('target_column_name', axis=1) # seperating features from target variable
    y = data_transformed['target_column_name'] # identifying target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) # split data in train and test data
    model = RandomForestClassifier(random_state=42) # initiate model
    model.fit(X_train, y_train) # fit model to data
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) # calculate accuracy
    permutation = permutation_importance(model, X_test, y_test, n_repeats=10, random_state=42) # run permutation
    for i in permutation.importances_mean.argsort()[::-1]: # output results
        if permutation.importances_mean[i] > 0:
            print(f"Feature: {X.columns[i]}, Importance: {permutation.importances_mean[i]:.4f}")
