# how to handle file error exception
try:
    with open("TextData.txt" , 'r') as  file: # with is use to wrap the code
        content = file.read()
        print(content)
except FileNotFoundError as fnr:
    print(fnr)
finally:
    file.close()