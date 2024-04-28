# # import os
# # from typing import Type
# #
# # import joblib
# # from zenml.enums import ArtifactType
# # from xgboost import XGBRegressor
# # from zenml.materializers.base_materializer import BaseMaterializer
# #
# #
# # class SKLearnModelMaterializer(BaseMaterializer):
# #     ASSOCIATED_TYPES = (XGBRegressor)
# #     ASSOCIATED_ARTIFACT_TYPE = ArtifactType.MODEL
# #
# #     def load(self, data_type: Type[XGBRegressor]) -> XGBRegressor:
# #         """Read from artifact store."""
# #         model_path = os.path.join(self.uri, 'model.joblib')
# #         return joblib.load(model_path)
# #
# #     def save(self, model:
# #              XGBRegressor) -> None:
# #         """Write to artifact store."""
# #         model_path = os.path.join(self.uri, 'model.joblib')
# #         joblib.dump(model, model_path)
#
#
#
#
#
#
#
# from sklearn.tree import DecisionTreeRegressor
# from zenml.materializers.base_materializer import BaseMaterializer
# import pickle
#
# class DecisionTreeRegressorMaterializer(BaseMaterializer):
#     """
#     Custom materializer for DecisionTreeRegressor models.
#     """
#
#
#
#     def load(self, path: str) -> DecisionTreeRegressor:
#         """
#         Loads a DecisionTreeRegressor model from a file.
#
#         Args:
#             path: The path to load the model from.
#
#         Returns:
#             The loaded DecisionTreeRegressor model.
#         """
#         with open(path, "rb") as f:
#             return pickle.load(f)
#
#
#     def save(self, artifact: DecisionTreeRegressor, path: str) -> None:
#         """
#         Saves the DecisionTreeRegressor model to a file.
#
#         Args:
#             artifact: The DecisionTreeRegressor model to save.
#             path: The path to save the model to.
#         """
#         with open(path, "wb") as f:
#             pickle.dump(artifact, f)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # ... your pipeline steps
#
# @step
# def train_model(x_train: pd.DataFrame, y_train: pd.Series) -> DecisionTreeRegressor:
#     # Train your DecisionTreeRegressor model
#     model = DecisionTreeRegressor()
#     model.fit(x_train, y_train)
#     return model
#
# @step(materializer="decision_tree_materializer")  # Reference the custom materializer
# def predict(model: DecisionTreeRegressor, x_test: pd.DataFrame) -> pd.Series:
#     # Make predictions using the loaded model
#     predictions = model.predict(x_test)
#     return predictions
#
# # ... other pipeline steps
#
# pipeline = Pipeline(
#     steps=[
#         train_model,
#         predict,
#     ],
#     materializers={
#         "decision_tree_materializer": DecisionTreeRegressorMaterializer,
#     },
# )
