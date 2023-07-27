import csv

import numpy as np
import pandas as pd
from scipy import stats


# Collects metrics on the entire table and reports those metrics as specified in parameters passed
def show_metrics(df, all=False):    
    churn_variables = []
    churn_dtypes = []
    churn_count = []
    churn_unique = []
    churn_missing = []
    churn_pc_missing = []
    
    for item in df.columns:
        if df[item].isna().sum() > 0 or all:
            churn_variables.append(item)
            churn_dtypes.append(df[item].dtype)
            churn_count.append(len(df[item]))
            churn_unique.append(len(df[item].unique()))
            churn_missing.append(df[item].isna().sum())
            churn_pc_missing.append(round((df[item].isna().sum() / len(df[item])) * 100, 2))

    output = pd.DataFrame({
        'variable': churn_variables, 
        'dtype': churn_dtypes,
        'count': churn_count,
        'unique': churn_unique,
        'missing': churn_missing, 
        'pc_missing': churn_pc_missing
    })    
        
    return output

# Step 1 checks each of the individual columns
def checkAndCorrectColumnsPANDAS(df):
    #check the columns
    print(show_metrics(df, all=True))
    #print(df.dtypes)

    #correct for non string objects, incorrect data types, and incorrect lengths of strings
    strings = ["Customer_id", "Interaction", "City", "County", "County", "Area", "Timezone", "Job", "Education", "Employment", "Marital", "Gender"]
    for c in strings:
        df = df.loc[df[c].apply(lambda x: not isinstance(x, (float, int)))]
    print("Step 1: ", len(df))
    lengths = {'Customer_id': 7, 'Interaction': 37, 'State': 2, 'Zip': 5}
    for c in lengths.keys():
        df = df.loc[df[c].apply(lambda x: len(x) <= lengths[c])]
    print("Step 2: ", len(df))
    
    #correct for null values
    df=df.dropna(subset=["Bandwidth_GB_Year", "Phone", "TechSupport"])
    print("Step 3: ", len(df))
    df["Children"].fillna(0, inplace=True)
    df["Techie"].fillna('No', inplace=True)
    df["InternetService"].fillna('None', inplace=True)
    df["Income"].fillna(df["Income"].mean(), inplace=True)
    df["Tenure"].fillna(df["Tenure"].mean(), inplace=True)
    df["Age"].fillna(round(df["Age"].mean()), inplace=True)
    print("Step 4: ", len(df))

    #return if there are no longer any null issues
    check = show_metrics(df)
    if check.empty:
        return df
    else:
        print(check)

# Step 2 check for outliers across the demographic variables
def checkAndCorrectOutliers(df):
    # correct numerics acros a standard deviation
    num_demo = ["Income", "Population", "Children"]
    std_dev = 3
    for c in num_demo:
        df = df[(np.abs(stats.zscore(df[c])) < std_dev)]
    print("Step 5: ", len(df))

    # correct numerics within a range
    manual_demo = {"Lat": {'high': 180, 'low': -180}, "Lng": {'high': 180, 'low': -180}, "Age": {'high': 130, 'low': 18}}
    for c in manual_demo.keys():
        df = df.drop(df[df[c] > manual_demo[c]['high']].index)
        df = df.drop(df[df[c] < manual_demo[c]['low']].index)
    print("Step 6: ", len(df))

    # ensure enumered variables are maintained valid
    enum_demo = {"Area": ['Rural', 'Urban', 'Suburban'], "Employment": ['Part Time', 'Retired', 'Student', 'Full Time', 'Unemployed'], "Marital": ['Married', 'Widowed', 'Divorced', 'Never Married', 'Separated'], "Gender": ['Male', 'Female'], "Techie": ['Yes', 'No']}
    for c in enum_demo.keys():
        df = df[df[c].isin(enum_demo[c])]
    print("Step 7: ", len(df))

    # lone strings = [City, State, County, Zip, Timezone, Job, Education]

    return df


df = pd.read_csv('churn_raw_data.csv', dtype={'Zip': 'str'})
df = checkAndCorrectColumnsPANDAS(df) # Step 1 of cleaning
df = checkAndCorrectOutliers(df)
df.to_csv('churn_final_data.csv', index=False)