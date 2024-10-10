# Handling Zeros
## 1. Add Constat
Add constant to every value in the dataframe
### 1.1 Import Libraries
    import pandas as pd
### 1.2 Run Script
    df = pd.DataFrame(dataframe)
    df_transformed = df + 1
## 2. Replace Zeros with Constant
Replace zero-values with a very small constant.
### 2.1 Import Libraries
    import pandas as pd
### 2.2 Replace Zeros
    df = pd.DataFrame(dataframe)
    df = df.replace(0, 1e-10)
## 2. Replace Zeros
Replace zero-values with a NaN. Only applicable if zero represent a missing value.
### 2.1 Import Libraries
    import pandas as pd
    import numpy as np
### 2.2 Replace Zeros with NaN
    df = pd.DataFrame(dataframe)
    df = df.replace(0, np.nan)
