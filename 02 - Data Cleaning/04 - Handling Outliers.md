# Handling Outliers
## 1. Interquartile Range (IQR)
### 1.1. Remove Outliers
#### 1.1.1 Import Libraries
    import pandas as pd
#### 1.1.2 Remove Outliers (see ["xxx
 df_outliers_removed = df[(df['column_name'] >= lower_bound) | (df['column_name'] <= upper_bound)]


## 2. Z-Scores
### 2.1. Remove Outliers
#### 2.1.1 Import Libraries
    import pandas as pd
#### 2.1.2 Remove Outliers
    df_outliers_removed = df[df['z_scores'] <= 3]
### 2.2 Impute Outliers
#### 2.2.1 Import Libraries
    import pandas as pd
#### 2.2.2a Impute Mean
    feature_mean = df['column_name_to_be_imputed'].mean()
    df_outlier_imputed['column_name_to_be_imputed'] = df['column_name_to_be_imputed'].where(df['z_scores'] > 3, feature_mean)
#### 2.2.2b Impute Median
    feature_median = df['column_name_to_be_imputed'].median()
    df_outlier_imputed['column_name_to_be_imputed'] = df['column_name_to_be_imputed'].where(df['z_scores'] > 3, feature_median)
#### 2.2.2c Impute Mode
    feature_mode = df['column_name_to_be_imputed'].mode()
    df_outlier_imputed['column_name_to_be_imputed'] = df['column_name_to_be_imputed'].where(df['z_scores'] > 3, feature_mode)
