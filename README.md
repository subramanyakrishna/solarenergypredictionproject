# Solar Energy Prediction Project
This repo contains codes for solarneergyprediction web application we created with colaboration with nokia
You can access the website [here](https://solarenergyprediction.herokuapp.com/)
(Website might lag sometimes since server will go to sleep after 30 min of inactivity)
## Intro
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
## Contributors
Web Application development - [Subramanya K](https://github.com/subramanyakrishna) ,[K Shivanithyanathan](https://github.com/shivanithyak)  
Xgboost and GBR model building - [Roshan Nayak](https://github.com/RosNayak)  
Dataset creation and Model Building - [Priyanshu M](https://github.com/priyanshu-m)  
Forecasting - [Venkatesh Subramanya Iyer Giri](https://github.com/vendroid7)
