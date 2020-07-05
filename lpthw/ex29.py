# DICTIONARIES

#create a mapping of state to abbreviations
states = {
    'Odisha': 'OD',
    'Rajasthan': 'RJ',
    'West Bengal': 'WB',
    'Maharashtra': 'MH',
    'Kerala': 'KL'
}

#create a basic set of states and some cities in them
cities = {
    'RJ': 'Jaipur',
    'MH': 'Mumbai',
    'WB': 'Kolkata',
    'KL': 'Trivandrum'
}

#add some more cities
cities['RJ'] = 'Ajmer'
# Ajmer is added but Jaipur is deleted
cities['OD'] = 'Bhubhaneshwara'

#print out some cities
print('-' * 30)
print("OD state has: ", cities['OD'])
print("RJ statae has: ", cities['RJ'])


# print some states
print('-' * 30)
print("Maharashtra's abbreviation is: ", states['Maharashtra'])
print("Kerala's abbreviation is: ", states['Kerala'])

# do it by using state then cities dict
print('-' * 30)
print("Maharashtra has: ", cities[states['Maharashtra']])
print("West Bengal has: ", cities[states['West Bengal']])

# print every state abbreviation
print('-' * 30)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")

# print every city in state
print('-' * 30)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 30)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated as {abbrev}")
    print(f"and has city/cities {cities[abbrev]}")

print('-' * 30)
#safely get a abbreviation by state that might not be there
state = states.get('Goa')

if not state:
    print("Sorry, no Goa.")

# get a city with a default value
city = cities.get('GO', 'Does not exist')
print(f"The city for the state 'GO' is: {city}")
