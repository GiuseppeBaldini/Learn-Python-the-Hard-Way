regions = {
    'Puglia': 'PG',
    'Basilicata': 'BA',
    'Campania': 'CA',
    'Calabria': 'CB',
    'Sicilia': 'SI'
}

cities = {
    'Vieste': 'Puglia',
    'Melfi': 'Basilicata',
    'Napoli': 'Campania',
    'Reggio': 'Calabria',
    'Messina': 'Sicilia'
}

print "Now it's time to learn some geography. More specifically,"
"southern Italy geography."

print "Let's start with abbreviations."
"Puglia's abbreviation is: ", regions['Puglia']
"Campania's abbreviation is: ", regions['Campania'], ". Easy, right?"

print '_*' * 20

print "Time to learn where specific cities are."

print "For example, Vieste is in ", cities['Vieste']
print "Messina is in " , cities['Messina']

print '*_' * 20

print "Let's have a look at all the abbreviations."

for region, abbrev in regions.items():
    print "%s is abbreviated %s." % (region, abbrev)

# Using both lists at the same Time

for city, region in cities.items():
    print """ The city called %s is in %s, which can be abbreviated: %s
    """ % (city, region, regions[region])

print "We shousld create a fantasy city in Italy. Because why not?"

city = cities.get('A city do maaar')

if not city:
    print "This city is hiding from the map. Very clever."

print list(cities.keys())
