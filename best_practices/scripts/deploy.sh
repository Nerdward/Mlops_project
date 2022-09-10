export MODEL_BUCKET ="stg-mlflow-model"

export MLFLOW_TRACKING_URI="http://127.0.0.1:5000"
export MODEL_RUN_ID="6dd459b11b4e48dc862f4e1019d166f6"

mlflow artifacts download \
    --run-id ${MODEL_RUN_ID} \
    --artifact-path model \
    --dst-path .

aws s3 cp --recursive model/ s3://${MODEL_BUCKET}/model/
