def count_vowels_consonants(text):
    """Counts the number of vowels and consonants in a string.

    Args:
        text: The string to count vowels and consonants in.

    Returns:
        A dictionary with two keys: 'vowels' and 'consonants', and the corresponding counts.
    """

    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowel_count = 0
    consonant_count = 0

    for char in text.lower():
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return {"vowels": vowel_count, "consonants": consonant_count}

# Example usage
text = "This is a string to count vowels and consonants."
result = count_vowels_consonants(text)
print(f"Vowels: {result['vowels']}")
print(f"Consonants: {result['consonants']}")