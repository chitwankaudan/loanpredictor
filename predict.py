import os
import settings
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

def cross_validate(train):
    """
    Transforms dataset into design matrix X and target variable Y 
    and fits a logistic regression model. Uses crossvalidation with
    cv folds specified in settings.py to create and return predictions. 
    """
    clf = LogisticRegression(random_state=1, class_weight="balanced")

    predictors = train.columns.tolist()
    predictors = [p for p in predictors if p not in settings.NON_PREDICTORS]

    predictions = cross_val_predict(clf, train[predictors], train[settings.TARGET], cv=settings.CV_FOLDS)
    return predictions

def compute_error(target, predictions):
    """ 
    Gives basic accuracy of model by comparing predicitons
    and target variables.
    """
    return metrics.accuracy_score(target, predictions)

def compute_false_negatives(target, predictions):
    """
    Gives # of false negatives rate (our model predicted 0 but
    actual value is 1)
    """
    df = pd.DataFrame({"target": target, "predictions": predictions})
    return df[(df["target"] == 1) & (df["predictions"] == 0)].shape[0] / (df[(df["target"] == 1)].shape[0] + 1)

def compute_false_positives(target, predictions):
    """
    Gives # of false positives rate (our model predicted 1 but
    actual value is 0)
    """
    df = pd.DataFrame({"target": target, "predictions": predictions})
    return df[(df["target"] == 0) & (df["predictions"] == 1)].shape[0] / (df[(df["target"] == 0)].shape[0] + 1)

if __name__ == "__main__":
    data = pd.read_pickle("processed/cleaned.pkl")
    predictions = cross_validate(data)
    error = compute_error(data[settings.TARGET], predictions)
    fn = compute_false_negatives(data[settings.TARGET], predictions)
    fp = compute_false_positives(data[settings.TARGET], predictions)
    print("Accuracy Score: {}".format(error))
    print("False Negatives: {}".format(fn))
    print("False Positives: {}".format(fp))