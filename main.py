with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def countWords(text):
    words = text.split()
    print(f"This book has {len(words)} words in it.")


def countChars(text):
    result = {}
    chars = list(text.lower())

    for char in chars:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    print(result)


countWords(file_contents)
countChars(file_contents)
