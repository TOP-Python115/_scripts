from typing import Callable

_methods = {}


def visitor(arg_type: 'Expression'):
    """Параметризует декоратор."""
    def decorator(func_obj: Callable):
        """Параметризованный декоратор."""
        class_name = func_obj.__qualname__.rsplit('.')[0]
        _methods[(class_name, arg_type)] = func_obj

        def _wrapper(instance_obj, obj_to_process: 'Expression'):
            """Производит вызов нужного метода для обработки объекта соответствующего класса."""
            key = (
                instance_obj.__class__.__qualname__,
                obj_to_process.__class__
            )
            method = _methods[key]
            return method(instance_obj, obj_to_process)
        return _wrapper
    return decorator


class Expression:
    pass

class FloatExpression(Expression):
    def __init__(self, value: float):
        self.value = value

class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    def __str__(self):
        return ''.join(self.buffer)

    @visitor(FloatExpression)
    def visit(self, fe: FloatExpression):
        self.buffer += [str(fe.value)]

    @visitor(AdditionExpression)
    def visit(self, ae: AdditionExpression):
        self.buffer += ['(']
        self.visit(ae.left)
        self.buffer += [' + ']
        self.visit(ae.right)
        self.buffer += [')']


e1 = AdditionExpression(
    FloatExpression(1),
    AdditionExpression(
        FloatExpression(2),
        FloatExpression(3)
    )
)
printer = ExpressionPrinter()
printer.visit(e1)
print(printer)
