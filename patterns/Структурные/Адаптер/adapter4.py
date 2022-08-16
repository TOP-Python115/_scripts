from abc import ABC, abstractmethod

class PNGInterface(ABC):
    @abstractmethod
    def draw(self):
        pass

class PNGImage(PNGInterface):
    def __init__(self, image):
        self.image = image
        self.format = 'raster'

    @staticmethod
    def get_image():
        return 'png'

    def draw(self):
        return 'drawing ' + self.get_image()


class SVGImage:
    def __init__(self, image):
        self.image = image
        self.format = 'vector'

    @staticmethod
    def get_image():
        return 'svg'


class SVGAdapter:
    def __init__(self, vector_image: SVGImage):
        self.image = vector_image

    @staticmethod
    def get_image():
        return 'svg'

    def rasterize(self):
        return 'rasterized ' + self.get_image()

    def draw(self):
        return 'drawing ' + self.rasterize()


print('\nObject adapter:')
png_image = PNGImage('some image')
print(png_image.draw())

svg_image = SVGImage('some vector')
svg_adapted = SVGAdapter(svg_image)
print(svg_adapted.draw())



class ConvertingNotVector(Exception):
    pass

class ImageAdapter(PNGImage, SVGImage):
    def __init__(self, image: PNGImage | SVGImage):
        self.image = image

    def rasterize(self):
        if self.image.format == 'vector':
            return 'rasterized ' + self.image.get_image()
        else:
            raise ConvertingNotVector

    def draw(self):
        try:
            return 'drawing ' + self.rasterize()
        except ConvertingNotVector:
            return self.image.draw()


print('\nClass adapter:')
images = [
    PNGImage('1'),
    PNGImage('2'),
    SVGImage('3'),
    PNGImage('4'),
    SVGImage('5')
]
for img in images:
    print(ImageAdapter(img).draw())
print()
