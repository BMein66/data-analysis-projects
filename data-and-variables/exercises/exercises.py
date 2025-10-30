# 1. Declare and assign the variables here:
shuttle_name = 'Determination'
shuttle_speed_mph = 17500
distance_to_Mars_km = 225000000
distance_to_Moon_km = 384400
miles_per_km = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(distance_to_Mars_km))
print(type(distance_to_Moon_km))
print(type(miles_per_km))


# Code your solution to exercises 3 and 4 here:
miles_to_Mars = distance_to_Mars_km * miles_per_km
hrs_to_Mars = miles_to_Mars / shuttle_speed_mph
days_to_Mars = str(hrs_to_Mars / 24)

# Code your solution to exercise 5 here
miles_to_Moon = distance_to_Moon_km * miles_per_km
hrs_to_Moon = miles_to_Moon / shuttle_speed_mph
days_to_Moon = str(hrs_to_Moon / 24)

print (shuttle_name + " will take " + days_to_Moon + " days to reach the Moon." )
