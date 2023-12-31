

provinces = {
	'British Columbia' : 'BC',
	'Ontario' : 'ON',
	'Alberta' : 'AB'
}

canada_cities = {
	'BC':'Vancouver',
	'ON' : 'Ontario',
	'AB' : 'Alberta'
}

states = {
	'Oregon' : 'OR',
	'Florida': 'FL',
	'California' : 'CA',
	'New york' : 'NY',
	'Michigan' : 'MI'
}


cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville',
	'WA': 'Seattle'
}

megalist = [provinces, states]

cities['NY'] = 'New York'
cities['OR'] = 'Portland'


print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation 
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")
	
# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in (states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there 
state = states.get('Texas')

if not state:
	print("Sorry, no Texas.")

#get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")

print('-' * 10)
for country in megalist:
	for state, abbrev in country.items():
		if "British Columbia" in country.keys():
			print(f"{state} is abbreviated as {abbrev} and has: ", canada_cities[abbrev])
		elif "Oregon" in country.keys():
			print(f"{state} is abbreviated as {abbrev} and has: ", cities[abbrev])
	

