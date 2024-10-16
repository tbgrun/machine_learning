# Handling Zeros
## 1. Add Constat
Adds a constant to every value in the dataframe
### 1.1 Import Libraries
    import pandas as pd
### 1.2 Run Script
    df = pd.DataFrame(dataframe)
    df_transformed = df + 1
## 2. Replace Zeros with Constant
Replaces only zero-values with a very small constant.
### 2.1 Import Libraries
    import pandas as pd
### 2.2 Replace Zeros
    df = pd.DataFrame(dataframe)
    df = df.replace(0, 1e-10)
## 3. Replace Zeros
Replaces only zero-values with a NaN. Only applicable if zero represent a missing value. Check out ["Handling Missing Values"](https://github.com/tbgrun/machine_learning/blob/main/02%20-%20Data%20Cleaning/01%20-%20Handling%20Missing%20Values.md).
### 3.1 Import Libraries
    import pandas as pd
    import numpy as np
### 3.2 Replace Zeros with NaN
    df = pd.DataFrame(dataframe)
    df = df.replace(0, np.nan)
