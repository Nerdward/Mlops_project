import mlflow
import pandas as pd

# import xgboost as xgb


def feature_eng(data):
    df = pd.DataFrame(data, index=[0])
    columns = [
        "MSSubClass",
        "LotFrontage",
        "LotArea",
        "OverallQual",
        "OverallCond",
        "YearBuilt",
        "YearRemodAdd",
        "MasVnrArea",
        "BsmtFinSF1",
        "BsmtFinSF2",
        "BsmtUnfSF",
        "TotalBsmtSF",
        "1stFlrSF",
        "2ndFlrSF",
        "LowQualFinSF",
        "GrLivArea",
        "BsmtFullBath",
        "BsmtHalfBath",
        "FullBath",
        "HalfBath",
        "BedroomAbvGr",
        "KitchenAbvGr",
        "TotRmsAbvGrd",
        "Fireplaces",
        "GarageYrBlt",
        "GarageCars",
        "GarageArea",
        "WoodDeckSF",
        "OpenPorchSF",
        "EnclosedPorch",
        "3SsnPorch",
        "ScreenPorch",
        "PoolArea",
        "MiscVal",
        "MoSold",
        "YrSold",
    ]
    X = df[columns]

    return X


def load_model(model_location):
    model = mlflow.pyfunc.load_model(model_location)

    return model


def make_prediction(model, input_data):
    X = feature_eng(input_data)
    # X = xgb.DMatrix(X)
    preds = model.predict(X)

    return preds
