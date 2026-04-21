import numpy as np
data = np.array([1, 2, 3, 4, 5])
mean = np.mean(data)
median = np.median(data)
mode = np.bincount(data).argmax()
max_value = np.max(data)
min_value = np.min(data)
range_value = max_value - min_value
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)
print("Range:", range_value)

variance = np.var(data)
std_dev = np.std(data)
print("Variance:", variance)
print("Standard Deviation:", std_dev)

variance_sample = np.var(data, ddof=1)
std_dev_sample = np.std(data, ddof=1)
print("Sample Variance:", variance_sample)
print("Sample Standard Deviation:", std_dev_sample)

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)