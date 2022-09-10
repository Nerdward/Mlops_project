mlflow server --backend-store-uri sqlite:///backend.db --default-artifact-root ./artifacts

export MLFLOW_TRACKING_URI="http://127.0.0.1:5000"
export MODEL_RUN_ID="6dd459b11b4e48dc862f4e1019d166f6"

mlflow artifacts download \
    --run-id ${MODEL_RUN_ID} \
    --artifact-path model \
    --dst-path .

```bash
aws s3 cp --recursive model/ s3://nerdward-bucket/model/
```

```bash
docker build -t house-price-prediction:v1 .

docker run -it --rm \
    -p 8080:8080 \
    -v /home/azureuser/.aws:/root/.aws \
    house-price-prediction:v1
```

aws ecr create-repository --repository-name duration-model

aws ecr get-login-password | docker login --username AWS --password-stdin 435520236541.dkr.ecr.us-east-1.amazonaws.com/house-prediction


REMOTE_URI="public.ecr.aws/r2u6t4r3/house-prediction"
REMOTE_TAG="v1"
REMOTE_IMAGE=${REMOTE_URI}:${REMOTE_TAG}

LOCAL_IMAGE="house-price-prediction:v1"
docker tag ${LOCAL_IMAGE} ${REMOTE_IMAGE}
docker push ${REMOTE_IMAGE}

aws ecr-public create-repository \
     --repository-name house-prediction \
     --region us-east-1

isort .
black .
pylint --recursive .
pytest tests/
