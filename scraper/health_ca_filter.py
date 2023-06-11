import pandas as pd

# index_col specify the index column position:
rawData = pd.read_csv('Hospital_General_Information.csv', index_col = 0)
print(rawData)

# use [[]] to select columns,use [0:4] to select rows
data = rawData[['Hospital Name', 'Location', 'ZIP Code', 'State','County Name']]
print(data)

data1 = data[data['State'] == 'CA']
data2 = data1[data1['County Name'].isin(['LOS ANGELES', 'VENTURA', 'ORANGE'])]
print(data2)

data2.to_csv('Hospital.csv')
