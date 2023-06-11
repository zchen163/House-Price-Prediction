import json
import csv

schoolidlst = []
with open('schooldigger_all_data.csv') as csvread:
    reader = csv.reader(csvread)
    next(reader)
    for line in reader:
        # print(line)
        schoolidlst.append(line[0])

# print(schoolidlst)
# print(len(schoolidlst))

testdata = ['060000109444', '062100002518', '062100002521']
table = []
count = 0

for i in schoolidlst:
    filename = i + '.json'
    count += 1
    try:
        with open(filename) as readfile:
            data = json.load(readfile) # load .json file into a string
            js = json.loads(data) # parse json file
            js1 = json.dumps(js, indent = 4)
            # print(js1)
            try:
                id = js['schoolid']
                name = js['schoolName']
                zip = js['address']['zip']
                lat = js['address']['latLong']['latitude']
                lng = js['address']['latLong']['longitude']
                county = js['county']['countyName']
                level = js['schoolLevel']
                if js['isPrivate'] is True:
                    type = 'private'
                elif js['isCharterSchool'] == 'Yes':
                    type = 'charter'
                elif js['isVirtualSchool'] == 'Yes':
                    type = 'virtual'
                else:
                    type = 'public'
                try:
                    history = js['rankHistory']
                    scorelst = []
                    for j in history:
                        # print(j['year'])
                        scorelst.append(j['averageStandardScore'])
                    # print(scorelst)
                    score = round(sum(scorelst)/len(scorelst), 2)
                    # print(score)
                except:
                    score = 'NA'
                    continue
                tsratio = js['schoolYearlyDetails'][0]['pupilTeacherRatio']
                enrollment = js['schoolYearlyDetails'][0]['numberOfStudents']
                freelunch = js['schoolYearlyDetails'][0]['percentFreeDiscLunch']
                ethnic_african = js['schoolYearlyDetails'][0]['percentofAfricanAmericanStudents']
                ethnic_asian = js['schoolYearlyDetails'][0]['percentofAsianStudents']
                ethnic_hispanic = js['schoolYearlyDetails'][0]['percentofHispanicStudents']
                ethnic_white = js['schoolYearlyDetails'][0]['percentofWhiteStudents']
                ethnic_tworace= js['schoolYearlyDetails'][0]['percentofTwoOrMoreRaceStudents']
                ethnic_other = round(100 - float(ethnic_asian) - float(ethnic_african) - float(ethnic_white) - float(ethnic_hispanic) - float(ethnic_tworace), 2)
                if ethnic_other < 0:
                    ethnic_other = 0
                line = [id, name, zip, lat, lng, level, type, score, tsratio, enrollment, freelunch, ethnic_african, ethnic_asian, ethnic_hispanic, ethnic_white, ethnic_tworace, ethnic_other]
                print(line)
                table.append(line)
            except:
                line = ['schoolid', 'schoolname', 'zip', 'lat', 'lng', 'schoollevel', 'schooltype', 'average score', 'teacher student ratio', 'enrollment', 'freelunch ratio', 'ethnic african ratio', 'ethnic asian ratio', 'ethnic hispanic ratio', 'ethnic white student ratio', 'ethnic two_or_more ratio', 'ethnic others ratio']
                table.append(line)
                # faillst.append(i)
                continue
    except:
        continue

header = ['schoolid', 'schoolname', 'zip', 'lat', 'lng', 'schoollevel', 'schooltype', 'average score', 'teacher student ratio', 'enrollment', 'freelunch ratio', 'ethnic african ratio', 'ethnic asian ratio', 'ethnic hispanic ratio', 'ethnic white student ratio', 'ethnic two_or_more ratio', 'ethnic others ratio']
# write into newfile:

resultcount = 0
with open('all_rating_data.csv', 'w') as csvwrite:
    writer = csv.writer(csvwrite, delimiter=',')
    writer.writerow(header)
    for i in table:
        resultcount += 1
        writer.writerow(i)

csvwrite.close()
