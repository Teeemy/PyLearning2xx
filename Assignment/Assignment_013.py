from collections import Counter

def are_anagrams(str1, str2):
  """
  Checks if two strings are anagrams.

  Args:
    str1: The first string.
    str2: The second string.

  Returns:
    True if the strings are anagrams, False otherwise.
  """
  # Convert strings to lowercase and remove spaces
  str1 = str1.lower().replace(" ", "")
  str2 = str2.lower().replace(" ", "")

  # Count letter occurrences
  counter1 = Counter(str1)
  counter2 = Counter(str2)

  # Compare counts
  return counter1 == counter2

# Example usage
string1 = "silent"
string2 = "listen"


if are_anagrams(string1, string2):
  print(f"{string1} and {string2} are anagrams.")
else:
  print(f"{string1} and {string2} are not anagrams.")