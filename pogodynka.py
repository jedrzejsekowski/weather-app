import datetime
import requests
import csv
import json

<<<<<<< HEAD
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
=======
# Authorization token
headers = {'Authorization': 'Token {}'.format("yourAuthorizationToken")}

# Create CSV

f = csv.writer(open("wynikiPogodowe_"+datetime.datetime.now().isoformat()+".csv", "w"), lineterminator='\n')

# Columns headers
f.writerow(["Data", "Temperatura (F)"])

# Custom day range
def petlaDni():
    dOd = raw_input("Podaj date rozpoczecia DD/MM/YY: ")
    dDo = raw_input("Podaj date zakonczenia DD/MM/YY: ")

    dataRozpoczecia = datetime.datetime.strptime(dOd, "%d/%m/%y")
    dataZakonczenia = datetime.datetime.strptime(dDo, "%d/%m/%y")

    bezpiecznikDni = dataZakonczenia + datetime.timedelta(days=1)

    while dataRozpoczecia != bezpiecznikDni:
        kolumnaA = []
        kolumnaB = []

        sformatowanaData = str(dataRozpoczecia)[0:10]
        requestUrl = "https://api.meteo.pl:443/api/v1/model/coamps/grid/2a/coordinates/121%2C82/field/airtmp_sig_fcstfld/level/031050_000010%3B1/date/" + sformatowanaData + "T00/forecast/"
        request = requests.post(requestUrl, headers=headers).json()

        for item in request['times'][:3]:
            kolumnaA.append(item)

        for item in request['data'][:3]:
            kolumnaB.append(str(item))

        for item1, item2 in zip(kolumnaA, kolumnaB):
            f.writerow([item1, item2])

        dataRozpoczecia = dataRozpoczecia + datetime.timedelta(days=1)

# Yesterday
def dzienWczorajszy():
    kolumnaA = []
    kolumnaB = []

    wczoraj = datetime.date.today() - datetime.timedelta(days=1)
    sformatowanaData = str(wczoraj)[0:10]
    requestUrl = "https://api.meteo.pl:443/api/v1/model/coamps/grid/2a/coordinates/121%2C82/field/airtmp_sig_fcstfld/level/031050_000010%3B1/date/" + sformatowanaData + "T00/forecast/"
    request = requests.post(requestUrl, headers=headers).json()

    for item in request['times'][:3]:
        kolumnaA.append(item)

    for item in request['data'][:3]:
        kolumnaB.append(str(item))

    for item1, item2 in zip(kolumnaA, kolumnaB):
        f.writerow([item1, item2])


def ostatnie7dni():
    siedemDniTemu = datetime.date.today() - datetime.timedelta(days=7)

    while siedemDniTemu != datetime.date.today():
        kolumnaA = []
        kolumnaB = []

        sformatowanaData = str(siedemDniTemu)[0:10]
        requestUrl = "https://api.meteo.pl:443/api/v1/model/coamps/grid/2a/coordinates/121%2C82/field/airtmp_sig_fcstfld/level/031050_000010%3B1/date/" + sformatowanaData + "T00/forecast/"
        request = requests.post(requestUrl, headers=headers).json()

        for item in request['times'][:3]:
            kolumnaA.append(item)

        for item in request['data'][:3]:
            kolumnaB.append(str(item))

        for item1, item2 in zip(kolumnaA, kolumnaB):
            f.writerow([item1, item2])

        siedemDniTemu = siedemDniTemu + datetime.timedelta(days=1)


def ostatnie30dni():
    trzydziesciDniTemu = datetime.date.today() - datetime.timedelta(days=30)

    while trzydziesciDniTemu != datetime.date.today():
        kolumnaA = []
        kolumnaB = []

        sformatowanaData = str(trzydziesciDniTemu)[0:10]
        requestUrl = "https://api.meteo.pl:443/api/v1/model/coamps/grid/2a/coordinates/121%2C82/field/airtmp_sig_fcstfld/level/031050_000010%3B1/date/" + sformatowanaData + "T00/forecast/"
        request = requests.post(requestUrl, headers=headers).json()

        for item in request['times'][:3]:
            kolumnaA.append(item)

        for item in request['data'][:3]:
            kolumnaB.append(str(item))

        for item1, item2 in zip(kolumnaA, kolumnaB):
            f.writerow([item1, item2])

        trzydziesciDniTemu = trzydziesciDniTemu + datetime.timedelta(days=1)



options = {
    1 : petlaDni,
    2 : dzienWczorajszy,
    3 : ostatnie7dni,
    4 : ostatnie30dni,
}

numerFunkcji = int(input("\nHi there, this is list of wheater range:\n"
>>>>>>> b02418eb97e52aea4426b0bb832c411359bd80e1
                         "----------------------------------\n"
                         "[1]: Custom range\n"
                         "[2]: Yesterday\n"
                         "[3]: Last 7 days\n"
<<<<<<< HEAD
                         "[4]: Last 14 days\n"
                         "[0]: Exit\n\n"
                         "Your option: "))

    # call dict number with function
    options[optionNumber]()

if __name__ == "__main__":
    menu()
    print ("\nSuccessful! File created: " + filename + "\n")
=======
                         "[4]: Last 30 days\n"
                         "[0]: Exit\n\n"
                         "Choose function: "))

options[numerFunkcji]()

print ("\nSuccessful! File created: wynikiPogodowe_"+datetime.datetime.now().isoformat()+".csv\n")
>>>>>>> b02418eb97e52aea4426b0bb832c411359bd80e1
