""" Program to show implementation of Utility/Score function
    to release the name of Most native country """
    
# Import Libraries
import pandas as pd
import numpy as np

#Load the Adult dataset
dataset = pd.read_csv("adult.data.txt", names=["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status",
        "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
        "Hours per week", "Country", "Target"],sep=r'\s*,\s*',na_values="?")
dataset.tail()

"""Utility/Score function implementation"""
def Utility_function() :
   # Finds country with most number of entries 
   Utility = ((dataset["Country"].value_counts() / dataset.shape[0])).head(1)
   if dataset.dtypes["Country"] == np.object:
     dataset["Country"].value_counts().plot(kind="bar", color = 'g')
   return Utility  

#Call Utility function()
utility = Utility_function()  
print ("Most native country is:", utility)  
