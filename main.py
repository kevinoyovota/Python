# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    try:
        stream = open(filename, mode = "rt")
        words = stream.read()
        stream.close()
        return words

    except FileNotFoundError:
        print("The file was not found. Try again.")
    
    return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    words = ""
    for letter in text:
        if letter.isalpha() or letter == " ":
            words += letter

    word_count = {}
    word_list = text.split()

    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

print(count_words())
