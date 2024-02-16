# PALINDROME : reads the same forward and backward
# create a function that checks if a given string is a palindrome or not

def is_palindrome(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str


original_str = input("Enter the String\n")
original_str = original_str.lower()
rev_str = is_palindrome(original_str)
print(rev_str)

if original_str == rev_str:
    print("Palindrome")
else:
    print("Not a Palindrome")
