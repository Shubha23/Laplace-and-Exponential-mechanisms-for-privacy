# Find sensitivity - New dataset
import pandas as pd

#Load both datasets - Adult (actual) dataset and modified dataset                                 
Actual_dataset = pd.read_csv("adult.data.txt", names=["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status",
        "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
        "Hours per week", "Country", "Target"],engine = 'python',sep=r'\s*,\s*',na_values="?")        
Actual_dataset.tail()    

Neighbouring_dataset = pd.read_csv("adultnew.data.txt", names=["Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status",
        "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
        "Hours per week", "Country", "Target"],engine='python',sep=r'\s*,\s*',na_values="?")     
Neighbouring_dataset.tail()

#Count of Adult dataset 
Actual_attribute = Actual_dataset["Country"].value_counts()

#Count of modified dataset
Modified__attribute = Neighbouring_dataset["Country"].value_counts() 

#Sensitivity between above datasets
Sensitivity = max(abs(Modified__attribute - Actual_attribute))
print ("Sensitivity of neighbouring databases is:", Sensitivity)
 

