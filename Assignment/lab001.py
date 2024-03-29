batman = "Bruce Wayne"
first = batman[0]  # Accessing the first character
print(first)
space = batman[5]  # Accessing the empty space in the string
print(space)
last = batman[len(batman) - 1]
print(last)
# The following will produce an error since the index is out of bounds
# err = batman[len(batman)]

my_string = "This is MY string!"
print(my_string[:8])  # All the characters before 'M'
print(my_string[8:])  # All the characters starting from 'M'
print(my_string[:])  # The whole string
print(my_string[::-1])  # The whole string in reverse (step is -1)