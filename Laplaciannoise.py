# Implementing Laplace mechanism on Adult dataset by adding Laplacian random noise
import pandas as pd
import numpy as np

# Load Adult dataset 
dataset = pd.read_csv("adult.data.txt",
    names=["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status",
        "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
        "Hours per week", "Country", "Target"],sep=r'\s*,\s*',na_values="?")
dataset.tail()

# Set parameters for Laplace function implementation
location = 1.0
scale = 1.0

#Find actual data count
datacount = dataset["Country"].value_counts()

# Gets random laplacian noise for all values
Laplacian_noise = np.random.laplace(location,scale, len(datacount))
print(Laplacian_noise)

# Add random noise generated from Laplace function to actual count
noisydata = datacount + Laplacian_noise

# Generate noisy histogram
noisydata.plot(kind="bar",color = 'g')
