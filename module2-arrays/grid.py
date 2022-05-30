from arrays import Array
import random

"""
Code used for the 'Crear un array de dos dimensiones' class.

Grid type class
Methods:
    1. Initialize
    2. Get height
    3. Get width
    4. Access item
    5. String representation
"""


class Grid():
    """Represents a two-dimensional array."""

    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        # * Returns the number of rows.
        return len(self.data)

    def get_width(self):
        """Returns the number of columns."""
        return len(self.data[0])

    def __getitem__(self, index):
        """Supports two-dimensional indexing with [row][column]."""
        return self.data[index]

    def testslots(self):
        """__testslots__
            Replaces the array values with random numbers
        """
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                self[i][j] = random.randint(0, self.get_width())

    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "

            result += "\n"

        return str(result)


'''
Code used in the shell to instance a grid

matrix = Grid(3, 3)
print(matrix)
for row in range(matrix.get_height()):
    for column in range(matrix.get_width()):
        matrix[row][column] = row * column

print(matrix)
matrix.get_height()
matrix.get_width()
matrix.__getitem__()
matrix.__getitem__(1)
matrix.__getitem__(2)[0]
matrix.__str__()
'''


# *  Challenge
class Cube():
    def __init__(self, rows, columns, depth, fill_value=None):
        """ Create tri-dimensional Arrays """
        self.cube = [Array(columns, Array(depth)) for i in range(rows)]

    def get_height(self):
        # * Returns the number of rows.
        return len(self.cube)

    def get_width(self):
        """Returns the number of columns."""
        return len(self.cube[0])

    def get_depth(self):
        """Returns the number of rows and columns."""
        return len(self.cube[0][0])

    def __getitem__(self, index):
        return self.cube[index]

    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""

        for depth in range(self.get_depth()):
            result += f'Depth index: [{depth}] \n'
            for row in range(self.get_height()):
                for col in range(self.get_width()):
                    result += str(self.cube[row][col][depth]) + " "

            result += "\n" * 2

        return str(result)


if __name__ == '__main__':
    matrix = Grid(3, 3)
    matrix.testslots()
    print(f'Matrix \n{matrix}')

    cube = Cube(3, 4, 3)

    for row in range(cube.get_height()):
        for column in range(cube.get_width()):
            for depth in range(cube.get_depth()):
                cube[row][column][depth] = f'[Row {row}, column {column}, depth {depth}]\n'

    print(f'\tCube\n{cube}')
