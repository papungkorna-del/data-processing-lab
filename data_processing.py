import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
print("FIRST 5 CITIES:")
for city in cities[:5]:
    print(city)
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("GERMANY CITIES:")
german_cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        if r['country'] == 'Germany':
            german_cities.append(dict(r))

    for city in german_cities:
        print(city)
print()

# Print all cities in Spain with a temperature above 12°C
print("SPAIN CITIES WITH TEMPERATURE ABOVE 12°C:")
spain_cities = []

with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        if r['country'] == 'Spain':
            if r['temperature'] > '12':
                spain_cities.append(dict(r))

    for city in spain_cities:
        print(city)
print()

# Count the number of unique countries
cnt_cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cnt_cities.append(r['country'])

print("Unique Countries Count:")
print(len(set(cnt_cities)))
print()

# Print the average temperature for all the cities in Germany
german_avg_temp = []
for city in german_cities:
    german_avg_temp.append(float(city['temperature']))

print("German Cities Average Temp:")
print(sum(german_avg_temp)/len(german_avg_temp))
print()

# Print the max temperature for all the cities in Italy
italy_cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        if r['country'] == 'Italy':
            italy_cities.append(dict(r))

max_temp = [float(city['temperature']) for city in italy_cities]
print("Max Italy City Temp:")
print(max(max_temp))
print()

