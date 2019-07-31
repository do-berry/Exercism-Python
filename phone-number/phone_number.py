import string

class Phone(object):
    def __init__(self, phone_number):
        phone_number = phone_number.translate(phone_number.maketrans('','',string.punctuation))
        try:
            self.number = ''.join([i for i in phone_number if i.isdigit()])
        except ValueError:
            print("Error!")
        if self.number[0] == '1':
            self.number = self.number[1:]
        self.area_code = self.number[:3]

    def pretty(self):
        return "({}) {}-{}".format(self.area_code, self.number[3:6], self.number[6:10])
