# Caitlyn Rogers
# CSCI 1200A
# Lab Exercise 8.0
# 10/11/21
# lab_8_0.py

print('*** Welcome to Lab Exercise 8.0 ***')

# Task 1
def describe_city(city_name, city_country='japan'):
	"""Display city information"""
	print(f"\n{city_name.title()} is a city in {city_country.title()}.")
	
#Task 2
describe_city('dublin', 'ireland')

#Task 3
describe_city('tokyo')

#Task 4
describe_city(city_country='italy',city_name='rome')

print()
print('*** End Lab 8.0 ***')
