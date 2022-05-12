# lab 13 

import pandas as pd
import numpy as np

df1 = pd.read_csv('flat_file_df1.csv')
df2 = pd.read_csv('flat_file_df2.csv')
# had to drop gender because df2 is missing the whole column
df1.drop( columns='gender', inplace = True)

# now we must join them

df = pd.merge(df1, df2, on = 'age', how = 'left')

# hair_color
df['hair_color_x'].value_counts()

df['hair_color_x'].fillna(value = 'brown', inplace = True)

# eye_color
df['eye_color_x'].value_counts()

df['eye_color_x'].fillna(value = 'brown', inplace = True)

# height
print(df.height_x)
df['height_x'].fillna(df.height_x.mean, inplace = True)

# is the missing data gone?
df.isnull().sum()
# yes

# part two
df.mean()
df['height_x'].sum()
df.median()
df.mode()
df.describe()

df['hair_color_x'].mode()
df['eye_color_x'].mode()