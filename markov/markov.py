"""Generate sentences from text file."""
from random import randint


def generate_dictionary(path):
    """Generate a dict from a given file path."""
    # read in text file to list
    file = open(path, "r", encoding="utf-8")
    cont = file.read()
    text = cont.split()
    file.close()
    # create and fill next word dictionary
    dict = {word: [] for word in text}
    for i in range(0, len(text)-1):
        dict[text[i]].append(text[i+1])
    return dict


def generate_sentence(word, dict, n):
    """Generate a sentence given a start and a dict."""
    sentence = [word]
    current = word
    for i in range(1, n):
        sample = dict[current]
        current = sample[randint(0, len(sample)-1)]
        sentence.append(current)
    return " ".join(sentence)


def advanced_dict(path, string=None):
    """Generate a dict from a given file path or string."""
    if string:
        text = string.split()
    else:
        # read in text file to list
        file = open(path, "r", encoding="utf-8")
        cont = file.read()
        text = cont.split()
        file.close()
    # create and fill next 2 words dictionary
    dict = {(text[i], text[i + 1]): [] for i in range(0, len(text) - 1)}
    for i in range(0, len(text) - 2):
        dict[(text[i], text[i + 1])].append(text[i + 2])
    return dict


def advanced_sentence(words, dict, n):
    """Generate a sentence given 2 starting words and a dict."""
    sentence = words.split()
    for i in range(1, n):
        sample = dict[(sentence[-2], sentence[-1])]
        sentence.append(sample[randint(0, len(sample) - 1)])
    return " ".join(sentence)


def conversation(dict, length, n):
    """Generate replies to repeated 2 word user input text."""
    for i in range(0, length):
        words = input()
        try:
            reply = advanced_sentence(words, dict, n)
            print(reply)
        except KeyError:
            print("Sorry I don't understand.")
