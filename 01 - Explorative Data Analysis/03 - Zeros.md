# Zeros
### 1. Identify zeros in dataframe
#### 1.1 Import Libraries
    import pandas as pd
#### 1.1 Identifies if any value in the dataframe is a zero
    df = pd.DataFrame(dataframe)
    print((df == 0).any().any())
#### 1.2 Identifies which column contains zeros
    df = pd.DataFrame(dataframe)
    df_zeros = (df == 0).stack()
    print(df_zeros[df_zeros]) # filteres only columns where zeros are present 
#### 1.3 Identifies numbers of zeros in each column
    df = pd.DataFrame(dataframe)
    print((df==0).sum())
#### 1.4 Identifies which value is a zero in the dataframe
    df = pd.DataFrame(dataframe)
    print(df == 0)

[klick here to get to "Handling Zeros"](https://github.com/tbgrun/machine_learning/blob/main/02%20-%20Data%20Cleaning/02%20-%20Handling%20Zeros)
