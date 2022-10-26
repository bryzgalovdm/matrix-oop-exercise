# Libs
from itertools import chain

class Matrix:
    # TODO: Coeffs and matrix as properties?
    # TODO: make set also a possibility
    # TODO: make sure you can't set a value outside the matrix
    # TODO: make beautiful printing output (render floats without decimals as ints, truncate long floats)
    # TODO: wrap repeated code in a decorator?
    # TODO: add inversion
    # TODO: conceive tests and test
    def __init__(self, rows: int, columns: int, coeff) -> None:

        # Internal cuisine
        if isinstance(coeff, Matrix):
            self._coeff = list(chain(*coeff._matrix))
        else:
            self._coeff = coeff
        self._rows = rows
        self._columns = columns

        self._matrix = []
        # Initialise the matrix given a value
        if isinstance(self._coeff, (int, float)):
            for row in range(self._rows):
                self._matrix.append([self._coeff] * self._columns)
        # Initialize matrix given an array and dimensions (or another matrix given we transformed it to _coeff list)
        elif isinstance(self._coeff, (list, set, tuple)):
            # Check that the dimensions are correct
            if self._rows * self._columns != len(self._coeff):
                raise ValueError("Dimensions do not match")
            for row in range(self._rows):
                self._matrix.append(self._coeff[self._columns*row:self._columns*(row+1)])
        else:
            raise TypeError("Invalid input type of coefficients: should be int, float, list, set, tuple, or Matrix")


    # Immutable properties
    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    # Overload operators (= cannot be overloaded by default)
    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self._matrix == other._matrix
        else:
            return NotImplementedError(f"Comparison with Matrix is not implemented for this type: {type(other)}")

    def __add__(self, other):
        if isinstance(other, Matrix):
            # Check that the dimensions are the same
            if self._rows != other._rows or self._columns != other._columns:
                raise ValueError("Dimensions do not match")
            # Add the matrices
            result = []
            for row in range(self._rows):
                for column in range(self._columns):
                    result.append(self._matrix[row][column] + other._matrix[row][column])
            return Matrix(self._rows, self._columns, result)
        elif isinstance(other, (int, float)):
            # Add a scalar to the matrix
            return Matrix(self._rows, self._columns, [x + other for x in self._coeff])
        else:
            raise NotImplementedError(f"Addition with Matrix is not implemented for this type: {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Matrix):
            # Check that the dimensions are the same
            if self._rows != other._rows or self._columns != other._columns:
                raise ValueError("Dimensions do not match")
            # Subtract the matrices
            result = []
            for row in range(self._rows):
                for column in range(self._columns):
                    result.append(self._matrix[row][column] - other._matrix[row][column])
            return Matrix(self._rows, self._columns, result)
        elif isinstance(other, (int, float)):
            # Add a scalar to the matrix
            return Matrix(self._rows, self._columns, [x - other for x in self._coeff])
        else:
            raise NotImplementedError(f"Subtraction from Matrix is not implemented for this type: {type(other)}")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            # Check that the dimensions are the same
            if self._columns != other._rows:
                raise ValueError("Dimensions do not match")
            # Multiply the matrices
            result = []
            for row in range(self._rows):
                for column in range(other._columns):
                    result.append(sum([self._matrix[row][i] * other._matrix[i][column] for i in range(self._columns)]))
            return Matrix(self._rows, other._columns, result)
        elif isinstance(other, (int, float)):
            # Multiply the matrix by a scalar
            return Matrix(self._rows, self._columns, [x * other for x in self._coeff])
        else:
            raise NotImplementedError(f"Multiplication with Matrix is not implemented for this type: {type(other)}")

    def __rmul__(self, other): # To account for the case where the scalar is on the left
        if isinstance(other, (int, float)):
            return Matrix(self._rows, self._columns, [x * other for x in self._coeff])

    def __neg__(self):
        return Matrix(self._rows, self._columns, [-x for x in self._coeff])

    def __truediv__(self, other):
        return Matrix(self._rows, self._columns, [x / other for x in self._coeff])

    def __iadd__(self, other):
        if isinstance(other, Matrix):
            # Check that the dimensions are the same
            if self._rows != other._rows or self._columns != other._columns:
                raise ValueError("Dimensions do not match")
            # Add the matrices
            result = []
            for row in range(self._rows):
                for column in range(self._columns):
                    result.append(self._matrix[row][column] + other._matrix[row][column])
            return Matrix(self._rows, self._columns, result)
        elif isinstance(other, (int, float)):
            # Add a scalar to the matrix
            return Matrix(self._rows, self._columns, [x + other for x in self._coeff])
        else:
            raise NotImplementedError(f"Addition with Matrix is not implemented for this type: {type(other)}")

    def __isub__(self, other):
        if isinstance(other, Matrix):
            # Check that the dimensions are the same
            if self._rows != other._rows or self._columns != other._columns:
                raise ValueError("Dimensions do not match")
            # Subtract the matrices
            result = []
            for row in range(self._rows):
                for column in range(self._columns):
                    result.append(self._matrix[row][column] - other._matrix[row][column])
            return Matrix(self._rows, self._columns, result)
        elif isinstance(other, (int, float)):
            # Add a scalar to the matrix
            return Matrix(self._rows, self._columns, [x + other for x in self._coeff])
        else:
            raise NotImplementedError(f"Subtraction from Matrix is not implemented for this type: {type(other)}")


    def __imul__(self, other):
        if isinstance(other, Matrix):
            # Check that the dimensions are the same
            if self._columns != other._rows:
                raise ValueError("Dimensions do not match")
            # Multiply the matrices
            result = []
            for row in range(self._rows):
                for column in range(other._columns):
                    result.append(sum([self._matrix[row][i] * other._matrix[i][column] for i in range(self._columns)]))
            return Matrix(self._rows, other._columns, result)
        elif isinstance(other, (int, float)):
            # Multiply the matrix by a scalar
            return Matrix(self._rows, self._columns, [x * other for x in self._coeff])
        else:
            raise NotImplementedError(f"Multiplication with Matrix is not implemented for this type: {type(other)}")

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            return Matrix(self._rows, self._columns, [x * other for x in self._coeff])

    # Copy the matrix
    def copy(self):
        return Matrix(self._rows, self._columns, self._coeff)

    # Overload print (formatting methods)
    def __str__(self) -> str:
        output = ""
        for row in range(self._rows):
            for column in range(self._columns):
                output += str(self._matrix[row][column]) + " "
            output += "\n"
        return output

    def __repr__(self) -> str:
        return f"Matrix({self._rows}, {self._columns}, {self._coeff})"
