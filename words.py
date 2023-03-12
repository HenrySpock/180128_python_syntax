def print_upper_words(words, letters):
    """Function takes in two arrays: an array of words and an array of letters.
    Prints words from the first array that start with letters of the second 
    all capitalized."""

    for word in words:
        if word[0].lower() in letters:
            print(word.upper())

# words = ['Once', 'in', 'a', 'lifetime']
# letters = ['o', 'l']
# print_upper_words(words, letters)
# should print:
# "ONCE"
# "LIFETIME"

# words = ["I'm", 'not', 'your', 'buddy', 'Guy']
# letters = ['n', 'g']
# print_upper_words(words, letters)
# should print:
# "NOT"
# "GUY"