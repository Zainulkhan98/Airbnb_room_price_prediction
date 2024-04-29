

# Airbnb Price Prediction

This project is a machine learning pipeline that predicts Airbnb prices based on various features. The project is implemented in Python and uses the ZenML library to manage the machine learning pipeline.

## Project Structure

The project is divided into several Python scripts, each responsible for a specific part of the machine learning pipeline:

- `Ingest_data.py`: This script is responsible for data ingestion. It reads a CSV file from a given path and returns a pandas DataFrame. The DataFrame is limited to the first 10,000 rows of the CSV file.

- `Feature_engineering.py`: This script is responsible for feature engineering. It includes functions for splitting date columns, imputing missing data, encoding categorical variables, scaling numerical variables, and dropping unnecessary features.

- `Modeling.py`: This script is responsible for splitting the data into training and testing sets, training the model, and making predictions. It uses the XGBoost regressor for model training.

- `Evaluation.py`: This script is responsible for evaluating the model. It calculates the R2 score, mean squared error, and mean absolute error of the model's predictions.

- `Main_pipeline.py`: This script combines all the steps into a full machine learning pipeline. It ingests the data, performs feature engineering, trains the model, makes predictions, and evaluates the model.

## Usage

To run the project, you need to first initialize ZenML:

```bash
zenml init
```

Then, start the ZenML service:

```bash
zenml up --blocking
```

Stop the service by pressing `Ctrl+C`. After that, run the main pipeline:

```python
if __name__ == "__main__":
    Airbnb_pipeline('Data/Airbnb_Data.csv')
```

Once the pipeline has successfully run, start the ZenML service again:

```bash
zenml up
```

You can then access the ZenML dashboard by clicking on the link provided.

## Dependencies

This project requires the following Python packages:

- pandas
- sklearn
- zenml
- xgboost
- joblib

## Note

This project uses the ZenML library to manage the machine learning pipeline. ZenML pipelines are designed to be reproducible and version-controlled. The `enable_cache=False` decorator on each step ensures that the step is run every time the pipeline is executed, rather than reusing results from a previous run.
