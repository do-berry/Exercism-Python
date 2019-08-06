class Matrix(object):

    def __init__(self, matrix_string):
        self.rows = [tuple(map(int, line.split())) for line in tuple(matrix_string.splitlines())]
        self.columns = tuple(map(tuple, zip(*self.rows)))

    def row(self, index):
        return list(self.rows[index - 1])

    def column(self, index):
        return list(self.columns[index - 1])
