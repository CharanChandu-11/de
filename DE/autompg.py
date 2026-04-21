import pandas as pd
import numpy as np
df=pd.read_csv("auto-mpg.csv")
df.replace('?', np.nan, inplace=True)
df['horsepower'] = pd.to_numeric(df['horsepower'])
df_clean = df.dropna()
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].mean())
q1 = df['mpg'].quantile(0.25)
q3 = df['mpg'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
df['mpg']=np.where(df['mpg'] < lower_bound, lower_bound, np.where(df['mpg'] > upper_bound, upper_bound, df['mpg']))
df 