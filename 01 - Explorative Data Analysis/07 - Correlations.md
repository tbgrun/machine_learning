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
### 2.2 Run Heatmap
    correlation_matrix = df.corr() # generates correlation matrix
    plt.figure(figsize=(10, 8))  # set figure size
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True, linewidths=0.5) # generates heatmap
    plt.show()
