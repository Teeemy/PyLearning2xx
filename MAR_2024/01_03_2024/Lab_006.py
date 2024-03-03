# File Handling:How to read a Text, and Write it into python code
# to read a file, you have to first know the FUNCTION to use

# first  is OPEN("file_name","mode")

# second is to know the MODE
# e.g
# 'r' for reading (default)
# 'w' for writing (creates a new file or turncates existing one)
# 'a' for appending
# 'b' for binary mode e.g exe file or vlc.exe
# '+' for updating(reading and writing)

# Read and Write content
#Read a file
#Reading Entire content = file_object.read)()
#Line = file_object.readline() for single line
#lines = file_object.readlines() for all lines in a list

#the last is close the file

# an example of how to read a file

file = open("TextData.txt",'r')
content = file.read()
print(content)
file.close()
