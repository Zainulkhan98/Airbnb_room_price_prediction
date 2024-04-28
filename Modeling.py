from typing import Tuple

import joblib
import xgboost
from sklearn.base import RegressorMixin
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import linear_model
import pandas as pd
from zenml import step
from sklearn import tree


@step(enable_cache=False)
def split_step(data: pd.DataFrame, test_size:float, target_column:str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    try:

        X = data.drop(target_column, axis=1)
        Y = data[target_column]
        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=42)
        y_train = pd.Series(y_train)
        y_test = pd.Series(y_test)
        return x_train, x_test, y_train, y_test
    except Exception as e:
        print(f"Error during splitting: {e}")


@step(enable_cache=False)
def modeling(x_train:pd.DataFrame,y_train:pd.Series) -> XGBRegressor:
    model = XGBRegressor().fit(x_train,y_train)
    joblib.dump(model, 'joblib_loaded/model')
    return model


# Making predictions
@step(enable_cache=False)
def predict(model: XGBRegressor, x_test: pd.DataFrame) -> pd.Series:
    pred = model.predict(x_test)
    predictions = pd.Series(pred)
    return predictions
