import string

def is_pangram(sentence=""):
    if not sentence:
        return False
    alphabet = list(string.ascii_lowercase)
    for char in sentence:
        if char.lower().isalpha() and char.lower() in alphabet:
                alphabet.remove(char.lower())
    if alphabet:
        return False
    return True