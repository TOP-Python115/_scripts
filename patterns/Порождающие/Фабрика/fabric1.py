"""Фабричный метод"""

from enum import Enum
from math import cos, sin

class CoordinateSystems(Enum):
    CARTESIAN = 0
    POLAR = 1

class Point:
    """Точка на плоскости."""
    # нарушение OCP
    # def __init__(self, 
                 # a: float, 
                 # b: float, 
                 # system=CoordinateSystems.CARTESIAN):
        # if system is CoordinateSystems.CARTESIAN:
            # self.x = a
            # self.y = b
        # elif CoordinateSystems.POLAR:
            # self.x = a * cos(b)
            # self.y = a * sin(b)
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    @staticmethod
    def new_cartesian_point(x: float, y: float):
        """Создание точки с помощью декартовых координат."""
        return Point(x, y)
    
    @staticmethod
    def new_poar_point(rho: float, theta: float):
        """Создание точки с помощью полярных координат."""
        return Point(rho*cos(theta), rho*sin(theta))
    
    def __repr__(self):
        return f"<Point: x={self.x}, y={self.y}>"


p1 = Point.new_cartesian_point(2, 3)
p2 = Point.new_poar_point(5, 0.9)
print(p1, p2, sep='\n')
