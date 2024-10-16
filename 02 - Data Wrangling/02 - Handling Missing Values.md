# Handling Missing Values
### 2.1 Remove rows or columns
#### 2.1.1 Import Libraries
    import pandas as pd
#### 2.1.2 Run Script
    df.dropna()
### 2.2 Impute Missing Values
#### Impute single columns
##### 2.2.1 Import Libraries
    import pandas as pd
##### 2.2.2 Run Script
###### 2.2.2a Impute using mean
    df['column_name_1'] = df['column_name_1'].fillna(df['column_name_1'].mean())
###### 2.2.2b Impute using median
    df['column_name_1'] = df['column_name_1'].fillna(df['column_name_1'].median())
#### 2.3 Impute on dataframe
Imputes missing values based on data type in all columns of the dataframe
##### 2.3.1 Import Libraries
    import pandas as pd
    from sklearn.compose import ColumnTransformer
    from sklearn.impute import SimpleImputer
##### 2.3.2 Run Impute
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', SimpleImputer(strategy='mean'), df.select_dtypes(include=['number']).columns),
            ('cat', SimpleImputer(strategy='most_frequent'), df.select_dtypes(include=['object']).columns),
        ],
        remainder='passthrough'
    )

    # Fit and transform the data
    df_imputed = pd.DataFrame(preprocessor.fit_transform(df), columns=df.columns)
    df_imputed
Impute strategies:
- **mean:** normal distributed data
- **median:** skewed numerical data
- **most frequent:** categorial data
- **constatnt:** fills in a specific constant value (e.g., True/False for booleans)
