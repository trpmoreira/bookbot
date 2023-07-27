with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def countWords(text):
    words = text.split()
    print(len(words))

countWords(file_contents)