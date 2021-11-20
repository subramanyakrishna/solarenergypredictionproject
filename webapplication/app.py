from datetime import date, timedelta
import mainpage
import perday
import numpy as np
from monthly import monthlyData
import utils
from flask import Flask, render_template, request
from pickle import load
from random import choice
gbrModel = load(open('gbr1.pkl', 'rb'))


app = Flask(__name__)

# render main page
API_KEY = choice(['8beb38e482734df9bb81eb1e724aa3b9',
                 'dfdad03e8a3440d190ff52602a1739fb'])


@app.route('/')
def man():
    # this by itself selects template folder
    return render_template('index.html')

# returns solar energy distribution in different times in a day and total production in a day


def getPerDayChart(lat, long, endDate, startDate, API_KEY):
    # returns response from weatherbit for hourly prediction
    resFromWebit = perday.getWeatherDataForPerDay(
        lat, long, endDate, startDate, API_KEY)
    # get elevetion data at that location using opentopodataapi
    altimeter = perday.locElevationForPerDay(lat, long)
    solarOutputPerhours = list()
    time = list()
    for i in range(0, 24):
        X = perday.refinedDataForPerDay(resFromWebit, i)
        X.append(altimeter)
        X = utils.getCorrectUnitPerDay(X)
        # if data in between 0 to 5 or 18 to 24 no solar energy is created
        if (X[0] >= 0 and X[0] <= 5) or (X[0] >= 18 and X[0] <= 24):
            solarOutputPerhours.append(0)
            time.append(X[0])
            continue
        time.append(X[0])
        X = list([X])
        pred = gbrModel.predict(X)
        solarOutputPerhours.append(pred[0])
        X = []
    solarOutputPerDay = sum(solarOutputPerhours)
    return solarOutputPerhours, time, solarOutputPerDay

# return the predicted results for  given location and date


@app.route('/perday', methods=['POST'])
def home():
    # get lat,lng,enddate from request
    lat = float(request.form['lat'])
    long = float(request.form['long'])
    endDate = request.form['endDate']
    return render_template('perday.html', lat=lat, long=long, endDate=endDate)


@app.route('/monthly', methods=['POST', 'GET'])
def monthlyRoute():
    lat = float(request.args.get('lat'))
    long = float(request.args.get('long'))
    endDate = request.args.get('endDate')
    return monthlyData(lat, long, endDate, API_KEY)


@app.route('/result', methods=['POST', 'GET'])
def result():
    lat = float(request.args.get('lat'))
    long = float(request.args.get('long'))
    endDate = request.args.get('endDate')
    # get the current time in that location
    hour = utils.getTime(lat, long)

    endDate = date.fromisoformat(endDate)
    # if selected date is more than todays date return error since we don't have data for that
    if date.today() < endDate:
        return {"response": "Please select date lesser than todays date since we can't get the future environmental condition to predict solar output", "mainpageUrl": "https://solaroutputprediction.herokuapp.com/"}
    # check wherther api under limit
    if(utils.checkLimitExceeded(API_KEY) == True):
        return {"response": "Weatherbit API limit exceeded"}

    startDate = (endDate-timedelta(days=1)).isoformat()

    # get predited data to plot chart of solar energy production in diffent time in that day
    solarOutputPerhours, times, solarOutputPerDay = getPerDayChart(
        lat, long, endDate, startDate, API_KEY)

    X, city_name = mainpage.getWeatherData(lat, long, hour, API_KEY)

    X = utils.getCorrectUnit(X)

    averageSolarEnergyPerHour = round(sum(solarOutputPerhours)/12, 2)
    costsavings = round(5.73*averageSolarEnergyPerHour, 2)
    co2 = round(0.185*averageSolarEnergyPerHour, 2)
    # if current time is between given range then output is zero
    solarOutputPerhours = utils.rotateArray(solarOutputPerhours, 24, 1)
    times = utils.rotateArray(times, 24, 1)
    if (hour >= 0 and hour <= 5) or (hour >= 18 and hour <= 24):
        return {'currTimeprediction': '0  kWh', 'solarOutputPerhours': solarOutputPerhours, 'time': times, 'solarOutputPerDay': '{}  kWh'.format(round(solarOutputPerDay, 2)), 'costsavings': '₹ {} per hour'.format(costsavings), 'averageSolarEnergyPerHour': '{} kWh'.format(round(averageSolarEnergyPerHour, 2)), 'co2': '{}  kg'.format(co2), 'city_name': city_name, 'lat': lat, 'long': long, 'endDate': endDate, 'co2NoOfTree': int(co2/21)}
    X = list([X])
    pred = round(gbrModel.predict(X)[0], 3)
    return {'currTimeprediction': '{} kWh'.format(round(pred, 2)), 'solarOutputPerhours': solarOutputPerhours, 'time': times, 'solarOutputPerDay': '{}  kWh'.format(round(solarOutputPerDay, 2)), 'costsavings': '₹ {} per hour'.format(costsavings), 'averageSolarEnergyPerHour': '{} kWh'.format(round(averageSolarEnergyPerHour, 2)), 'co2': '{}  kg'.format(co2), 'city_name': city_name, 'lat': lat, 'long': long, 'endDate': endDate, 'co2NoOfTree': int(co2/21)}


if(__name__ == "__main__"):
    app.run(debug=True)
