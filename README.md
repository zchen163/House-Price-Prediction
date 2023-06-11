# CSE6242_Project: House Price Prediction in Los Angeles

## DESCRIPTION
This project aims to predict house price in Los Angeles and help house-buyers buy a perfect house in Los Angeles. We collected house-intrinsic data such as building year, square feet, number of rooms from Kaggle and environmental data including population, traffic, school, hospital etc. from online resources. We performed house value prediction using various machine learning models including Linear Regression, Ridge and Lasso Regression, Support Vector Machine, Random Forest and Ensemble learning. We demonstrated that incorporating environmental information improved the prediction performance. House information and prediction results are visualized in the form of an interactive map.

Installation and execution are detailed below. Complete information can be found in GitHub at https://github.com/cse6242-team110-spring2019. For demo purpose, we only include necessary files and codes.

## INSTALLATION
All the analysis is performed using python unless otherwise specified. The code package consists of code of 1. Web scraping: getting additional data related to house value from external websites other than zillow, such as environmental information, geo-economic information, school information and so on. 2. Data preprocessing and feature engineering. 3. Variable selection and different model comparison. 4. Visualization in the form of interactive map. 

We recommend using python 3.7+ for python scripts. The following packages are required for running modeling on ml.py, matplotlib, panda, numpy, and sklearn.

## EXECUTION
Just need to run the python code for all four stages one by one.
1. Web scraping. In scraper folderMore detailed information is in datascraping_readme.txt

(1.1) rev_geo.py: using property longitude and latitude to find address and zip code (zip code from zillow kaggle competition is incorrect)

(1.2). Commute.py: zip code avg commute time

(1.3). Crimeindex.py: zip level crime rate 

(1.4). Health_ca_filter.py : zip level hospital 

(1.5). Household_income.py zip level household income

(1.6). People.py: zip code demographic information

(1.7). Schooldigger_rating.py, schooldigger_rating_dataprocess.py : zip level school data and pre-process data to get information such as  enrollment ratio, free lunch and so on

2. Data preprocess:

(2.1). Data_clean_ols_rf.ipynb zillow data preprocessing and feature engineering, benchmarking model

(2.2) preprocessing.R data preprocessing and feature engineering using expanded data, visualization of house value prediction results

(2.3) Note: The original data is very big, > 500 MB. Therefore, for demo purpose, please download the corresponding data from the google drive link below:
https://drive.google.com/open?id=1VmO0_R_UM5USD9TtXkazqRG07cV44xKH
The folder contains all the original Kaggle data, environmental data and intermediate data required for testing the code

3. Modeling

(3.1) ml.py applying linear regression, ridge, lesso, SVM, random forest using zillow or expanded data

(3.2)

4. Map visualization: in Map folder

(4.1). Package to include: jquery-2.1.1.min.js, rodents.geojson, 

(4.2) style code: los_angeles.css, los_angeles.js

(4.3). Load data; load_csv.html

(4.4). Map visualization: los_angeles.html, ratmap.html




        

