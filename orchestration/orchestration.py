
# We will start with the data pre-loaded into **train_X**, **test_X**, **train_y**, **test_y**.
from asyncio import wait_for
import pandas as pd
from sklearn.model_selection import train_test_split
import mlflow
import xgboost as xgb

from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from hyperopt.pyll import scope
from sklearn.metrics import mean_squared_error

from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner

# from sklearn.preprocessing import Imputer
@task
def prepare_data(filename):
    data = pd.read_csv(filename)
    data.dropna(axis=0, subset=['SalePrice'], inplace=True)

    return data

@task
def feature_eng(data):
    y = data.SalePrice
    X = data.drop(['Id','SalePrice'], axis=1).select_dtypes(exclude=['object'])
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.25)

    return train_X, test_X, train_y, test_y

# my_imputer = Imputer()
# train_X = my_imputer.fit_transform(train_X)
# test_X = my_imputer.transform(test_X)

# We build and fit a model just as we would in scikit-learn.

@task
def train_model_search(train, valid, test_y):
    def objective(params):
        with mlflow.start_run():
            # mlflow.set_tag("model", "xgboost")
            # mlflow.log_params(params)
            booster = xgb.train(
                params=params,
                dtrain=train,
                num_boost_round=1000,
                evals=[(valid, 'validation')],
                early_stopping_rounds=50
            )
            y_pred = booster.predict(valid)
            rmse = mean_squared_error(test_y, y_pred, squared=False)
            mlflow.log_metric("rmse", rmse)

        return {'loss': rmse, 'status': STATUS_OK}


    search_space = {
        'max_depth': scope.int(hp.quniform('max_depth', 4, 100, 1)),
        'learning_rate': hp.loguniform('learning_rate', -3, 0),
        'reg_alpha': hp.loguniform('reg_alpha', -5, -1),
        'reg_lambda': hp.loguniform('reg_lambda', -6, -1),
        'min_child_weight': hp.loguniform('min_child_weight', -1, 3),
        'objective': 'reg:squarederror',
        'seed': 42
    }

    best_result = fmin(
        fn=objective,
        space=search_space,
        algo=tpe.suggest,
        max_evals=50,
        trials=Trials()
    )
    return best_result
    
# ### Train best model

@task
def train_best_model(train, valid):
    with mlflow.start_run():
        
        # train = xgb.DMatrix(train_X, label=train_y)
        # valid = xgb.DMatrix(test_X, label=test_y) 

        best_params = {'learning_rate': '0.42649323727247074', 
                        'max_depth': '4',
                        'min_child_weight': '2.823388102868533',
                        'objective': 'reg:squarederror',
                        'reg_alpha': '0.08394020560827088',
                        'reg_lambda': '0.1989734719817237',
                        'seed': '42'
                        }

        # mlflow.log_params(best_params)

        booster = xgb.train(
            params=best_params,
            dtrain=train,
            num_boost_round=1000,
            evals=[(valid, 'validation')],
            early_stopping_rounds=50
        )

        y_pred = booster.predict(valid)

        # mlflow.xgboost.log_model(booster, artifact_path="models_mlflow")

@flow(task_runner=SequentialTaskRunner())
def main(train_path='../exp_tracking/train.csv', test_path='../exp_tracking/test.csv'):
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("Xgboost Mlops")
    mlflow.xgboost.autolog()

    df_train = prepare_data(train_path)

    train_X, test_X, train_y, test_y = feature_eng(df_train)

    train = xgb.DMatrix(train_X, label=train_y)
    valid = xgb.DMatrix(test_X, label=test_y) 

    best = train_model_search(train, valid, test_y)
    train_best_model(train, valid, wait_for=best)

from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import IntervalSchedule
from datetime import timedelta

if __name__ == "__main__":
    main()
# Deployment(
#     flow=main,
#     name="model_training",
#     # schedule=IntervalSchedule(interval=timedelta(weeks=1)),
#     flow_runner=SubprocessFlowRunner(),
#     tags=["ml"],
# )
