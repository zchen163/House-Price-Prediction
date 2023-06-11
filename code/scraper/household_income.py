# crawling data from https://www.bestplaces.net/crime/zip-code/california/los_angeles/<zipcode>

#Parse data using BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import csv

table = []
data = open('all3county_zipcodes.txt', 'r')
for line in data:
    # print(line.rstrip())
    zip = re.findall('([0-9]+)', line)
    zip1 = zip[0]
    city = re.findall('\((.*?)\)', line)
    city1 = city[0].replace(' ', '_').lower()
    # print(zip[0], city1)
    try:
        url = 'https://www.bestplaces.net/economy/zip-code/california/' + str(city1) + '/' + str(zip1)
        html = urllib.request.urlopen(url).read()
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        p = soup.find_all('p')
        # print(p)

        sent = str(p[11])
        print(sent)
        income = re.findall('([0-9]+\,[0-9]+)', sent)
        print('income is', income[2])

        result = [str(zip1), income[2]]
        print(result)
        table.append(result)
    except:
        result = [str(zip1), '0']
        table.append(result)


header = ['zipcode', 'household income']
# write into newfile:
with open('household_income.csv', 'w') as csvwrite:
    writer = csv.writer(csvwrite, delimiter=',')
    writer.writerow(header)
    for i in table:
        writer.writerow(i)

csvwrite.close()
