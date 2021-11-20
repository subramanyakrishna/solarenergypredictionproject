
from time import sleep
from numpy import array
from requests import request
from datetime import date, timedelta
from xgboost import XGBRegressor
model2 = XGBRegressor()
model2.load_model("xgb_r_sklearn.txt")


def getCorrectUnit(X):
    X[1] = 0.621371 * X[1]
    X[5] = 2.23694 * X[5]
    pmb = X[6]
    hm = X[7]
    X[6] = 0.02953 * X[6]  # 0.02953
    pmbmin0_3 = pmb-0.3
    pmbmin0_3toPower0_190284 = pmbmin0_3**0.190284
    hmBYpmbmin0_3toPower0_190284 = hm/pmbmin0_3toPower0_190284
    rightEq = (1+0.0000842288*hmBYpmbmin0_3toPower0_190284)**5.25530260032
    X[7] = pmbmin0_3*rightEq
    X[7] = 0.02953*X[7]
    return X


def refinedData(resFromWebit, altimeter, visibility=0.6):
    cloudcoverage = float(resFromWebit['data'][0]['clouds'])
    temperature = float(resFromWebit['data'][0]['temp'])
    dewpoint = float(resFromWebit['data'][0]['dewpt'])
    relativehumidity = float(resFromWebit['data'][0]['rh'])
    windspeed = float(resFromWebit['data'][0]['wind_spd'])
    stationpressure = float(resFromWebit['data'][0]['pres'])
    X = [cloudcoverage, visibility, temperature, dewpoint,
         relativehumidity, windspeed, stationpressure, altimeter]
    return getCorrectUnit(X)


def locElevationForPerDay(lat, long):
    urlAltitude = "https://api.opentopodata.org/v1/aster30m?locations=" + \
        str(lat)+","+str(long)+""
    resAltimeter = request("GET", urlAltitude).json()
    altimeter = float(resAltimeter['results'][0]['elevation'])
    return altimeter

# date.today().isoformat()


def monthlyData(lat, long, endDate, API_KEY):
    # sleep(5)
    # dates = ['2021-05-22', '2021-05-20', '2021-05-18', '2021-05-16', '2021-05-14', '2021-05-12', '2021-05-10',
    #          '2021-05-08', '2021-05-06', '2021-05-04', '2021-05-02', '2021-04-30', '2021-04-28', '2021-04-26', '2021-04-24']
    # result = [18579.14, 18241.4, 19994.53, 16318.705, 17704.342, 16928.57, 18296.838,
    #           18112.727, 30431.305, 16663.742, 18278.76, 12214.036, 15264.97, 17067.67, 13023.178]

    # return {"result": result, "dates": dates}
    altimeter = locElevationForPerDay(lat, long)
    i = 1
    dataForPrediction = []
    dates = []
    endDate = date.fromisoformat(endDate)
    startDate = (endDate-timedelta(days=1)).isoformat()
    urlWeatherBit = "https://api.weatherbit.io/v2.0/history/hourly?lat="+str(lat)+"&lon="+str(
        long)+"&start_date="+str(startDate)+"&end_date="+str(endDate)+"&tz=local&key="+API_KEY
    resForVisibility = request("GET", urlWeatherBit)
    if resForVisibility.status_code == 428:
        urlWeatherBit = "https://api.weatherbit.io/v2.0/history/hourly?lat="+str(lat)+"&lon="+str(
            long)+"&start_date="+str(startDate)+"&end_date="+str(endDate)+"&tz=local&key="+API_KEY
        resForVisibility = request("GET", urlWeatherBit)
    resFromWebit = resForVisibility.json()
    visibility = float(resFromWebit['data'][12]['vis'])
    while(i < 31):
        days_before_i = (endDate-timedelta(days=i)).isoformat()
        dates.append(days_before_i)
        days_before_iplus1 = (endDate-timedelta(days=i+1)).isoformat()
        apiUrlForMonth = "https://api.weatherbit.io/v2.0/history/daily?lat="+str(lat)+"&lon="+str(
            long)+"&start_date={start}&end_date={end}&key={api_key}".format(start=str(days_before_iplus1), end=str(days_before_i), api_key=API_KEY)
        res = request("GET", apiUrlForMonth).json()
        dataForPrediction.append(refinedData(res, altimeter, visibility))
        i = i+2
    dataForPrediction = array(dataForPrediction)
    result = model2.predict(dataForPrediction)
    result = list(result)
    result = [str(x) for x in result]

    return {"result": result, "dates": dates}
