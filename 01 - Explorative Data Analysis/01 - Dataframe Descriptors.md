# Dataframe Descriptors
### 1. Dataframe Info
Provides information about number of columns and number of rows in a dataframe.
#### 1.1 Import Libraries
    import pandas as pd
#### 1.2 Show Data Properties
    rows, columns = df_tips_raw.shape
    print(f'number of rows: {rows}, number of columns: {columns}')
### 2. Data Properties
Provides information about the data type of each column and amount of non-zero values.
#### 2.1 Import Libraries
    import pandas as pd
#### 2.2 Show Data Properties
    df.info()
### 3. Statistic Summary
Provides basic statistics (e.g., counts, mean, std, quartiles, etc.) of each column.
#### 3.1 Import Libraries
    import pandas as pd
#### 3.2 Run Statistics
    df.describe()



