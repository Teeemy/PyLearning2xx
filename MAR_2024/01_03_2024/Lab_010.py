# reading file with readlines
with open("td.txt", 'r')as file:
    lines = file.readlines()
#print(lines)
for line in lines:
    #print(line)
    print(line,end="")

# append in file handing
with open("td.txt",'a')as file:
    file.write("\nOnibon")