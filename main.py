#from fastapi import FastAPI
#app = FastAPI()

#def hell():
#    return {"Hello": "World"}

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: str = None):
#    return {"item_id": item_id, "q": q}

import inspect
from fastapi import FastAPI
import uvicorn
from bikeshare_model.predict import make_prediction
from bikeshare_model import __version__ as model_version

#trained_model = load_model('/dist/bikeshare_model-0.0.1-py2.py3-none-any.whl')
app = FastAPI()
#my_model = model.load_model()

@app.get("/predict/")
def predict():
    frame = inspect.currentframe()
    try:
        wheel_file = inspect.getfile(frame.f_back)
        #class DataInputSchema(BaseModel):
        #    dteday: Optional[Union[str, datetime]]
        #    season: Optional[str]
        #    hr: Optional[str]
        #    holiday: Optional[str]
        #    weekday: Optional[str]
        #    workingday: Optional[str]
        #    weathersit: Optional[str]
        #    temp: Optional[float]
        #    atemp: Optional[float]
        #    hum: Optional[float]
        #    windspeed: Optional[float]
        #    yr: Optional[int]
        #    mnth: Optional[str]

        data = {'dteday': '2012-11-6', 'season': 'winter', 'hr': '6pm', 'holiday': 'No', 'weekday': 'Tue',
               'workingday': 'Yes', 'weathersit': 'Clear', 'temp': 16.0, 'atemp': 17.5, 'hum': 30, 'windspeed': 10.0, 'yr': 2012, 'mnth': 'january'}
        prediction = make_prediction(data)
        return {"Prediction": prediction}
    finally:
        del frame

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)