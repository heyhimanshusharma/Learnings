def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        # Count the approximate numbers of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The text file {filename} has about {num_words} words")

files = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for file in files:
    count_words(file)