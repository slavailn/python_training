# Initiate dictionary
average_temps = {"May": 10.5, "Jun": 25.4, "July": 26.7}
print(average_temps)

# Get keys
print( average_temps.keys() )

# Get values
print( average_temps.values() )

# Return the value of a specified key
print( average_temps.get("May") )

# Update dictionary with a specified key-value pair
average_temps.update({"Aug": 26.5}) 
print(average_temps)

# Remove element with a specified key
average_temps.pop("Aug")
print(average_temps)

# Remove all elements from the dictionary
average_temps.clear()
print(average_temps)

