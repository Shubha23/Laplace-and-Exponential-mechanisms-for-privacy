""" Program to add noise generated from Exponential mechanism
    to Original Adult dataset.
"""   
# Import libraries 
import pandas as pd
import numpy as np

# Load the Adult dataset
dataset = pd.read_csv("adult.data.txt", names=["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status",
        "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
        "Hours per week", "Country", "Target"],sep=r'\s*,\s*',na_values="?")
dataset.tail()

datacount = dataset["Country"].value_counts()

# Generate random noise from exponential function.
Exponential_noise = np.random.exponential(1)     # Keep max limit = 1

print ("Exponentially generated noise:", Exponential_noise)

"""Add random noise drawn from Exponential function to Original data count"""
noisydata = datacount + Exponential_noise

#Plot histogram for Noisy data
noisydata.plot(kind="bar", color = 'r')
