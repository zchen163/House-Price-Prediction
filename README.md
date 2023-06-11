# House Price Prediction in Los Angeles

* Project is done in collaboration with Shengchen Liu, Kai Ni, Jinjun Liu, Zheng Kuang, Shaojuan Liao. Complete information can be found in GitHub at https://github.com/cse6242-team110-spring2019.

## Introduction

House purchase is a big decision in most people’s life. A good housing price prediction model that can integrate multiple factors is required for both house buyers and sellers when making an important financial decision (Banerjee 2017). Although there have been existing methods for house price prediction, the accuracy isn’t good enough. Besides, most prediction models only adapt physical features of a property, leaving important features unconsidered, such as neighborhood quality, school information, crime rate, etc. In this project, we aim at developing an accurate house price prediction model in Los Angeles area with integration of multiple community/environmental data and local economic indicators. We will use various machine learning algorithms to make the prediction. The results will be presented in the form of visually interactive map.

## Data pre-processing
- Remove irrelevant data
- Remove features containing excessivedeviating values
- Remove redundant / interdependent features

![image](https://github.com/zchen163/House-Price-Prediction/assets/48006055/00c0f9f6-92e6-4cc0-b2a5-a1bf64510d19)

## Experiments

1. Prediction modeling

We used a small sub dataset which has 60,000 instances to do the training and testing. Mean Absolute Error ( MAE ) and logerror were used to evaluate the results.

<img width="302" alt="image" src="https://github.com/zchen163/House-Price-Prediction/assets/48006055/a4b3137a-3208-427d-a996-212f9cb0e345">

Figure 2. The MAE at different max depth of decision tree

![image](https://github.com/zchen163/House-Price-Prediction/assets/48006055/860e872d-4777-4591-b926-229bac9ee3d5)

Figure 3. logerror distribution at Max Depth = 8

2. Prediction using neighborhood information

Six regression models were used here, they are linear regression, ridge regression, lasso regression, support vector regression, random forest, and a naïve ensemble method. 

<img width="425" alt="image" src="https://github.com/zchen163/House-Price-Prediction/assets/48006055/5bb212d2-c788-45e3-98ba-d6ebe9beb77f">

Figure 4. Comparison of calculated mean squared error(left) and coefficient determination of R 2 (right). For all these linear based algorithms, the expanded dataset worked better than the original dataset, giving the lower errors and higher scores.

<img width="426" alt="image" src="https://github.com/zchen163/House-Price-Prediction/assets/48006055/006a0be0-ff3d-4b8d-a863-8303ad38fbfb">

Figure 5. Important features using original data (left) and expanded data (right)

## Map visualization

An interactive map is implemented using Leaflet , an open source JavaScript library for mobile friendly interactive maps.

<img width="588" alt="image" src="https://github.com/zchen163/House-Price-Prediction/assets/48006055/57c84325-ced4-4dcb-bdff-53d20d3bdc61">

Figure 6. Examples of the interactive map created by Leaflet. 

## Description
This project aims to predict house price in Los Angeles and help house-buyers buy a perfect house in Los Angeles. We collected house-intrinsic data such as building year, square feet, number of rooms from Kaggle and environmental data including population, traffic, school, hospital etc. from online resources. We performed house value prediction using various machine learning models including Linear Regression, Ridge and Lasso Regression, Support Vector Machine, Random Forest and Ensemble learning. We demonstrated that incorporating environmental information improved the prediction performance. House information and prediction results are visualized in the form of an interactive map.

Installation and execution are detailed below. Complete information can be found in GitHub at https://github.com/cse6242-team110-spring2019. For demo purpose, we only include necessary files and codes.

## Installation
All the analysis is performed using python unless otherwise specified. The code package consists of code of 1. Web scraping: getting additional data related to house value from external websites other than zillow, such as environmental information, geo-economic information, school information and so on. 2. Data preprocessing and feature engineering. 3. Variable selection and different model comparison. 4. Visualization in the form of interactive map. 

We recommend using python 3.7+ for python scripts. The following packages are required for running modeling on ml.py, matplotlib, panda, numpy, and sklearn.

## Execution
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




        

