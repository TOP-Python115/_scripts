from pprint import pprint

class MatrixError(Exception):
    def __init__(self, message, i=0, j=1, *args):
        text = f"an error occured: {message}"
        self.i = i
        self.j = j
        super().__init__(text)


class SetElementError(MatrixError):
    def __init__(self, message, i=0, j=1, *args):
        text = f"an error with the element {i=} {j=} occured: {message}"
        super().__init__(text, i, j, *args)

err = MatrixError('error message')
s_err = SetElementError('error message', 10 ,0)
