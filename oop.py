# Libs
from itertools import chain

class Matrix:
    # TODO: conceive tests and test
    # TODO: make adaptable printing output (squeeze it horizontally if all ints, for example; and adapt for large values by converting them to scientific notation)
    def __init__(self, rows: int, columns: int, coefficients) -> None:

        # Internal cuisine
        if isinstance(coefficients, Matrix):
            self._coefficients = list(chain(*coefficients._matrix))
        elif isinstance(coefficients, (int, float)):
            self._coefficients = [coefficients] * rows * columns
        else:
            self._coefficients = coefficients
        self._rows = rows
        self._columns = columns
        self._matrix = self._initialize_matrix(self._rows, self._columns,
                                               self._coefficients)

    def _initialize_matrix(self, rows, columns, coefficients):
        matrix = []
        # Initialize matrix given an array and dimensions (or another matrix given we transformed it to _coefficients list)
        if isinstance(coefficients, (list, tuple)):
            # Check that the dimensions are correct
            if rows * columns != len(coefficients):
                raise ValueError("Dimensions do not match")
            for row in range(rows):
                matrix.append(coefficients[columns*row:columns*(row+1)])
        else:
            raise TypeError(f"Invalid input type of coefficients - {type(coefficients)}"
                            ": should be int, float, list, tuple, or Matrix")
        return matrix

    # Immutable properties
    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @property
    def coefficients(self):
        return self._coefficients

    @coefficients.setter
    def coefficients(self, value):
        self._coefficients = value
        self._matrix = self._initialize_matrix(self._rows, self._columns,
                                               self._coefficients)

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
            return Matrix(self._rows, self._columns, [x + other for x in self._coefficients])
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
            return Matrix(self._rows, self._columns, [x - other for x in self._coefficients])
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
            return Matrix(self._rows, self._columns, [x * other for x in self._coefficients])
        else:
            raise NotImplementedError(f"Multiplication with Matrix is not implemented for this type: {type(other)}")

    def __rmul__(self, other): # To account for the case where the scalar is on the left
        if isinstance(other, (int, float)):
            return Matrix(self._rows, self._columns, [x * other for x in self._coefficients])

    def __neg__(self):
        return Matrix(self._rows, self._columns, [-x for x in self._coefficients])

    def __truediv__(self, other):
        return Matrix(self._rows, self._columns, [x / other for x in self._coefficients])

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
            return Matrix(self._rows, self._columns, [x + other for x in self._coefficients])
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
            return Matrix(self._rows, self._columns, [x + other for x in self._coefficients])
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
            return Matrix(self._rows, self._columns, [x * other for x in self._coefficients])
        else:
            raise NotImplementedError(f"Multiplication with Matrix is not implemented for this type: {type(other)}")

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            return Matrix(self._rows, self._columns, [x * other for x in self._coefficients])

    # Copy the matrix
    def copy(self):
        return Matrix(self._rows, self._columns, self._coefficients)

    # Overload print (formatting methods)
    def __str__(self) -> str:
        MAX_SPACE = 7
        output = ""
        for row in range(self._rows):
            for column in range(self._columns):
                numberFormat = str(round(self._matrix[row][column], 2))
                if len(numberFormat) < MAX_SPACE - 1:
                    output += numberFormat + (MAX_SPACE - len(numberFormat)) * " "
                else:
                    output += numberFormat[:MAX_SPACE-3] + ".. "
            output += "\n"
        return output

    def __repr__(self) -> str:
        return f"Matrix({self._rows}, {self._columns}, {self._coefficients})"
