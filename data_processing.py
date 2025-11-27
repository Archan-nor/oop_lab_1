import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

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
germany = []
for i in cities:
    if i['country'] == 'Germany':
        germany.append(i['city'])
print('All cities in Germany:')
print(germany)
print("")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
# Print all cities in Spain with a temperature above 12°C

Spain = []
for i in cities:
    if i['country'] == 'Spain':
        if float(i['temperature']) > 12:
            Spain.append(i['city'])
print('All cities in Spain with a temperature above 12°C:')
print(Spain)
print("")

# Count the number of unique countries

temp = []
for i in cities:
    if i['country'] in temp:
        continue
    else:
        temp.append(i['country'])
print('Count the number of unique countries:',end=' ')
print(len(temp))
print("")

# Print the average temperature for all the cities in Germany
germany = []
for i in cities:
    if i['country'] == 'Germany':
        germany.append(float(i['temperature']))
avggerman = sum(germany)/len(germany)
print('Average temperature for all the cities in Germany:')
print(avggerman)
print("")

# Print the max temperature for all the cities in Italy
italy = []
for i in cities:
    if i['country'] == 'Italy':
        italy.append(float(i['temperature']))
print('Max temperature for all the cities in Italy')
print(max(italy))
