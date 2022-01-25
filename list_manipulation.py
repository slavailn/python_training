# Some examples of list operations
days = ["monday", "tuesday", "wednesday", "thursday"]
print( days )

# Append item to the end of the list
days.append("friday")
print( days )

# Remove item from the list
days.remove("friday")
print( days )

# Get item index
print( days.index( "monday" ) )

# Get item from the list
print( days[2] )

# Get a slice of the list
print( days[0:2] )
print( days[1:] )
print( days[-1:] )
print( days[-3:-1] )

# Clear the list
days.clear()
print( days )



