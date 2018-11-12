import datetime
import requests
import csv
import json

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
                         "----------------------------------\n"
                         "[1]: Custom range\n"
                         "[2]: Yesterday\n"
                         "[3]: Last 7 days\n"
                         "[4]: Last 30 days\n"
                         "[0]: Exit\n\n"
                         "Choose function: "))

options[numerFunkcji]()

print ("\nSuccessful! File created: wynikiPogodowe_"+datetime.datetime.now().isoformat()+".csv\n")