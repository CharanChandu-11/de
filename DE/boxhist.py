from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

plt.figure()
df.boxplot()
plt.title("Boxplot of Iris Dataset")
plt.figure()

plt.figure()
plt.boxplot(df['sepal length (cm)'])
plt.title("Boxplot of Sepal Length")
plt.ylabel("Sepal Length (cm)")
plt.show()

plt.figure()
plt.hist(df["petal length (cm)"])
plt.title("Histogram of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.scatter(df["sepal length (cm)"], df["sepal width (cm)"])
plt.title("Scatter Plot of Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.show()
