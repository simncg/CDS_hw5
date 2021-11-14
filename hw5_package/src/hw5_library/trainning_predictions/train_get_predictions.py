# Function
from sklearn.linear_model import LogisticRegression

def train_predictions_model(X_train, y_train, X_test):
    logit = LogisticRegression()
    cols = ["age", "height", "weight", "aids", "cirrhosis", "hepatic_failure", 
            "immunosuppression", "leukemia", "lymphoma", "solid_tumor_with_metastasis"]
    X_train = X_train[cols]
    X_test = X_test[cols]
    logit.fit(X_train, y_train)
    probas_train = logit.predict_proba(X_train)
    X_train["predictions"] = probas_train[:,1]
    probas_test = logit.predict_proba(X_test) 
    X_test["predictions"] = probas_test[:,1]
    
    return X_train, X_test