
class FloatExpression:
    def __init__(self, value: float):
        self.value = value


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ExpressionPrinter:
    @classmethod
    def print(cls, buffer: list, expression):
        if isinstance(expression, FloatExpression):
            buffer.append(str(expression.value))
        elif isinstance(expression, AdditionExpression):
            buffer.append('(')
            cls.print(buffer, expression.left)
            buffer.append(' + ')
            cls.print(buffer, expression.right)
            buffer.append(')')
        else:
            buffer.append(str(expression))


# 1 + (2 + 3)
e1 = AdditionExpression(
    'abc',
    AdditionExpression(
        FloatExpression(2),
        FloatExpression(3)
    )
)
e1_str = []
ExpressionPrinter.print(e1_str, e1)
print(''.join(e1_str))
