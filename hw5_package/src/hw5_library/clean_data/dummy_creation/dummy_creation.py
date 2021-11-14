# Function
import pandas as pd

def dummy_creation(df, column):
    return pd.get_dummies(df, columns = column, drop_first = True)

    