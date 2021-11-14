# Function 
import pandas as pd
def fill_nan_height_weight(X):
    for var in ["height", "weight"]:
        X[var] = X[var].fillna(X[var].mean())
    return X