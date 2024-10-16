# Outliers
## 1. Interquartile Range (IQR)
The IQR method identifies outliers by looking at the range within which the central 50% of the data lies.
import pandas as pd
### 1.1 Import Libraries
    import numpy as np
    import pandas as pd
### 1.2 Run Outlier Identification
    q1 = df['column_name'].quantile(0.25) # calculate q1 (25th percentile)
    q3 = df['column_name'].quantile(0.75) # calculate q3 (75th percentile)
    iqr = q3 - q1 # calculate IQR
    lower_bound = q1 - 1.5 * iqr # define lower boundary
    upper_bound = q3 + 1.5 * iqr # define upper boundary
    outliers = df[(df['column_name'] < lower_bound) | (df['column_name'] > upper_bound)] # identify outliers
    print(outliers)
### 1.3 Visualization
    import matplotlib.pyplot as plt
    plt.boxplot(data)
    plt.show()
* Boxplot is by default 1.5x IQR
## 2. Z-Score
The Z-score method measures how many standard deviations a data point is from the mean. A Z-score above 3 or below -3 is considered an outlier.
### 2.1 Import Libraries
    import numpy as np
    from scipy import stats
### 2.2 Run Outlier Identification
    df['z_score'] = (df['value'] - df['value'].mean()) / df['value'].std() # calculates z-score
    outliers = df[np.abs(df['z_score']) > 3] # identify outliers
    print(outliers)
## 3. Modified Z-Score
This method is robust for smaller datasets and uses the median and median absolute deviation (MAD) instead of mean and standard deviation.
import pandas as pd
### 3.1 Import Libraries
    import numpy as np
    import pandas as pd
### 3.2 Run Outlier Identification
    median = df['value'].median() # calculate median
    MAD = np.median(np.abs(df['value'] - median)) # calculate MAD
    df['modified_z_score'] = 0.6745 * (df['value'] - median) / MAD # calculate modified z-scores
    outliers = df[np.abs(df['modified_z_score']) > 3.5] # identify outliers
    print(outliers)

[klick here to get to "Handling Outliers"](https://github.com/tbgrun/machine_learning/blob/main/02%20-%20Data%20Wrangling/04%20-%20Handling%20Outliers.md)
