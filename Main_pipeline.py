from Ingest_data import ingest_data
from Feature_engineering import splitting_date_col,imputation,categorical_encoding,scaling,dropping_features
from Modeling import modeling,split_step,predict
from Evaluation import evaluate_model
from zenml import pipeline


@pipeline(enable_cache=False)
def Airbnb_pipeline(Data_path:str) -> float:
    """Full ML pipeline."""
    print("Ingesting data...")
    Data = ingest_data(Data_path=Data_path)
    print("Feature Engineering...")
    print('Dropping Features...')
    Processed_Data = dropping_features(Data)
    print('Splitting Date Column...')
    Processed_Data = splitting_date_col(Processed_Data)
    print('Imputing Data...')
    Processed_Data = imputation(Processed_Data)
    print('Categorical Encoding...')
    Processed_Data = categorical_encoding(Processed_Data)
    print('Scaling Data...')
    Processed_Data = scaling(Processed_Data)
    print('Splitting Data...')
    x_train, x_test, y_train, y_test = split_step(data=Processed_Data, test_size=0.2, target_column='log_price')
    print('Modeling Data...')
    Model = modeling(x_train=x_train,y_train=y_train)
    print('predicting Data...')
    prediction = predict(model=Model, x_test=x_test )
    print('Evaluating Data...')
    Evaluation = evaluate_model(y_test=y_test, prediction=prediction)
    return Evaluation


if __name__ == "__main__":
    Airbnb_pipeline('Data/Airbnb_Data.csv')