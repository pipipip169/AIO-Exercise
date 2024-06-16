# Levenshtein distance

def levenshtein_distance(source, target):
    """
    Returns the Levenshtein distance between two strings.

    Args:
        source: The source string.
        target: The target string.

    Returns:
        The Levenshtein distance between the two strings.
    """

    # Create a matrix to store the distances between prefixes.
    matrix = [[0 for _ in range(len(target) + 1)]
              for _ in range(len(source) + 1)]

    # Initialize the first row and column of the matrix.
    for i in range(len(source) + 1):
        matrix[i][0] = i
    for j in range(len(target) + 1):
        matrix[0][j] = j

    # Fill in the rest of the matrix.
    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,  # deletion
                matrix[i][j - 1] + 1,  # insertion
                matrix[i - 1][j - 1] + cost)  # substitution

    # Return the distance between the full strings.
    return matrix[len(source)][len(target)]


# testing
source = "kitten"
target = "sitting"
print(
    f"Levenshtein distance between '{source}' and '{target}' is {levenshtein_distance(source, target)}")

source = "yu"
target = "you"
print(
    f"Levenshtein distance between '{source}' and '{target}' is {levenshtein_distance(source, target)}")
