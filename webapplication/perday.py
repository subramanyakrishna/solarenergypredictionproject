from requests import request


def getWeatherDataForPerDay(lat, long, endDate, startDate, API_KEY):
    urlWeatherBit = "https://api.weatherbit.io/v2.0/history/hourly?lat="+str(lat)+"&lon="+str(
        long)+"&start_date="+str(startDate)+"&end_date="+str(endDate)+"&tz=local&key="+API_KEY
    res = request("GET", urlWeatherBit)
    resFromWebit = res.json()
    return resFromWebit


def locElevationForPerDay(lat, long):
    urlAltitude = "https://api.opentopodata.org/v1/aster30m?locations=" + \
        str(lat)+","+str(long)+""
    resAltimeter = request("GET", urlAltitude).json()
    altimeter = float(resAltimeter['results'][0]['elevation'])
    return altimeter


def refinedDataForPerDay(resFromWebit, i):
    visibility = float(resFromWebit['data'][i]['vis'])
    cloudcoverage = float(resFromWebit['data'][i]['clouds'])
    temperature = float(resFromWebit['data'][i]['temp'])
    dewpoint = float(resFromWebit['data'][i]['dewpt'])
    relativehumidity = float(resFromWebit['data'][i]['rh'])
    windspeed = float(resFromWebit['data'][i]['wind_spd'])
    stationpressure = float(resFromWebit['data'][i]['pres'])
    hour = str(resFromWebit['data'][i]['timestamp_local'])
    hour = int(hour[11:13])
    X = [hour, cloudcoverage, visibility, temperature,
         dewpoint, relativehumidity, windspeed, stationpressure]
    return X
