from pprint import pprint

class Shape:
    """Base class defining coordinates and size for shapes."""
    def __init__(self: "Shape object", 
                 x: int, 
                 y: int, 
                 w: float, 
                 h: float) -> None:
        """Defines two coordinates and two dimensions of shape's size."""
        self.x = x
        self.y = y
        self.width = w
        self.height = h
    
    def move(self, dx: int, 
                   dy: int) -> None:
        """Changes shape's coordinates."""
        self.x += dx
        self.y += dy

class MixinResize:
    """Mixin class adding resize method to two-dim shapes."""
    def resize(self, dw: float, 
                     dh: float) -> None:
        """Changes shape's size with two dimensions."""
        self.width += dw
        self.height += dh

class MixinRightResize:
    """Mixin class adding resize method to one-dim shapes."""
    def resize(self, da: float) -> None:
        """Changes shape's size with one dimension."""
        self.width += da
        self.height += da

class Rectangle(Shape, MixinResize):
    """Describes rectangles."""
    pass

class Square(Shape, MixinRightResize):
    """Describes squares."""
    def __init__(self, x: int, 
                       y: int, 
                       a: float) -> None:
        super().__init__(x, y, a, a)

class Diamond(Shape, MixinRightResize):
    """Describes diamonds."""
    def __init__(self, x: int, 
                       y: int, 
                       a: float, 
                       alpha: float) -> None:
        super().__init__(x, y, a, a)
        self.alpha = alpha


t = tuple(globals().values())
for obj in t:
    if callable(obj):
        print(obj.__name__)
        print(obj.__doc__, end='\n\n')
        for attr_name in dir(obj):
            attr = getattr(obj, attr_name)
            if callable(attr) and not attr_name.startswith('__'):
                print(f'\t{attr.__name__}')
                print(f'\t{attr.__annotations__}')
                print(f'\t{attr.__doc__}', end='\n\n\n')
