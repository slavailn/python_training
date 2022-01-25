user_input = input("Enter login: ") # The program will wait for user input
print(user_input)

# String formatting
user_input = input("Enter login: ")
message = "Hello %s" % user_input # %s will be substituted for variable after %
print(message)

# String formatting in python > 3.6, more readable
user_input = input("Enter login: ")
message = f"Hello {user_input}"
print(message)

# Greeting function
def greet(name):
    greeting = "Hi %s" % name
    return greeting
    
print( greet("Mary") )

# String formatting with multiple variables
f_name = input("First name? ")
l_name = input("Last name? ")
message = "Full name is %s %s" % (f_name, l_name)
print(message)
message = f"Full name is {f_name} {l_name}"
print(message)




