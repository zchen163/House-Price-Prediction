import json
import csv
from decimal import Decimal

# sampledata of js['schoollist'][0]
# sampledata = '''{
#             "schoolid": "060000113904",
#             "schoolName": "Community Collaborative Charter",
#             "phone": "(760) 494-9646",
#             "url": "https://www.schooldigger.com/go/CA/schools/0000113904/school.aspx",
#             "urlCompare": "https://www.schooldigger.com/go/CA/schools/0000113904/search.aspx",
#             "address": {
#                 "street": "32248 Crown Valley Rd.",
#                 "city": "Acton",
#                 "state": "CA",
#                 "stateFull": "California",
#                 "zip": "93510",
#                 "zip4": "2620",
#                 "cityURL": "https://www.schooldigger.com/go/CA/city/Acton/search.aspx",
#                 "zipURL": "https://www.schooldigger.com/go/CA/zip/93510/search.aspx",
#                 "html": "32248 Crown Valley Rd.<br />Acton, CA 93510-2620"
#             },
#             "lowGrade": "K",
#             "highGrade": "12",
#             "schoolLevel": "Alternative",
#             "isCharterSchool": "Yes",
#             "isMagnetSchool": "No",
#             "isVirtualSchool": "Yes",
#             "isTitleISchool": "(n/a)",
#             "isTitleISchoolwideSchool": "(n/a)",
#             "district": {
#                 "districtID": "0600001",
#                 "districtName": "Acton-Agua Dulce Unified",
#                 "url": "https://www.schooldigger.com/go/CA/district/00001/search.aspx",
#                 "rankURL": "https://www.schooldigger.com/go/CA/districtrank.aspx?finddistrict=00001"
#             },
#             "county": {
#                 "countyName": "Los Angeles",
#                 "countyURL": "https://www.schooldigger.com/go/CA/county/Los+Angeles/search.aspx"
#             },
#             "rankHistory": null,
#             "rankMovement": null,
#             "schoolYearlyDetails": [
#                 {
#                     "year": 2017,
#                     "numberOfStudents": 1924,
#                     "percentFreeDiscLunch": 23.75,
#                     "percentofAfricanAmericanStudents": 3.12,
#                     "percentofAsianStudents": 7.9,
#                     "percentofHispanicStudents": 31.24,
#                     "percentofIndianStudents": 0.05,
#                     "percentofPacificIslanderStudents": 0.05,
#                     "percentofWhiteStudents": 45.27,
#                     "percentofTwoOrMoreRaceStudents": 12.37,
#                     "percentofUnspecifiedRaceStudents": null,
#                     "teachersFulltime": 107.1,
#                     "pupilTeacherRatio": 17.9,
#                     "numberofAfricanAmericanStudents": 60,
#                     "numberofAsianStudents": 152,
#                     "numberofHispanicStudents": 601,
#                     "numberofIndianStudents": 1,
#                     "numberofPacificIslanderStudents": 1,
#                     "numberofWhiteStudents": 871,
#                     "numberofTwoOrMoreRaceStudents": 238,
#                     "numberofUnspecifiedRaceStudents": null
#                 }
#             ],
#             "isPrivate": false,
#             "privateDays": null,
#             "privateHours": null,
#             "privateHasLibrary": null,
#             "privateCoed": null,
#             "privateOrientation": null,
#             "hasBoundary": false
#         }'''


ziplst = []
with open('crime_by_zipcode.csv') as csvread:
    reader = csv.reader(csvread)
    next(reader)
    for line in reader:
        print(line)
        if line[1] != '0':
            ziplst.append(line[0])

# print(addr_lst)
# print(ziplst)
print(len(ziplst))

table = []

# ziplst = ['93510', '90034']
for i in ziplst:
    filename = 'zip_' + i + '.json'
    # count += 1
    with open(filename) as readfile:
        data = json.load(readfile) # load .json file into a string
        js = json.loads(data) # parse json file
        js1 = json.dumps(js, indent = 4)
        # print(js1)
        try:
            number = js['numberOfSchools']
            schoollist = js['schoolList']
            print(number)
            print(len(schoollist))
            for i in schoollist:
                schoolid = i['schoolid']
                schoolname = i['schoolName']
                schoolzip = i['address']['zip']
                try:
                    schoollevel = i['schoolLevel']
                except:
                    schoollevel = 'NA'
                if i['isPrivate'] is True:
                    schooltype = 'private'
                elif i['isCharterSchool'] == 'Yes':
                    schooltype = 'charter'
                else:
                    schooltype = 'public'
                tsratio = i['schoolYearlyDetails'][0]['pupilTeacherRatio']
                freelunch = i['schoolYearlyDetails'][0]['percentFreeDiscLunch']
                ethnic_african = i['schoolYearlyDetails'][0]['percentofAfricanAmericanStudents']
                ethnic_asian = i['schoolYearlyDetails'][0]['percentofAsianStudents']
                ethnic_hispanic = i['schoolYearlyDetails'][0]['percentofHispanicStudents']
                ethnic_white = i['schoolYearlyDetails'][0]['percentofWhiteStudents']
                ethnic_tworace= i['schoolYearlyDetails'][0]['percentofTwoOrMoreRaceStudents']
                ethnic_other = round(100 - float(ethnic_asian) - float(ethnic_african) - float(ethnic_white) - float(ethnic_hispanic) - float(ethnic_tworace), 2)
                if ethnic_other < 0:
                    ethnic_other = 0
                line = [schoolid, schoolname, schoolzip, schoollevel, schooltype, tsratio, freelunch, ethnic_african, ethnic_asian, ethnic_hispanic, ethnic_white, ethnic_tworace, ethnic_other]
                print(line)
                table.append(line)
        except:
            line = ['schoolid', 'schoolname', 'zip', 'schoollevel', 'schooltype', 'teacher student ratio', 'freelunch ratio', 'ethnic african ratio', 'ethnic asian ratio', 'ethnic hispanic ratio', 'ethnic white student ratio', 'ethnic two_or_more ratio', 'ethnic others ratio']
            continue

header = ['schoolid', 'schoolname', 'zip', 'schoollevel', 'schooltype', 'teacher student ratio', 'freelunch ratio', 'ethnic african ratio', 'ethnic asian ratio', 'ethnic hispanic ratio', 'ethnic white student ratio', 'ethnic two_or_more ratio', 'ethnic others ratio']
# write into newfile:
with open('all_school_data.csv', 'w') as csvwrite:
    writer = csv.writer(csvwrite, delimiter=',')
    writer.writerow(header)
    for i in table:
        writer.writerow(i)

csvwrite.close()
