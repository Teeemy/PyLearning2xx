# reverse a string using function

def reverse_string(str):
    rev_str = " "
    for c in str:
        rev_str = c + rev_str
    return rev_str


name = reverse_string("Olawale")
print(name)
