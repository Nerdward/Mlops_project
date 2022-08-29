from fastapi import FastAPI
import predict

app = FastAPI()
MODEL_LOCATION = './model'

@app.on_event("startup")
def load_artifacts():
    return predict.load_model(MODEL_LOCATION)

@app.post("/predict")
def _predict(request:dict):
    """Predict House price"""
    X = predict.feature_eng(request)
    model = load_artifacts()
    preds = predict.make_prediction(model, X)

    return {"house_price": preds.tolist()}
