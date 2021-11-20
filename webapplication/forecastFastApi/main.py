from fastapi.middleware.cors import CORSMiddleware
from sklearn.preprocessing import MinMaxScaler
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from keras.models import load_model
from fastapi import FastAPI, Request


forecastingModel = load_model('forecasting_model')


def getReverseMinMaxvalue(minMaxedValue, min, max):
    return minMaxedValue * (max-min) + min


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

scaler = MinMaxScaler(feature_range=(0, 1))


@app.get('/')
async def ping():
    return {"message": "forecastapi"}


@app.post('/getForecast')
async def get_forcast(info: Request):
    request_body = await info.json()
    tenDayaOutputFromApi = request_body['tenDaysOutputs']
    max_value = max(tenDayaOutputFromApi)
    min_value = min(tenDayaOutputFromApi)
    transformedInputs = scaler.fit_transform(
        np.array(tenDayaOutputFromApi).reshape(-1, 1))
    tenDaySolarOutput = transformedInputs.reshape(1, 10, 1)
    next3DaysOutput = []
    for i in range(0, 3):
        pre = forecastingModel.predict(tenDaySolarOutput)
        # 8th day is added for next prediction
        tenDaySolarOutput = np.append(tenDaySolarOutput, pre[0][0])
        tenDaySolarOutput = tenDaySolarOutput[1:]  # first day is removed
        tenDaySolarOutput = tenDaySolarOutput.reshape(1, 10, 1)

        next3DaysOutput.append(tenDaySolarOutput[0][9][0])
    next3DaysOutput = [round(getReverseMinMaxvalue(
        dayOutput, min_value, max_value), 2) for dayOutput in next3DaysOutput]

    return {'next3DaysOutput': next3DaysOutput}


if(__name__ == "__main__"):
    app.run(debug=True)
