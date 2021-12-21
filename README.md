# Solar Energy Prediction Project
This repo contains codes for solarneergyprediction web application we created with colaboration with nokia
You can access the website [here](https://solarenergyprediction.herokuapp.com/)
(Website might lag sometimes since server will go to sleep after 30 min of inactivity)
## Introduction
* Solar energy is going to play a measure role in the future global
energy supply. Due to the fluctuating nature of solar energy, an
efficient use is possible depending on reliable forecast information.
* We analyse how the different factors affect the prediction of energy
production and how our dataset can be used to predict the expected
output of sustainable sources.
* As a result, we facilitate users the necessary information to decide
how much they wish to invest according to the desired energy output
for their particular location.
## Data Collection
* The Training dataset was taken from American Meteorological
Society (AMS) 2013-2014 Solar Energy Prediction Contest.
* The dataset is of size 2.84 GB. The data are in netCDF4 files with
each file holding the grids for each ensemble member at every time
step for a particular variable.
* Each netCDF4 file contains the latitude-longitude grid and time step
values as well as metadata listing the full names of each variable and
the associated units.
* Each netCDF4 file contains the total data for one of the model
variables and are stored in a multidimensional array.
## Data Preparation
* Weather features were contained in netCDF4 files stored in a
multidimensional array.
* NetCDF4 libraries available in R language were used to convert
netCDF4 format file for further data cleaning and processing.
* Missing values in time series weather features were replaced using
linear and spline interpolation techniques.
* Daily dataset was prepared by averaging over the entire day (for sunlit
hours) to represent each data by single data instance.
## Model Building and Evaluation
We have worked onvarious model, Below table shows the R2 score of each models
|Model    | R2 Score  |
|---------|-----------|
|Linear regression| 0.44|
|SVR |0.46|
|Linear regression on PCA| 0.53|
|NN with 2 hidden layer| 0.78|
|Random forest |0.82|
|Gradient boosting regressor |0.82|
|LightGBM regressor| 0.83|
|Stack model 1| 0.83|
|XGBOOST regressor |0.84|
|Stack model 2 |0.85|

Note:
* Stack Model 1: Four base estimator and Linear Regressor as Final estimator
* Stack Model 2: Four base estimator and Neural Network with one hidden layer and relu as
activation function
## Time Series Forecasting
* Forecasting in general is the process of making predictions based on
past and present data and most commonly by analysis of trends.
* In Machine Learning we Forecast Time series data by training the
model on past values. Using the technique we can forecast future
data which can be helpful.
* In this project we have forecasted solar energy data by analyzing past
solar energy values.
* We use LSTM i.e., Long short term memory. It is a type of RNN but
it solves many drawbacks which RNN has.
## Application Development
* We developed a web application to help the user to utilize our
machine learning model and predict the total solar energy generation
at a particular location, if they want to set up a solar energy plant.
* Web application is deployed on Heroku: Cloud Application Platform
#### Data Collection using API
* Weatherbit: Weatherbit API is used to retrieve current weather
observations from over 47,000 live weather stations. We provide the
city name, from which the latitude and longitude is retrieved and used
in the API, and the API provides the weather information required.
* Opentopodata: It is an elevation API, which is used for the
“Altimeter” feature.The elevation is provided using the city name or
the latitude and longitude.
* Timezonedb: To get time in given latitude and longitude.
* Opencagedata: The OpenCage Geocoding API provides reverse
(lat/long to text) and forward (text to lat/long) geocoding via a
RESTful API.
#### Backend Functional Process Charts:
##### Backend Process Chart:
![Backend Process Chart](https://user-images.githubusercontent.com/64394655/146876197-bfd299f0-6e7c-4340-a71d-18a047e3a4d4.png)
##### Flow Chart of hourly prediction:
![Flow Chart of hourly prediction](https://user-images.githubusercontent.com/64394655/146876309-c42a626d-44d2-4a9b-8c98-84854560bdf4.png)
##### Flow Chart of Daily prediction:
![Flow Chart of Daily prediction](https://user-images.githubusercontent.com/64394655/146876382-242acca3-0712-4dde-bb75-666acfa520f4.png)
## Future Scope and Conclusion
* Model will aid users for solar Power forecasting at any particular
location in making practical design decisions.
* This forecasting approach is a key step towards the development of a
data-driven decision-making framework for power system operation.
* Similar study and conclusion can be drawn on large scale national
solar grid and wind farms’ energy forecasting models.
## Contributors
Web Application development - [Subramanya K](https://github.com/subramanyakrishna) ,[K Shivanithyanathan](https://github.com/shivanithyak)  
Xgboost and GBR model building - [Roshan Nayak](https://github.com/RosNayak)  
Dataset creation and Model Building - [Priyanshu M](https://github.com/priyanshu-m)  
Forecasting - [Venkatesh Subramanya Iyer Giri](https://github.com/vendroid7)  
Other - [Tanay Somnani](https://github.com/TanSom),[K S Eshwar Subramanya Prasad](https://github.com/EshSubP)

![image](https://user-images.githubusercontent.com/64394655/146876625-ea876c6b-f525-4259-9f9c-d0f4914e6e21.png)

