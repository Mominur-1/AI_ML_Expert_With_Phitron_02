# https://www.codechef.com/learn/course/pandas/LPDP06/problems/LPDPR29

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        'A' : [1, 2, np.nan, 4, 5],
        'B' : [5, np.nan, np.nan, np.nan, 10],
        'C' : ['a', 'b', 'c', None, 'e']
    }
)

print(df)

# Replace null values based on given conditions
df_filled = df.fillna({'A': 0, 'B': 99, 'C': 'Unknown'})
print(df_filled)

# Forward fill column B
df_B = df.copy()
df_B.loc[df_B['B'].isna(), 'B'] = df['B'].ffill()
print(df_B)


# Fills missing values in numeric columns with the mean of the column and in string columns with 'Unknown'.
df = df.apply(
    lambda col: col.fillna(col.mean()) 
    if pd.api.types.is_numeric_dtype(col) 
    else col.fillna('Unknown'),
    axis= 0
)
print(df)