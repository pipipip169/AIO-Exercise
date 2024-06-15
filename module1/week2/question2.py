# alphabet counting

def count_alphabets(text):
    """
    Returns a dictionary of alphabet counts in the given string.

    Args:
        text: The string to count the alphabets in.

    Returns:
        A dictionary of alphabet counts.
    """
    # Initialize an empty dictionary to store alphabet counts.
    alphabet_counts = {}

    for char in text:
        if char.isalpha():
            if char in alphabet_counts:
                alphabet_counts[char] += 1
            else:
                alphabet_counts[char] = 1

    return alphabet_counts

#testing

text = "Hello world!"
result = count_alphabets(text)
print(result)