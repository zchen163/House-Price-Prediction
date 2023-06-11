# crawling data from https://www.bestplaces.net/crime/zip-code/california/los_angeles/<zipcode>

#Parse data using BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import csv

table = []
data = open('orange_venturacountyzipcodes.txt', 'r')
for line in data:
    # print(line.rstrip())
    zip = re.findall('([0-9]+)', line)
    zip1 = zip[0]
    city = re.findall('\((.*?)\)', line)
    city1 = city[0].replace(' ', '_').lower()
    # print(zip[0], city1)
    try:
        url = 'https://www.bestplaces.net/crime/zip-code/california/' + str(city1) + '/' + str(zip1)
        html = urllib.request.urlopen(url).read()
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        # print(tag)
        h5 = soup.find_all('h5')
        vio_sent = str(h5[0])
        # print(vio_sent)
        # print(type(vio_sent))
        vio_crime = re.findall('violent crime is ([0-9]+.[0-9])', vio_sent)

        prop_sent = str(h5[1])
        prop_crime = re.findall('property crime is ([0-9]+.[0-9])', prop_sent)
        result = [str(zip1), vio_crime[0], prop_crime[0]]
        table.append(result)
        print(result)
    except:
        result = [str(zip1), '0', '0']
        table.append(result)


header = ['zipcode', 'violent_crime_index', 'property_crime_index']
# write into newfile:
with open('crime_by_zipcode_part2.csv', 'w') as csvwrite:
    writer = csv.writer(csvwrite, delimiter=',')
    writer.writerow(header)
    for i in table:
        writer.writerow(i)

csvwrite.close()
