# Normal Distribution
## 1. Q-Q Plot
### 1.1 Import Libraries
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy import stats
### 1.2 Plot Data
    stats.probplot(data, dist="norm", plot=plt)
    plt.show()
## 2. Shapiro-Wilk Test
Sensitive to center of distribution, as well as to skewness and kurtosis.
### 2.1 Import Libraries
    import numpy as np
    from scipy import stats
### 2.2 Run Test
    stat, p_value = shapiro(df['column_name'])
    print(stat, p_value)
If p_value > alpha: fail to reject H0 (data is normal)
## 3. Anderson-Darling Test
Sensitive to tails of distribution.
### 3.1 Import Libraries
    import pandas as pd
    import numpy as np
    from scipy import stats
### 3.2 Run Test
    anderson_result = stats.anderson(data, dist='norm')
    statistic = anderson_result.statistic
    critical_values = anderson_result.critical_values
    significance_level = anderson_result.significance_level
If "statistic" is greater than "critical_value" at given "significance_level" then reject H0 (= data does not follow normal distribution).
