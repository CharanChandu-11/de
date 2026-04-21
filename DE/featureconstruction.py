import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

# One-Hot Encoding
data = pd.DataFrame({'City':['Delhi','Mumbai','Bangalore','Chennai','Delhi','Mumbai']})
encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(data[['City']])
print(encoded_data.toarray())

# Ordinal Encoding
data = pd.DataFrame({'Size':['Small','Medium','Large']})
encoder = OrdinalEncoder(categories=[['Small','Medium','Large']])
encoded_data = encoder.fit_transform(data[['Size']])
print(encoded_data)

# Binning
ages = pd.DataFrame({'Age':[25,35,45,55,65]})
ages['AgeGroup'] = pd.cut(ages['Age'], bins=[0,30,50,100], labels=['Young','Middle-aged','Senior'])
print(ages)