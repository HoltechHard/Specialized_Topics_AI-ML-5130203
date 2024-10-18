import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import lightgbm as lgbm

# KNN Class
class KNNModel:
    def __init__(self):
        # Hyperparameters definition
        self.params = {
            "n_neighbors": [3, 5, 7, 9],
            "weights": ["uniform", "distance"],
            "algorithm": ['auto', 'ball_tree', 'kd_tree', 'brute'],
            "leaf_size": [10, 20, 30],
            "metric": ["euclidean", "manhattan"]
        }

    def train(self, x_train, y_train):
        # Define the model
        model = KNeighborsClassifier()
        
        # Hyperparameter optimization
        grid_search = GridSearchCV(estimator=model,
                                   param_grid=self.params,
                                   scoring="accuracy",
                                   cv=5,
                                   n_jobs=-1)
        grid_search.fit(x_train, y_train)
        
        # Get best model
        best_model = grid_search.best_estimator_
        print("Best KNN Parameters:", grid_search.best_params_)
        
        return best_model


# SVM Class
class SVMModel:
    def __init__(self):
        # Hyperparameters definition
        self.params = {
            "C": [0.1, 1, 10],
            "kernel": ["linear", "rbf", "poly"],
            "gamma": ["scale", "auto"],
            "degree": [2, 3, 4],
            "class_weight": ["balanced"]
        }

    def train(self, x_train, y_train):
        # Define the model
        model = SVC()
        
        # Hyperparameter optimization 
        grid_search = GridSearchCV(estimator=model,
                                   param_grid=self.params,
                                   scoring="accuracy",
                                   cv=5,
                                   n_jobs=-1)
        grid_search.fit(x_train, y_train)
        
        # Get best model
        best_model = grid_search.best_estimator_
        print("Best SVM Parameters:", grid_search.best_params_)
        
        return best_model


# Random Forest Class
class RandomForestModel:
    def __init__(self):
        # Hyperparameters definition 
        self.params = {
            "n_estimators": [50, 100, 200],
            "max_depth": [10, 20, 30],
            "min_samples_split": [2, 5, 10],
            "min_samples_leaf": [1, 2, 4],
            "max_features": [1, 2, 3, 'sqrt', 'log2']
        }

    def train(self, x_train, y_train):
        # Define the model
        model = RandomForestClassifier()
        # Hyperparameter optimization 
        grid_search = GridSearchCV(estimator=model,
                                   param_grid=self.params,
                                   scoring="accuracy",
                                   cv=5,
                                   n_jobs=-1)
        grid_search.fit(x_train, y_train)
        # Get best model 
        best_model = grid_search.best_estimator_
        print("Best Random Forest Parameters:", grid_search.best_params_)
        
        return best_model


# XGBoost Class
class XGBoostModel:
    def __init__(self):
        # Hyperparameters definition
        self.params = {
            "max_depth": [8, 16, 32],
            "learning_rate": [0.01, 0.05, 0.1],
            "subsample": [0.7, 0.8],
            "colsample_bytree": [0.8, 0.9],
            "n_estimators": [50, 100, 200],
            "objective": ["binary:logistic"]
        }

    def train(self, x_train, y_train):
        # Define the model
        model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
        
        # Hyperparameter optimization 
        grid_search = GridSearchCV(estimator=model,
                                   param_grid=self.params,
                                   scoring="accuracy",
                                   cv=5,
                                   n_jobs=-1)
        grid_search.fit(x_train, y_train)
        
        # Get best model 
        best_model = grid_search.best_estimator_
        print("Best XGBoost Parameters:", grid_search.best_params_)
        
        return best_model


# LightGBM Class
class LightGBMModel:
    def __init__(self):
        # Hyperparameters definition 
        self.params = {
            "num_leaves": [31, 50, 100],
            "max_depth": [10, 20, 30],
            "learning_rate": [0.01, 0.05, 0.1],
            "n_estimators": [50, 100, 200],
            "boosting_type": ["gbdt", "dart"]
        }

    def train(self, x_train, y_train):
        # Define the model
        model = lgbm.LGBMClassifier()
        # Hyperparameter optimization 
        grid_search = GridSearchCV(estimator=model,
                                   param_grid=self.params,
                                   scoring="accuracy",
                                   cv=5,
                                   n_jobs=-1)
        grid_search.fit(x_train, y_train)
        
        # Get best model 
        best_model = grid_search.best_estimator_
        print("Best LightGBM Parameters:", grid_search.best_params_)
        
        return best_model
