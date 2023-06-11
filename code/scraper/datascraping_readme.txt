Data Scraping Readme

1. Reverse geocoding

Filename: rev_geo.py;
Instruction:
The street address and zipcode scraping is done by reverse geocoding provided by Google Map API. The registration of API and getting $300 credit should follow:
https://developers.google.com/maps/documentation/geocoding/intro

2. School Information

Filename: schooldigger_zip.py; schooldigger_zip_dataprocess.py; schooldigger_rating.py; schooldigger_rating_dataprocess.py;
Instruction:
The school data within certain area is done by schooldigger API. Relative regirstration and API information please follow:
https://developer.schooldigger.com/

First use API to search schools within a zipcode, the returned result is a list of school names, followed by data processing. schooldigger_zip.py is for data collection while schooldigger_zip_dataprocess.py is for corresponding data processing.

Then based on the list harvested, we got the rating and detailed information for each school based on their ID using schooldigger_rating.py. The corresponding data processing code is schooldigger_rating_dataprocess.py.

3. Neighborhood information

Filename: commute.py; crimeindex.py; household_income.py; people.py;
Instruction:
The Neighborhood information was collected by raw scrapping from website bestplaces.net. One example link of the crime data within zipcode 90034 is:
https://www.bestplaces.net/crime/zip-code/california/los_angeles/90034

The above codes can be used for directly scrapping commute, crime, economic and people data without API. Note that the website recently updated their layout, so the code may not work. However, it worked for us when we scrapped the data a few weeks ago.

4. Heath Information

Filename: health_ca_filter.py
Instruction:
The general information of all california hospitals can be found at:
https://data.medicare.gov/widgets/xubh-q36u

The code selected zipcodes within Los Angeles, Orange and Ventura county.


*This part of data scraping is done by Chen Zhang (czhang613)
