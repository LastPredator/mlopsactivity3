import pandas as pd
from sklearn.datasets import load_iris
import os

# Load dataset
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['target'] = iris.target

# Ensure 'data' directory exists
os.makedirs("data", exist_ok=True)

# Save to CSV
data.to_csv("data/preprocessed.csv", index=False)
print("✅ Data preprocessed and saved to data/preprocessed.csv")
