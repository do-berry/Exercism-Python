import string
import random

class Robot(object):

    def __init__(self):
        self.name = self.generateName()

    def generateName(self):
        generatedName = ""
        for i in range(2):
            generatedName += random.choice(string.ascii_uppercase)
        generatedName += str(random.randint(100,999))
        return generatedName

    def reset(self):
        generatedName = self.name
        while self.name == generatedName:
            self.name = self.generateName()
