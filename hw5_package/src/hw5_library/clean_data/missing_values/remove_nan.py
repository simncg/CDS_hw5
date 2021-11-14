# Function 
import pandas as pd
def remove_nan_age_gen_eth(X, y):
    # Drop rows with NaN from X
    X = X.dropna(subset=["age", "gender", "ethnicity"])
    # Drop the same rows from y     
    y = y[y.index.isin(X.index)]
    
    return X, y