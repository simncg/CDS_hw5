# Function for computing roc_auc_score
from sklearn.metrics import roc_auc_score

def train_test_roc_auc(X_train, y_train, X_test, y_test):
    roc_auc_score_train = roc_auc_score(y_train, X_train["predictions"])
    roc_auc_score_test = roc_auc_score(y_test, X_test["predictions"])
    return roc_auc_score_train, roc_auc_score_test
