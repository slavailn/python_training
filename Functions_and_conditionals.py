# Functions and conditionals

def check_temp(temp):
    if temp > 25:
        return "Hot"
    elif temp >= 15 and temp <= 25:
        return "Warm"
    else:
        return "Cold"

print( check_temp(26) )
print( check_temp(15) )
print( check_temp(16) )
print( check_temp(14) )

def check_type(string):
    if isinstance(string, str):
        return True
    else: 
        return False

print( check_type("login") )