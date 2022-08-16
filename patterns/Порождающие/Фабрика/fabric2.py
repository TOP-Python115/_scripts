"""Фабрика"""

from math import cos, sin

class Point:
    """Точка на плоскости."""
    class PointFactory:
        def new_cartesian_point(self, x: float, y: float):
            """Создание точки с помощью декартовых координат."""
            return Point(x, y)
        
        def new_poar_point(self, rho: float, theta: float):
            """Создание точки с помощью полярных координат."""
            return Point(rho*cos(theta), rho*sin(theta))
    
    factory = PointFactory()
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"<Point: x={self.x}, y={self.y}>"


p1 = Point.factory.new_cartesian_point(2, 3)
p2 = Point.factory.new_poar_point(5, 0.9)
print(p1, p2, sep='\n')
