file = open("bear.txt") # open file
print( file.read() ) # read file

# Saving file content to the variable
file = open("bear.txt") # open file
content = file.read() # Reads file content into variable
print(content) # print file content

# Closing file connection
file = open("bear.txt") # open file
file.close() # close file connection
#print('############')
#print( file.read() ) # This will generate error

# Encapsulating file processing, better way to work with files
# 'With' context manager aplies close() method implicitly
with open("bear.txt") as file:
    content = file.read()

print('***********')
print(content)

## ---------------------------------------- ##
# Write text to file
with open("bears.txt", "w") as file:
   file.write("black bear\nbrown bear\nmalay bear")
file.close()


# Read first n line of the file
with open("bears.txt") as file:
   head = [next(file) for x in range(2)]
print(head)

# Read first n characters from file
with open("bears.txt") as file:
   content = file.read(10)
print(content)

# Define a function that takes a character and a filepath
# and returns number of occurences of that character in a file
def character_count(filepath, character):
    with open(filepath, 'r') as file:
        content = file.read()
    num_occur = 0
    for i in content:
        if i == character:
            num_occur = num_occur + 1
    return(content, num_occur)

print( character_count(filepath="bears.txt", character="r") )

# Append the content of a text file to the end of another text file
with open("bear.txt", 'r') as file:
    content = file.read()
    with open("bears.txt", 'a') as file:
        file.write(content)

with open("bears.txt", 'r') as file:
    content = file.read()
    print(content)

# Repeat and append the content of the file N times
print("** ------------ **")
N = 0
while N < 3:
    with open('data.txt', 'r') as file:
        content = file.read()
        with open('data.txt', 'a+') as mod_file:
            mod_file.seek(0)
            mod_file.write(content)
            mod_file.seek(0)

    N = N + 1    













