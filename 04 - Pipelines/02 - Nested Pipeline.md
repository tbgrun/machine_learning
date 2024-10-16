# Nested Pipeline
## 1. Pipeline
### 1.1 Import Libraries
   from sklearn.compose import ColumnTransformer
   from sklearn.preprocessing import StandardScaler, OneHotEncoder
   from sklearn.pipeline import Pipeline
   from sklearn.model_selection import train_test_split
   from sklearn.decomposition import PCA
### 1.2 Identify Feautures and Target
    X = df.drop(columns='target_column_name') # removes target variable from dataframe
    y = df['target_column_name'] # target
### 1.3 Split Data
[see "Split Data" for different techniques](https://github.com/tbgrun/machine_learning/blob/main/03%20-%20Data%20Splitting/00%20-%20Data%20Splitting.md)
    
    X_train, X_test, y_train, y_test =
### 1.4 Run Pipeline (example)
    numeric_transformer = Pipeline(steps=[ # create a pipeline for numeric features: scaling and PCA
        ('scaler', StandardScaler()),  # scale numeric features
        ('pca', PCA(n_components=2))   # apply PCA on numeric features
    ])
    categorical_transformer = Pipeline(steps=[ # create a pipeline for categorical features: one-hot encoding
        ('onehot', OneHotEncoder())    # one-hot encode categorical features
    ])
    preprocessor = ColumnTransformer( # combine numeric and categorical transformers in a ColumnTransformer
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ]
    )
    nested_pipeline = Pipeline(steps=[ # combine the preprocessor and the final classifier in a nested pipeline
        ('preprocessor', preprocessor),      # nested preprocessor pipeline
        ('classifier', LogisticRegression()) # final classifier
    ])
    nested_pipeline.fit(X_train, y_train) # fit nested pipeline
    y_pred = nested_pipeline.predict(X_test)
### 1.5 Evaluation
    accuracy = nested_pipeline.score(X_test, y_test)
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
