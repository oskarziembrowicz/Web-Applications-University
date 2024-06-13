import requests

# Pobieranie wszystkich stacji
URL_ALL = 'https://api.gios.gov.pl/pjp-api/rest/station/findAll'
stations = requests.get(URL_ALL).json()
print('----------------')
print('STACJE POMIAROWE')
print('----------------')
for station in stations:
    print(f'Stacja: {station["stationName"]}, ID: {station["id"]}')


station_id = input('\nWpisz ID stacji, aby wyświetlić szczegóły: ')


# Wyświetlenie danych o stacji
URL_STATION = f'https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/{station_id}'
station_data = requests.get(URL_STATION).json()
print('\n--------------')
print('DANE ZE STACJI')
print('--------------')

data = 'Brak danych' if station_data["stIndexLevel"] == None else station_data["stIndexLevel"]["indexLevelName"]
print(f'Ogólny status zanieczyszczeń:\t{data}')

data = 'Brak danych' if station_data["so2IndexLevel"] == None else station_data["so2IndexLevel"]["indexLevelName"]
print(f'Wskaźnik poziomu dwutlenku siarki (SO2):\t{data}')

data = 'Brak danych' if station_data["no2IndexLevel"] == None else station_data["no2IndexLevel"]["indexLevelName"]
print(f'Wskaźnik poziomu dwutlenku azotu (NO2):\t{data}')

data = 'Brak danych' if station_data["pm10IndexLevel"] == None else station_data["pm10IndexLevel"]["indexLevelName"]
print(f'Wskaźnik poziomu pyłu zawieszonego (PM10):\t{data}')

data = 'Brak danych' if station_data["pm25IndexLevel"] == None else station_data["pm25IndexLevel"]["indexLevelName"]
print(f'Wskaźnik poziomu pyłu zawieszonego (PM25):\t{data}')

data = 'Brak danych' if station_data["o3IndexLevel"] == None else station_data["o3IndexLevel"]["indexLevelName"]
print(f'Wskaźnik poziomu ozonu (O3):\t{data}')


# Wyświetlenie listy stanowisk pomiarowych
URL_POSITIONS = f'https://api.gios.gov.pl/pjp-api/rest/station/sensors/{station_id}'
positions = requests.get(URL_POSITIONS).json()
print('\n--------------------')
print('STANOWISKA POMIAROWE')
print('--------------------')
for position in positions:
    print(f'STANOWISKO Rodzaj pomiaru: {position["param"]["paramName"]} ({position["param"]["paramFormula"]}), ID: {position["id"]}')

position_id = input('\nWpisz ID stanowiska pomiarowego, aby wyświetlić pomiary: ')

URL_POSITION = f'https://api.gios.gov.pl/pjp-api/rest/data/getData/{position_id}'
position_measurements = requests.get(URL_POSITION).json()
print('\n-------------')
print('Pomiary: ' + position_measurements['key'])
print('-------------')
for measurement in position_measurements['values']:
    print(f'\tData: {measurement["date"]}')
    print(f'\tWartość: {measurement["value"]}\n')


