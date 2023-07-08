import inspect
from fastapi import FastAPI
import uvicorn
from bikeshare_model.predict import make_prediction
from bikeshare_model import __version__ as model_version

app = FastAPI()

@app.get("/predict/")
def predict():
    frame = inspect.currentframe()
    try:
        data = {'dteday': '2012-11-6', 'season': 'winter', 'hr': '6pm', 'holiday': 'No', 'weekday': 'Tue',
               'workingday': 'Yes', 'weathersit': 'Clear', 'temp': 16.0, 'atemp': 17.5, 'hum': 30, 'windspeed': 10.0, 'yr': 2012, 'mnth': 'january'}
        prediction = make_prediction(data)
        return {"Prediction": prediction}
    finally:
        del frame

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)