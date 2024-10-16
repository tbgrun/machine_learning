# Handling Outliers
[Check "EDA: Outliers" for outlier identification](https://github.com/tbgrun/machine_learning/blob/main/01%20-%20Explorative%20Data%20Analysis/05%20-%20Outliers.md)
## 1. Interquartile Range (IQR)
### 1.1 Remove Outliers
#### 1.1.1 Import Libraries
    import pandas as pd
#### 1.1.2 Remove Outliers
    df_outliers_removed = df[(df['column_name'] >= lower_bound) & (df['column_name'] <= upper_bound)]
### 1.2 Impute Outliers
#### 1.2.1 Import Libraries
    import pandas as pd
#### 1.2.2a Impute Mean
    feature_mean = df['column_name_to_be_imputed'].mean()
    df_outlier_imputed['column_name_to_be_imputed'] = df['column_name_to_be_imputed'].where((df['column_name'] >= lower_bound) & (df['column_name'] <= upper_bound), feature_mean))
#### 1.2.2b Impute Median
    feature_median = df['column_name_to_be_imputed'].median()
    df_outlier_imputed['column_name_to_be_imputed'] = df['column_name_to_be_imputed'].where((df['column_name'] >= lower_bound) & (df['column_name'] <= upper_bound), feature_median))
#### 1.2.2c Impute Mode
    feature_mode = df['column_name_to_be_imputed'].mode()
    df_outlier_imputed['column_name_to_be_imputed'] = df['column_name_to_be_imputed'].where((df['column_name'] >= lower_bound) & (df['column_name'] <= upper_bound), feature_mode))
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
## 3. Z-Scores
### 3.1. Remove Outliers
#### 3.1.1 Import Libraries
    import pandas as pd
#### 3.1.2 Remove Outliers
    df_outliers_removed = df[df['modified_z_scores'] <= 3.5]
### 3.2 Impute Outliers
#### 3.2.1 Import Libraries
    import pandas as pd
#### 3.2.2a Impute Mean
    feature_mean = df['column_name_to_be_imputed'].mean()
    df_outlier_imputed['column_name_to_be_imputed'] = df['column_name_to_be_imputed'].where(df['modified_z_scores'] > 3.5, feature_mean)
#### 3.2.2b Impute Median
    feature_median = df['column_name_to_be_imputed'].median()
    df_outlier_imputed['column_name_to_be_imputed'] = df['column_name_to_be_imputed'].where(df['modified_z_scores'] > 3.5, feature_median)
#### 3.2.2c Impute Mode
    feature_mode = df['column_name_to_be_imputed'].mode()
    df_outlier_imputed['column_name_to_be_imputed'] = df['column_name_to_be_imputed'].where(df['modified_z_scores'] > 3.5, feature_mode)
