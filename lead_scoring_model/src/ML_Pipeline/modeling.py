#!/usr/bin/env python

import pandas as pd
from lightgbm import LGBMClassifier
from pandas import factorize
import pickle
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, plot_roc_curve, plot_precision_recall_curve
import pandas as pd
from lightgbm import LGBMClassifier
from pandas import factorize
import pickle
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier




def train_models(X, y):
    lr = LogisticRegression()
    gnb = GaussianNB()
    svm = LinearSVC()
    rf = RandomForestClassifier(n_estimators=300)
    xgb = XGBClassifier(n_estimators=300, objective='binary:logistic', tree_method='hist', eta=0.1, max_depth=3)
    lgb = LGBMClassifier(n_estimators=300)
    nn = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(10, 10), random_state=123)

    print("Training Logistic Regression Model")
    lr.fit(X, y)

    print("Training Gaussian Naive Bayes Model")
    gnb.fit(X, y)

    print("Training Linear SVM Model")
    svm.fit(X, y)

    print("Training Random Forest Model")
    rf.fit(X, y)

    print("Training XGBoost Model")
    xgb.fit(X, y)

    print("Training Light GBM Model")
    lgb.fit(X, y)

    print("Training Neural Network Model")
    nn.fit(X, y)

    models = {'Logistic_Reg': lr, 'Naive_Bayes': gnb, 'SVM': svm, 'Random_Forest': rf,
              'XGB': xgb, 'LGB': lgb, 'Neural_Nets': nn}

    return models

def evaluate_model(model_name, model, X_test, y_test):
    pred = model.predict(X_test)
    accuracy = accuracy_score(pred, y_test)
    print("Accuracy of %s: " % model_name, accuracy)

def save_models(models):
    for model_name, model in models.items():
        model_path = "../models/" + model_name.lower().replace(" ", "_") + ".model"
        pickle.dump(model, open(model_path, 'wb'))