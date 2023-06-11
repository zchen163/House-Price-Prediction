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
        url = 'https://www.bestplaces.net/people/zip-code/california/' + str(city1) + '/' + str(zip1)
        html = urllib.request.urlopen(url).read()
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        p = soup.find_all('p')
        # print(p)

        pop_sent = str(p[8])
        print(pop_sent)
        pop = re.findall('([0-9]+\,[0-9]+)', pop_sent)
        pop_total = pop[0]
        age = re.findall('([0-9]+\.[0-9])', pop_sent)
        print('pop is', pop_total, age[0])
        
        race_sent = str(p[9])
        print(race_sent)
        white = re.findall('([0-9]+\.[0-9])% are white', race_sent)
        black = re.findall('([0-9]+\.[0-9])% are black', race_sent)
        asian = re.findall('([0-9]+\.[0-9])% are asian', race_sent)
        hispanic = re.findall('([0-9]+\.[0-9])% claim Hispanic', race_sent)
        other = round(100 - float(white[0]) - float(black[0]) - float(asian[0]) - float(hispanic[0]), 1)
        print(white[0], black[0], asian[0], hispanic[0], other)
        if other < 0:
            other = 0
        result = [str(zip1), pop_total, age[0], white[0], black[0], asian[0], hispanic[0], other]
        print(result)
        table.append(result)
    except:
        result = [str(zip1), '0', '0', '0', '0', '0', '0', '0']
        table.append(result)


header = ['zipcode', 'population', 'average age', 'race white percentage', 'race black percentage', 'race asian percentage', 'race hispanic percentage', 'race other percentage']
# write into newfile:
with open('people.csv', 'w') as csvwrite:
    writer = csv.writer(csvwrite, delimiter=',')
    writer.writerow(header)
    for i in table:
        writer.writerow(i)

csvwrite.close()
