# Simple Pipeline
## 1. Pipeline
### 1.1 Import Libraries
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
### 1.2 Identify Feautures and Target
    X = df.drop(columns='target_column_name') # removes target variable from dataframe
    y = df['target_column_name'] # target
### 1.3 Split Data
[see "Split Data" for different techniques](https://github.com/tbgrun/machine_learning/blob/main/03%20-%20Data%20Splitting/00%20-%20Data%20Splitting.md)
    
    X_train, X_test, y_train, y_test =
### 1.4 Run Pipeline
    pipeline = Pipeline([
        ('scaler', scaling_technique), # scale data
        ('classifier', model_name) # fit model
    ])
    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)
### 1.5 Evaluation
    accuracy = pipeline.score(X_test, y_test)
## 2. Pipeline Attributes
### Missing Values
* **PowerTransformer:** Used for applying Box-Cox or Yeo-Johnson transformations.
### Feature Selection
* **SelectKBest:** Selects the k best features according to a scoring function.
* **Binarizer**: Binarizes data (sets values above a threshold to 1, others to 0).
* **VarianceThreshold:** Removes all features whose variance doesn’t meet a certain threshold.
* **RFE** (Recursive Feature Elimination): Recursively removes features and builds a model to identify the best features.
* **SelectFromModel:** Selects features based on importance weights from an estimator.
* **FeatureUnion:** Combines several feature extraction methods into a single pipeline step.
* **PCA** (Principal Component Analysis): Reduces dimensionality by selecting the principal components.
### Feature Engineering
* **PolynomialFeatures:** Generates polynomial and interaction features.
* **NMF** (Non-negative Matrix Factorization): Reduces dimensionality but restricts features and components to be non-negative.
### Encoding
* **LabelEncoder:** Encodes target labels as integers (useful for classification tasks).
* **OneHotEncoder:** Converts categorical values into a one-hot (binary) format.
### Scaling
* **StandardScaler:** Scales features to have mean 0 and standard deviation 1.
* **MinMaxScaler:** Scales features to a fixed range, typically between 0 and 1.
* **MaxAbsScaler:** Scales features to the range [-1, 1], useful for data with sparse values.
* **RobustScaler:** Scales using statistics that are robust to outliers.
* **Normalizer:** Normalizes samples individually to have unit norm.
### Clustering Algorithms (unsupervised pipelines)
* **KMeans:** K-means clustering algorithm.
* **DBSCAN:** Density-based spatial clustering.
* **AgglomerativeClustering:** Hierarchical clustering.
### Model Wrappers
* **VotingClassifier / VotingRegressor:** Combines predictions from multiple models using voting.
* **BaggingClassifier / BaggingRegressor:** Wraps an estimator to train on random subsets of the data.
* **StackingClassifier / StackingRegressor:** Stacks multiple estimators and trains them in parallel.
* **Pipeline:** Pipelines can be nested within pipelines (e.g., a feature engineering pipeline followed by a modeling pipeline).
