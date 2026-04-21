import numpy as np

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

mean_value = np.mean(data)
median_value = np.median(data)
std_dev = np.std(data)
variance = np.var(data)

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
correlation_matrix = np.corrcoef(x, y)

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("Correlation Coefficients:")
print(correlation_matrix)
