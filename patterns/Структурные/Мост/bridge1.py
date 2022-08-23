# Vector, Raster
# circle, square, triangle,

# подобная реализация ведёт к взрывному увеличению количества классов
class VectorCircle:
    def render(self):
        return f'vector circle {self.name}'

class VectorSquare:
    def render(self):
        return f'vector square {self.name}'

# class VectorTriangle ...
# class RasterCircle ...
# class RasterSquare ...
# class RasterTriangle ...


# вместо этого создаём классы интерфейсов, экземпляры которых будем присваивать в атрибуты объектов circle, square, triangle, ...
class Vector:
    """Interface to render images with lines."""
    @staticmethod
    def render(image):
        return f'vector {image}'

class Raster:
    """Interface to render images with pixels."""
    @staticmethod
    def render(image):
        return f'raster {image}'


class Shape:
    """Base class for all objects that can be rendered."""
    def __init__(self, renderer):
        # передаём объект экземпляра интерфейса
        self._interface = renderer

    def draw(self):
        # используем полиморфный метод нужного интерфейса
        return self._interface.render(self.__class__.__name__)

class Circle(Shape):
    pass

class Square(Shape):
    pass

class Triangle(Shape):
    pass


render_vector = Vector()
render_raster = Raster()

sq1 = Square(render_vector)
sq2 = Square(render_raster)
cr1 = Circle(render_vector)
tr1 = Triangle(render_raster)

for shape in (sq1, sq2, cr1, tr1):
    print(shape.draw())

sq2._interface = render_vector
print(sq2.draw())
