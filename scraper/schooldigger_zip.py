import urllib.request, urllib.parse, urllib.error
import json
import csv

 # https://api.schooldigger.com/v1.1/schools?st=CA&city=Los%20Angeles&page=1&perPage=10&appID=96678d7e&appKey=edda74e673d90594cd59dbcdcd9efa8a


serv_url = 'https://api.schooldigger.com/v1.1/schools?'
api_key = 'edda74e673d90594cd59dbcdcd9efa8a'
appID = '96678d7e'

# get lat lng list:
ziplst = []
with open('crime_by_zipcode.csv') as csvread:
    reader = csv.reader(csvread)
    next(reader)
    for line in reader:
        print(line)
        if line[1] != '0':
            ziplst.append(line[0])

# print(addr_lst)
print(ziplst)
print(len(ziplst))

par = {}
par['st'] = 'CA'
# par['zip'] = 90034
par['page'] = 1
par['perPage'] = 50
par['appID'] = appID
par['appkey'] = api_key
count = 0

for i in ziplst:
    par['zip'] = i
    count += 1
    user_url = urllib.parse.urlencode(par)
    url = serv_url + user_url
    print('retrieving...', url)
    # if count > 3:
    #     break
    try:
        data = urllib.request.urlopen(url).read().decode()
        js = json.loads(data)
        # print(json.dumps(js, indent=2))
        number = js['numberOfSchools']
        print(number)
        print(len(js['schoolList']))
        # filename = 'zip' +

        with open('zip_' + i + '.json', 'w') as outfile:
            json.dump(data, outfile)
    except:
        continue
