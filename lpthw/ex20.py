# EVEN MORE PRACTICE
def break_words(stuff):
    """This function will break up words for us."""
    # THESE WORDS IN TRIPLE QUOTES INSIDE EVERY FUNCTION
    # ARE CALLED DOCUMENTATION COMMENTS
    # THESE SHOULD GIVE A DESCRIPTION OF THE FUNCTION
    words = stuff.split(' ')
    return words
    # THE FUNCTION IS TAKING STRING AS AN ARGUMENT
    # LINE 7: SPLITS THE STRING INTO WORDS AND SAVES
    # THEM IN A LIST NAMED 'words'
    # LINE 8: RETURNS THE LIST

def sort_words(words):
    """Sorts the words"""
    return sorted(words)
    # SORTED FUNCTION DOES THE SORTING

def print_first_word(words):
    """Prints the first word after popping t off"""
    word = words.pop(0)
    # POP FUNCTION IS USED TO POP OUT A WORD FROM A STRING
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words and then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
