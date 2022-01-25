# The fuction takes a list containing both strings and 
# integers and prints out only integers.
out_list = []
def no_strings(mix_list):
    for item in mix_list:
        if isinstance(item, int):
            out_list.append(item)
    return(out_list)

print( no_strings([94, 'no_data', 95, 'no_data', 96]) )

# The function takes a list of numbers and returns numbers greater than 0
over_list = []
def over_zero(num_list):
    for item in num_list:
        if item > 0:
            over_list.append(item)
    return(over_list)

print( over_zero([-2, 5, -6, 7, 0, 1]) )

# The fuction takes a list containing both strings and 
# integers and prints out zeroes instead of strings.
out_list = []
def zero_strings(mix_list):
    for item in mix_list:
        if isinstance(item, int):
            out_list.append(item)
        else:
            out_list.append(0)
    return(out_list)

print( zero_strings([94, 'no_data', 95, 'no_data', 96]) )

# The function sums numbers in the list that 
# are stored as strings
def sum_list(input_list):
    converted_to_nums = []
    for item in input_list:
        converted_to_nums.append(float(item))
    return(sum(converted_to_nums))
    
print(sum_list(['3.1', '2.2', '1.5']))

# Function takes 2 strings as parameters, concatenates and returns the result
def string_concat(s1, s2):
    return(s1 + s2)
    
print( string_concat('3', '4') )

# Function takes a series of numbers with any length 
# and calculates their mean
def mean(*args):
    return( sum(args) / len(args) )

print( mean(1, 2, 3, 4) ) 

# Function takes infinite number of strings
# converts them to uppercase and then sorts
def up_and_sort(*args):
    uppercased = []
    for item in args:
        item = item.upper()
        uppercased.append(item)
    return(sorted(uppercased))
    
print( up_and_sort("snow", "glacier", "iceberg") )














