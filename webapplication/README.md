# solarenergyprediction
This repo contains code for web application which helps to predict solarenergy production in particular area,
You can access the website here : https://solarenergyprediction.herokuapp.com/ 

## Installtion and Usage
Use the environmental.yml to clone my anaconda environment
In current folder run following commands 
```
conda env create -f environment.yml
conda activate solarpredict
python app.py
```
Open another terminal in same location
```
cd forecastFastApi
python main.py
```

forecastFastApi folder contains code for api for deploying forcasting model, This is done because we were using free heruku server with limited slug size(500MB), Since tensorflow has huge installation size we created another api just for just forcasting.

## Folder Structure:
```
│   .gitignore
│   app.py
│   environment.yml
│   gbr1.pkl
│   mainpage.py
│   monthly.py
│   perday.py
│   Procfile
│   README.md
│   requirements.txt
│   utils.py
│   xgb_r_sklearn.txt
│
├───forecastFastApi
│       forecasting_model
│       main.py
│       Procfile
│       requirements.txt
│
├───static
│   │   world.png
│   │
│   ├───javascript
│   │       index.js
│   │
│   └───stylesheets
│           index.css
│           perday.css
│
└───templates
        index.html
        perday.html
```

