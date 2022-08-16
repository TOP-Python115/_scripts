class Point:
    """Единственно доступная реализация"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Point: x={self.x}, y={self.y}>"

    def __str__(self):
        return f"({self.x}; {self.y})"

def draw_point(point: Point):
    """Интерфейс для вывода"""
    print('.', end='')


class Line:
    """Отрезок задаётся двумя точками"""
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"<Line: start={self.start!s}, end={self.end!s}>"

class Rectangle(list):
    """Прямоугольник задаётся четырьмя отрезками"""
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.append(Line(Point(x, y), Point(x+width, y)))
        self.append(Line(Point(x+width, y), Point(x+width, y+height)))
        self.append(Line(Point(x, y+height), Point(x+width, y+height)))
        self.append(Line(Point(x, y), Point(x, y+height)))


class LineAdapter(list):
    """Генерирует необходимое количество точек для отрезка"""
    def __init__(self, line: Line):
        super().__init__()
        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        bottom = min(line.start.y, line.end.y)
        top = max(line.start.y, line.end.y)
        print(f'\nГенерируются точки для {line}')
        if left == right:
            for y in range(bottom, top+1):
                self.append(Point(left, y))
        elif bottom == top:
            for x in range(left, right+1):
                self.append(Point(x, top))



rectangles = [
    Rectangle(0, 0, 10, 10),
    Rectangle(3, 3, 5, 2)
]
# for rc in rectangles:
#     print(*rc, sep='\n')
#     print()
for rc in rectangles:
    for line in rc:
        for point in LineAdapter(line):
            draw_point(point)
print()

for rc in rectangles:
    for line in rc:
        for point in LineAdapter(line):
            draw_point(point)
print()
