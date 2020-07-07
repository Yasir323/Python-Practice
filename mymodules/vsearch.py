def search4words(phrase:str, letters:str='aeiou') -> set:
    """Return a set of 'letters' found in the 'phrase'."""
    return set(letters).intersection(set(phrase))
