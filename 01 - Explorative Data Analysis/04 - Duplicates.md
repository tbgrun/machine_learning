# Duplicates
### 1. Identify duplicated rows
#### 1.1 Import Libraries
    import pandas as pd
#### 1.2 Check for duplicated rows
Returns if duplicates are present or not.
    df.duplicated().any()
Returns "True" if duplicates are present and "False" if none are present.
#### 1.3 Show duplicated rows
Returns which rows are duplicated (if any) and shows their content.
    print(df[df.duplicated(keep=False)])
### 2. Remove duplicated rows
#### 2.1 Import Libraries
    import pandas as pd
#### 2.2 Remove duplicated
    df.drop_duplicates()
