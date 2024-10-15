Dank fü# Feature Engineering
## 1. Feature Construction
### 1.1 Interaction
#### 1.1.1 Import Libraries
    import pandas as pd
#### 1.1.2b Feature Addition
    df['new_feature'] = df['feature1']+* df['feature2']
#### 1.1.2b Feature Multiplication
    df['new_feature'] = df['feature1'] * df['feature2']
#### 1.1.2c Feature Ratio
    df['new_feature'] = df['feature1'] / df['feature2']
### 1.2 Polynomial Features
#### 1.2.1 Import Libraries
    import pandas as pd
    from sklearn.preprocessing import PolynomialFeatures
#### 1.2.2 Create Polynomial Feature
    poly = PolynomialFeatures(degree=x, include_bias=False) # initiates polynomial feature to degree x
    polynomial_features = poly.fit_transform(df) # fits data to create features
    df_polynomialfeature = pd.DataFrame(polynomial_features, columns=poly.get_feature_names_out(df.columns)) # creates dataframe with new features
**Degree**
* x=1: linear
* x=2: quadratic
* x=3: cubic
* x>3: higher degrees
* x=.5: square root (also to reduce skewness of positively skewed data)
* x=negative: when relationship between feature and target is inverse

**Include bias**
* True: adds an intercept column with 1s. It improves accuracy by shifting the predictions vertically. Useful if regression model does not feature intercept on its own.
* False: does not add 1s, Chose when regression model already includes an intercept term. Most models in scikit-learn (if 'fit_intercept' attribut is present, it contains an intercept term)


## 2. Dimension Reduction
