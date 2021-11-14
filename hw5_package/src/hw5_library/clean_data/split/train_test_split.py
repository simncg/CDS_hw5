# Function 
from sklearn.model_selection import train_test_split

def split_df(df, test_size=0.25):
    y = df.diabetes_mellitus
    X = df.drop("diabetes_mellitus", axis = 1)
    return train_test_split(X, y, test_size=test_size, random_state=42)