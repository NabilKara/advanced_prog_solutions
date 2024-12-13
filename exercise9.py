print("Enter the name of the cities one by one [enter 'stop' in order to exit]")
cityname = input()
cities = {}
MILLION = 10 ** 6
while cityname.lower() != "stop" :
    cities[cityname] = len(cityname) * MILLION
    cityname = input()
cities = dict(sorted(cities.items(), key=lambda x: x[1], reverse=True))
for city,population in cities.items():
    print(f"City : {city} , Population: {population}")