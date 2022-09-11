# Problem Description
A Real Estate company have data on some properties i.e house. Data like the number of bedrooms, size of the front porch etc. They want a model that predicts the price of the house given the house features.
This is a regression task. The machine learning engineer (me) sourced data from [Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data). The dataset contains over 100 columns of different features of houses. He cleaned the data and trained an xgboost model on it.

## Cloud
Cloud Infrastructure:
![cloud](/images/cloud.png)

## Reproducibility
Run this command to setup the python environment and pre-commit
```bash
make setup
```

## Experiment tracking and model registry
[MLflow](https://www.mlflow.org/) was used for experiment traccking and model registering.

To start up the mlflow server, run
```bash
bash orchestration/server.sh
```
>keep this terminal open for the training pipeline

## Workflow Orchestration
[Prefect](https://www.prefect.io/) was used for workflow orchestration to get the data, preprocess it, run hyperparameter tuning with hyperopt and train the xbgoost model.

To start the training pipeline:
```bash
bash orchestration/train.sh
```

## Model deployment
Checkout from develop branch to ci-cd branch
```bash
git checkout -b ci-cd develop
```
Change the [infrastructure](./best_practices/infrastructure/vars) production variables to your choice.

Commit and push the changes to the ci-cd remote branch
Make a pull request and merge with develop branch

## Testing
```bash
terraform init -backend-config="key=mlops-zoomcamp-prod.tfstate" -reconfigure
terraform output rest_api_url
```
Change the url in the [deployment test file](./deployment/test.py) to the rest api url
