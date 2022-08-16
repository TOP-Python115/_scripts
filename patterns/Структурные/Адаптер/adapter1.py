class Square:
    """Реализация, не подлежащая правкам"""
    def __init__(self, side: int):
        self.side = side


def calc_area(rectangle):
    """Интерфейс, не подлежащий правкам"""
    return rectangle.width * rectangle.height


class SquareToRectangleAdapter:
    """Позволяет использовать квадрат на месте прямоугольника"""
    def __init__(self, square: Square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side


squares = [
    Square(10),
    Square(6),
    Square(13)
]
squares_adapted = [SquareToRectangleAdapter(sq) for sq in squares]
for sq_ad in squares_adapted:
    print(calc_area(sq_ad))
print()

squares[1].side = 17
for sq_ad in squares_adapted:
    print(calc_area(sq_ad))
print()
