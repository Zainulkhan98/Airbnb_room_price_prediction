
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from Ingest_data import ingest_data
from zenml import step
from sklearn.impute import SimpleImputer
from new_input_features.Columns import *



@step(enable_cache=False)
def dropping_features(Data: pd.DataFrame) -> pd.DataFrame:
    try:
        Data = Data.drop(good_to_drop_col, axis=1)
        return Data
    except Exception as e:
        print(f"Error during dropping features: {e}")


@step(enable_cache=False)
def splitting_date_col(Data: pd.DataFrame) -> pd.DataFrame:
    try:
        Data['host_since'] = pd.to_datetime(Data['host_since'])
        Data['host_since_year'] = Data['host_since'].dt.year
        Data['host_since_month'] = Data['host_since'].dt.month
        Data['host_since_day'] = Data['host_since'].dt.day
        Data = Data.drop('host_since', axis=1)
        return Data
    except Exception as e:
        print(f"Error during seprating the datetime column: {e}")

# Not using this function on other columns because, the first these columns has way too many missing values


@step(enable_cache=False)
def imputation(Data: pd.DataFrame) -> pd.DataFrame:
    try:

        trf1 = ColumnTransformer(
            [('imputing_most_freq', SimpleImputer(strategy='most_frequent'), most_freq_col),
             ('imputing_mean', SimpleImputer(strategy='mean'), mean_col),
             ('imputing_median', SimpleImputer(strategy='median'), median_col)
             ],
            remainder='passthrough')
        trf1.fit_transform(Data)
        return Data
    except Exception as e:
        print(f"Error during imputation: {e}")


@step(enable_cache=False)
def categorical_encoding(Data: pd.DataFrame) -> pd.DataFrame:
    try:

        Data['amenities'] = Data['amenities'].str.replace('{', '')
        Data['amenities'] = Data['amenities'].str.replace('}', '')

        # Split the amenities
        sep_col = Data['amenities'].str.get_dummies(sep=',')

        # Join the amenities DataFrame with the original DataFrame
        Data = pd.concat([Data, sep_col], axis=1)

        Data = Data.drop(['amenities'], axis=1)
        Data = pd.DataFrame(Data)

        trf2 = ColumnTransformer([
            ('ohe', OneHotEncoder(sparse_output=False, handle_unknown='ignore'),
             categorical_col)], remainder='passthrough')
        trf2.fit_transform(Data)
        Data = Data.drop(categorical_col, axis=1)
        return Data
    except Exception as e:
        print(f"Error during categorical encoding: {e}")


@step(enable_cache=False)
def scaling(Data: pd.DataFrame) -> pd.DataFrame:
    try:

        trf3 = ColumnTransformer([
            ('standard_scaler', StandardScaler(),
             scaling_req_col),  # Specify column for scaling
        ], remainder='passthrough')
        trf3.fit_transform(Data)
        return Data  # Return scaled data directly
    except Exception as e:
        print(f"Error during scaling: {e}")
