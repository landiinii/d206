import csv

import numpy as np
import pandas as pd
from scipy import stats
import math


# Collects metrics on the entire table and reports those metrics as specified in parameters passed
def show_metrics(df, all=False):    
    churn_variables = []
    churn_dtypes = []
    churn_count = []
    churn_unique = []
    churn_missing = []
    churn_pc_missing = []
    churn_std_dev = []
    max_num = []
    min_num = []
    max_len = []
    min_len = []
    
    for item in df.columns:
        if df[item].isna().sum() > 0 or all:
            churn_variables.append(item)
            churn_dtypes.append(df[item].dtype)
            churn_count.append(len(df[item]))
            churn_unique.append(len(df[item].unique()))
            churn_missing.append(df[item].isna().sum())
            churn_pc_missing.append(round((df[item].isna().sum() / len(df[item])) * 100, 2))
            if df[item].dtype == 'float64' or  df[item].dtype == 'int64':
                churn_std_dev.append(len(df[(np.abs(stats.zscore(df[item])) > 3)]))
                max_num.append(df[item].max())
                min_num.append(df[item].min())
                max_len.append(0)
                min_len.append(0)
            elif df[item].dtype == 'str':
                churn_std_dev.append(0)
                max_num.append(0)
                min_num.append(0)
                max_len.append(df[item].str.len().max())
                min_len.append(df[item].str.len().min())
            else:
                churn_std_dev.append(0)
                max_num.append(0)
                min_num.append(0)
                max_len.append(0)
                min_len.append(0)


    output = pd.DataFrame({
        'variable': churn_variables, 
        'dtype': churn_dtypes,
        'count': churn_count,
        'unique': churn_unique,
        'missing': churn_missing, 
        'pc_missing': churn_pc_missing,
        'standard_dev': churn_std_dev,
        'max_num': max_num,
        'min_num': min_num,
        'max_len': max_len,
        'min_len': min_len
    })    
        
    return output


df = pd.read_csv('churn_raw_data.csv')
df = show_metrics(df, all=True)
print(df)
df.to_csv('assessment.csv', index=False)