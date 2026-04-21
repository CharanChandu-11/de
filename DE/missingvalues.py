import pandas as pd
from sklearn.datasets import load_iris
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df.shape
df.head()
df.columns
df = df.rename(columns={'sepal length (cm)': 'newname'})
display(df)
display(df['newname'])
listcol = ['newname', 'sepal width (cm)']
display(df[listcol])
df1 = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=df.columns)
display(df1)
combdf = pd.concat([df, df1],axis=0)

df['total'] = df['newname'] + df['sepal width (cm)']
df.isnull().sum()
cols = df.select_dtypes(include=['int64','float64'])
for col in cols:
    print("mean of", col, ":", df[col].mean())
    print("median of", col, ":", df[col].median())
    print("mode of", col, ":", df[col].mode()[0])
    print("standard deviation of", col, ":", df[col].std())
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    print("lower bound of", col, ":", lower_bound)
    print("upper bound of", col, ":", upper_bound)
    print('iqr of', col, ":", iqr)