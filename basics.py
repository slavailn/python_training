# Calculate number of hours in a week
num_hours = 24
num_days = 7
num_hours_week = num_hours * num_days
print(num_hours_week)

# Types of variables in python
x = 10 # integer
y = '10' # string
z = 10.0 # float 

print(x + x) # sum of integers is an integer
#print(x + y) # error
print(y + y) # prints '1010' - concatenates strings
print(x + z) # integer plus a float gives float

# Check variable types
print( type(x) ) # returns <<class 'int'>>
print( type(y) ) # returns <<class 'string'>>
print( type(z) ) # returns <<class 'float'>>

# Create list []
rainfall = ['heavy', 'light']
print(rainfall)
multi = [1, 1.0, "10", [1, 2, "cat"]] # list can contain any objects including other lists
print(multi)
type(multi)

# Range
a_range = list(range(1,10))
print(a_range)
a_range = list(range(1, 10, 2)) # range 1 to 10 with a step of 2. The last number will be 9
print(a_range)

# -------------------------------------------------------------- #
# Methods
# Method are work only with specific types
# methods are expressed as <variable>.<method()>, see below
print( 'hello'.upper() ) # capitalize - 'HELLO'
print( 'hello'.title() ) # only first letter is capital - 'Hello'
print( multi.pop() ) # prints the last item of the list

# Functions
# Created by user 

# Calculate average of the list of numbers
grades = [2, 6, 7, 10]
def mean_list(user_list):
    sum_list = sum(user_list) # sum of items 
    len_list = len(user_list) # number of items
    return( sum_list / len_list )

print( mean_list(user_list = grades) )  

# How many items in the list are equal to 10?
grades = [1, 2, 10, 55, 10.0]
print( grades.count(10) ) # 2 items are equal to 10

# ------------------------------------------------------------ #
# TUPLES
# Tuples are immutable lists
temp = (11, 22, 45)
print(temp)
temp = (11, 22, ['morning', 'evening'])
print(temp)

# ------------------------------------------------------------ #
# DICTIONARY
# Create a dictionary {key: value}
student_grades = {'John': 4.75, 'Sim': 10.11, 'Mary': 5.5}
print(student_grades)
# Extract keys
print( student_grades.keys() )
# Extract values
print( student_grades.values() )


















