from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
data = iris.data
feature_names = iris.feature_names

sample_dicts = [
    {feature_names[j]: data[i, j] for j in range(data.shape[1])}
    for i in range(data.shape[0])
]

means = np.mean(data, axis=0)
stds = np.std(data, axis=0)

# Step 3: Perform Z-score standardization on each feature
standardized_data = (data - means) / stds

standardized_sample_dicts = [
    {
        feature_names[j]: standardized_data[i, j]
        for j in range(standardized_data.shape[1])
    }
    for i in range(standardized_data.shape[0])
]

print("Original Sample Dictionaries:")
for sample in sample_dicts[:5]:
    print(sample)

print("\nStandardized Sample Dictionaries:")
for sample in standardized_sample_dicts[:5]:
    print(sample)
