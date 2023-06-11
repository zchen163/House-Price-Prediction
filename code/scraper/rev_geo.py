import csv
import json
import urllib.request, urllib.parse, urllib.error
import time

# put your googleapi key here:
api_key = 'AIzaSyA8TR0ALSoKdSF-REu4dsP4t2jd_fXC-2Y'

addr_lst = []
count = 0
parms = {}
newtable = []

# get lat lng list:
with open('2016_coordinates_60000_part1.csv') as csvread:
    reader = csv.reader(csvread)
    next(reader)
    for line in reader:
        # print(line)
        temp_dict = {}
        temp_dict['parcelid'] = line[0]
        temp_dict['lat'] = float(line[1])/1000000
        temp_dict['lng'] = float(line[2])/1000000
        # print(temp_dict)
        addr_lst.append(temp_dict)
# print(addr_lst)
# print(len(addr_lst))

# retrieve url:
for i in addr_lst:
    count = count + 1

    parms['location_type']= 'ROOFTOP'
    parms['key'] = api_key
    serv_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    user_url = urllib.parse.urlencode(parms)
    url = serv_url + 'latlng=' + str(i['lat']) + ',' + str(i['lng']) + '&'+ user_url
    # print(url)
    # print('Retrieving', url, '============')
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    js = json.loads(data)

    # parse data in json:
    try:
        formatted_addr = js['results'][0]['formatted_address']
        number_of_addresses = len(js['results'])
        print(formatted_addr, number_of_addresses)
        newline = [i['parcelid'], i['lat'], i['lng'], formatted_addr,  number_of_addresses]
        newtable.append(newline)
            # print(json.dumps(js1, indent=4))
        print('=====the #', count, 'fetching done=====')
    except:
        newline = [i['parcelid'], i['lat'], i['lng'], 'No result', '0']
        newtable.append(newline)
        print('!!!=====the #', count, 'has no result=====!!!')
        continue
    if (count) % 50 == 0:
        print('Pause 1s for every 50 requests')
        time.sleep(1)
    if (count) % 30010 == 0:
        break

# print(newtable)

header = ['parcelid', 'lat', 'lng', 'formatted address', '# ROOFTOP address fetched']
# write into newfile:
with open('2016_addr_60000_part1.csv', 'w') as csvwrite:
    writer = csv.writer(csvwrite, delimiter=',')
    writer.writerow(header)
    for i in newtable:
        writer.writerow(i)

csvwrite.close()


# example:  https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&location_type=ROOFTOP&key=AIzaSyA8TR0ALSoKdSF-REu4dsP4t2jd_fXC-2Y
# https://maps.googleapis.com/maps/api/geocode/json?latlng=34.11978,-118.384553&location_type=ROOFTOP&key=AIzaSyA8TR0ALSoKdSF-REu4dsP4t2jd_fXC-2Y
