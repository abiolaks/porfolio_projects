import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import plot_precision_recall_curve, plot_roc_curve
import pickle

from ML_Pipeline.processing import preprocess_data, load_data
from ML_Pipeline.modeling import train_models, evaluate_model, save_models

csv_file_path = "../data/raw/Marketing_Data.csv"

# Load data
df = load_data(csv_file_path)

# Preprocess data
df = preprocess_data(df)


# Split data into features and target variable
X = df[["Lead Owner", "What do you do currently ?", "Marketing Source", "Creation Source", "hour_of_day", "day_of_week"]]
y = df["Interest Level"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
models = train_models(X_train, y_train)

# Evaluate models
for model_name, model in models.items():
    evaluate_model(model_name, model, X_test, y_test)

# Save models
save_models(models)
