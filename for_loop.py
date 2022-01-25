
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    print(color)

for color in colors:
    if color > 50 and isinstance(color, int):
        print(color)

# Iterate over dictionary
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print( "{} has a number {}".format(key, value) )

for key, value in phone_numbers.items():
    print( "{}: {}".format(key, value))

# Replace + in phone numbers to 00 and print
for phone_numb in phone_numbers.values():
    phone_numb = phone_numb.replace('+', '00', 1)
    print(phone_numb)