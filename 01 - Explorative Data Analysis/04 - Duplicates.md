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

[klick here to get to "Handle Duplicates"](https://github.com/tbgrun/machine_learning/blob/main/01%20-%20Explorative%20Data%20Analysis/04.01%20-%20Handle%20Duplicates.md)
