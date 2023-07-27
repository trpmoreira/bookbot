book = "books/frankenstein.txt"

with open(book) as f:
    file_contents = f.read()


def countWords(text):
    words = text.split()
    return len(words)


def countChars(text):
    result = {}
    chars = list(text.lower())

    for char in chars:
        if char.isalpha() == True:
            if char not in result:
                result[char] = 1
            else:
                result[char] += 1
    new_results = list(result.items())
# want to sort by the second item in the tuple
    new_results.sort(key=lambda x: x[1], reverse=True)
    return new_results


def report(text):
    words = countWords(text)
    char = countChars(text)

    print(f"--- Begin report of {book} ---")
    print(f"The document contains {words} words")
    print("")
    for item in char:
        print(f"The '{item[0]}' character was found {item[1]} times")
    print(f"--- End report ---")


report(file_contents)
