# word counts in the given txt file

def count_words(file_path):
    """Returns a dictionary of word counts in the given text file.

    Args:
        file_path: The path to the text file.

    Returns:
        A dictionary of word counts.
    """
    # Initialize an empty dictionary to store word counts.
    word_counts = {}

    # Open the file at the given path for reading.
    with open(file_path, 'r') as file:
        for line in file:
            # Remove periods, commas, and hyphens from the line.
            # Convert the line to lowercase.
            # Split the line into words.
            words = line.replace('.', '').replace(
                ',', '').replace('-', ' ').lower().split()
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    return word_counts

# testing


file_path = r"C:\Users\MSI GS66\Downloads\P1_data.txt"
result = count_words(file_path)
print(result)
