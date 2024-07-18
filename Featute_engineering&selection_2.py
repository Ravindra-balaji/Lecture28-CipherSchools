# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HMqzyKKsqJYfYuoi0yx86oj9-Dmj_dfc
"""

import pandas as pd
from sklearn.feature_selection import VarianceThreshold

data = {
    'Feature1' : [1,1,1,1,1], # low variance
    'Feature2' : [2,3,4,5,6],
    'Feature3' : [3,4,5,6,7],
    'Feature4' : [1,1,1,1,1]
}
df = pd.DataFrame(data)

selector = VarianceThreshold(threshold=0.1)
df_variance_filtered = pd.DataFrame(selector.fit_transform(df), columns=df.columns[selector.get_support()])
print("After Variance Thresholding:\n", df_variance_filtered)

"""# 2. Correlation Matrix"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Feature1' : [1,2,3,4,5],
    'Feature2' : [2,4,6,8,10],
    'Feature3' : [2,4,6,8,10],
    'Feature4' : [5,6,7,8,9]
}
df = pd.DataFrame(data)

# Correlation matrix
corr_matrix = df.corr().abs()

# plot Correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.show()

# Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

# Find features with correlation greater than 0.9
to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]

# Drop features
df_corr_filtered = df.drop(to_drop, axis=1)
print("After Correlation Matrix:\n", df_corr_filtered)

"""# 3. Domain knowldege"""

import pandas as pd

data ={
    'Age' : [25,30,35,40,45],
    'Income' : [50000,60000,70000,80000,90000],
    'Height' : [5.5, 6.0, 5.8, 5.9, 6.1],
    'Weight' : [150,160,170,180,190]
}
df = pd.DataFrame(data)

# Based on triangle knowldge, we know Age and Salary are important
selected_features_domain = df[['Age','Income']]
print("After Domain Knowledge:\n", selected_features_domain)

