import urllib.request, urllib.parse, urllib.error
import json
import csv
import time

serv_url = 'https://api.schooldigger.com/v1.1/schools/'
# czhang84@wisc.edu account data, 5000call per day
api_key = '68ae7bee718e7ef2f827972941f0c6c1'
appID = 'a20d7f1b'

# czhang613@gatech.edu account data:
# api_key = 'edda74e673d90594cd59dbcdcd9efa8a'
# appID = '96678d7e'

# get lat lng list:
schoolidlst = []
with open('schooldigger_all_data.csv') as csvread:
    reader = csv.reader(csvread)
    next(reader)
    for line in reader:
        print(line)
        schoolidlst.append(line[0])

print(schoolidlst)
print(len(schoolidlst))

testdata = ['060000109444', '062100002518', '062100002521']

# sample url: https://api.schooldigger.com/v1.1/schools/060000109444?appID=a20d7f1b&appKey=68ae7bee718e7ef2f827972941f0c6c1

par = {}
par['appID'] = appID
par['appkey'] = api_key
count = 0

for i in schoolidlst:
    count += 1
    user_url = urllib.parse.urlencode(par)
    url = serv_url + str(i) + '?' + user_url
    # print(url)
    print('retrieving...', url)
    if count % 100 == 0:
        print('=====Pasue 1min for every 100 requests======')
        time.sleep(60)
    try:
        data = urllib.request.urlopen(url).read().decode()
        js = json.loads(data)
        # print(json.dumps(js, indent=2))
        # name = js['schoolName']
        # print(name)
        with open(i + '.json', 'w') as outfile:
            json.dump(data, outfile)
    except:
        continue
