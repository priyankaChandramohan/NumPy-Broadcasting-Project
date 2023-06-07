
import numpy as np
import scipy.stats

# Task 1: Scalar Broadcasting
vector = np.arange(1, 11) + 1

# Task 2: Matrix Broadcasting
matrix = vector[:, np.newaxis] + vector

# Task 3: Standardizing Data
data = np.exp(np.random.randn(50, 5))
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

# Task 4: Standardize the Data
normalized = (data - mean) / std
normalized_mean = np.mean(normalized, axis=0)
normalized_std = np.std(normalized, axis=0)

# Task 5: Print Mean and Standard Deviation of Normalized Data
print("Mean of Normalized Data:")
print(normalized_mean)
print("\nStandard Deviation of Normalized Data:")
print(normalized_std)

# Task: Chi-squared Hypothesis Testing
observed = np.array([[141, 68, 4],
                     [179, 159, 7],
                     [220, 216, 4],
                     [86, 101, 4]])

chi2, p, dof, expected = scipy.stats.chi2_contingency(observed)

if p < 0.05:
    print("There is evidence of a relationship between age group and movie genre inclination.")
else:
    print("There is no evidence of a relationship between age group and movie genre inclination.")
