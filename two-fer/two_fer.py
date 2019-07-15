import sys

def two_fer(name=None):
    txt = "One for {}, one for me."
    if name == None:
        return "One for you, one for me."
    else:
        return txt.format(name)