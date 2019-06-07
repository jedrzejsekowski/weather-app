import datetime
import requests
import csv
import json

# token
with open('access/token.json') as token:
    token = json.loads(token.read())
    token = "Token " + token['authorization']
headers = {"Authorization":  token}

# csv
filename = "wheaterResults_" + datetime.datetime.now().isoformat() + ".csv"
file = csv.writer(open(filename, "w"), lineterminator='\n')
file.writerow(["Date", "Temperature (F)"])

# yesterday
def yesterday():
    start = datetime.date.today() - datetime.timedelta(days=1)
    end = datetime.date.today()
    #dateRange(start, end)

# last week
def last7days():
    today = datetime.date.today()
    begining = datetime.date.today() - datetime.timedelta(days=7)
    dateRange(begining, today)

# only predefinied last 14 days
def last14days():
    today = datetime.date.today()
    begining = datetime.date.today() - datetime.timedelta(days=14)
    dateRange(begining, today)

# custom days
def customDays():
    start = raw_input("Insert start date YYYY-MM-DD: ") 
    year, month, day = map(int, start.split('-'))
    start = datetime.date(year, month, day)
    end = raw_input("Insert end date YYYY-MM-DD: ")
    year, month, day = map(int, end.split('-'))
    end = datetime.date(year, month, day)
    dateRange(start, end)

# function that make the most of requests
def dateRange(start, end):
    totalRange = end + datetime.timedelta(days=1)
    while start != totalRange:
        columnA = []
        columnB = []

        # formating date into the string usable in request
        start_string = str(start)
        start_string = datetime.datetime.strptime(start_string, '%Y-%m-%d')
        start_string = start_string.strftime('%Y-%m-%d')
        
        requestUrl = "https://api.meteo.pl/api/v1/model/coamps/grid/2a/coordinates/120,82/field/airtmp_sig_fcstfld/level/031050_000010;1/date/" + start_string + "T00/forecast/"
        request = requests.post(requestUrl, headers=headers).json()
        print(request)

        for item in request['times'][:3]:
            columnA.append(item)
        
        for item in request['data'][:3]:
            columnB.append(str(item))
        
        for item1, item2 in zip(columnA, columnB):
            file.writerow([item1, item2])
        
        start = start + datetime.timedelta(days=1)

# menu
def menu():
    options = {
        1: customDays,
        2: yesterday,
        3: last7days,
        4: last14days
    }
    optionNumber = int(input("\nChoose a date range:\n"
                         "----------------------------------\n"
                         "[1]: Custom range\n"
                         "[2]: Yesterday\n"
                         "[3]: Last 7 days\n"
                         "[4]: Last 14 days\n"
                         "[0]: Exit\n\n"
                         "Your option: "))

    # call dict number with function
    options[optionNumber]()

if __name__ == "__main__":
    menu()
    print ("\nSuccessful! File created: " + filename + "\n")