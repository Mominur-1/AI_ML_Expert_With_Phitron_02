# https://www.codechef.com/learn/course/pandas/LPDP06/problems/LPDPR28

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [5, np.nan, np.nan, None, 10],
    'C': ['a', 'b', 'c', None, 'e']
})
                   
print(df)

# Drop rows where column A has missing values
df_1 = df.dropna(subset=['A'])
print(df_1)

# Drop rows with less than 2 non-null values
df_2 = df.dropna(thresh=2)
print(df_2)

# Drop rows where both Column A and Column B has missing values
df.dropna(subset=['A','B'], how='all', inplace=True)
print(df)