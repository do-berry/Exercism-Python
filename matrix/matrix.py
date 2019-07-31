import numpy as np

class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = np.matrix(matrix_string.replace("\n",";"))

    def row(self, index):
        return [row[index - 1] for row in self.matrix]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
