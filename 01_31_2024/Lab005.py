# String Slicing
# Slicing is the process of obtaining a portion (substring) of a string by using its indices.
# string[start:end]

my_String = "I am learning Python with Selenium"
print(my_String[0:4]) # frm strt till befr the 4th index
print(my_String[1:7])
print(my_String[8:len(my_String)])# frm 8th index till end

# Reverse Slicing
# Reverse Slice
my_string = "This is Oyinkansola!"
print(my_string[13:2:-1]) # Take 1 step back each time
print(my_string[17:0:-2]) # Take 2 steps back. The opposite of what
# happens in the slide above

# How to Reverse a String in Python
txt = "Hello World"[::-1]
print(txt)


