from dataclasses import dataclass
from itertools import pairwise


@dataclass
class Point:
    x: int
    y: int

    def __str__(self):
        return f'({self.x}; {self.y})'


class Polygon:

    @dataclass
    class LineSegment:
        start: Point
        end: Point

        @property
        def length(self):
            x1, x2 = self.start.x, self.end.x
            y1, y2 = self.start.y, self.end.y
            return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    def __init__(self,
                 point1: Point,
                 point2: Point,
                 point3: Point,
                 *points: Point):
        points = (point1, point2, point3) + points
        self.points: tuple[Point, ...] = points
        self.edges: tuple[Polygon.LineSegment, ...] = ()
        for start, end in pairwise(self.points + (self.points[0], )):
            self.edges += (Polygon.LineSegment(start, end), )

    @property
    def perimeter(self):
        return sum(edge.length for edge in self.edges)

# пример 1
p0 = Point(0, 0)
p1 = Point(1, 1)
p2 = Point(0, 2)
print(p0, p1, p2, sep=', ')

# агрегация
triangle = Polygon(p0, p1, p2)
print(triangle.perimeter, end='\n'*2)


# пример 2
# слабая композиция
square = Polygon(
    Point(0, 0),
    Point(0, 1),
    Point(1, 1),
    Point(1, 0)
)
print(square.perimeter, end='\n'*2)
