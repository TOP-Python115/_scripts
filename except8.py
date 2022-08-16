from pprint import pprint

class MatrixError(Exception):
    pass

err = MatrixError('error message', 0, 2)

# raise MatrixError

# raise MatrixError()

raise MatrixError('error message', 0, 2)
