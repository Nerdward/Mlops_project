#!/usr/bin/env bash

cd "$(dirname "$0")"

mlflow server --backend-store-uri sqlite:///backend.db --default-artifact-root ./artifact
