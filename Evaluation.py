from typing import Tuple

import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from zenml import step
from sklearn.metrics import confusion_matrix


@step(enable_cache=False)
def evaluate_model(y_test: pd.Series, prediction:pd.Series) -> Tuple[float, float, float]:
    try:
        r2 = r2_score(y_test, prediction)
        mse = mean_squared_error(y_test, prediction)
        mae = mean_absolute_error(y_test, prediction)
        return r2, mse, mae
    except Exception as e:
        print(f"Error during evaluation: {e}")
