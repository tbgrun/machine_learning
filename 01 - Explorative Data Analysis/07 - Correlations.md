# Correlations
## 1. Pair Plot
### 1.1 Import Libraries
    import seaborn as sns
    import matplotlib.pyplot as plt
### 1.2 Run Pair Plot
    sns.pairplot(df, hue='grouping_column')
    plt.show()
## 2. Heatmap
### 2.1 Import Libraries
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
### 2.2a Run Heatmap as Single Plot
    correlation_matrix = df.corr() # generates correlation matrix. Use .corr().abs() if correlation should be positive
    plt.figure(figsize=(15, 10))  # set figure size
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True, linewidths=0) # generates heatmap
    plt.show()
### 2.2b Run Heatmap as Subplot
    correlation_matrix = df.corr() # generates correlation matrix. Use .corr().abs() if correlation should be positive
    fig, ax = plt.subplots(figsize=(15, 10))  # set axes and figure size
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True, linewidths=0, ax=ax) # generates heatmap
    plt.show()

[klick here to get to "Handling Multi-Colinearity"](https://github.com/tbgrun/machine_learning/blob/main/02%20-%20Data%20Wrangling/07%20-%20Handling%20Multi-Colinearity.md)
