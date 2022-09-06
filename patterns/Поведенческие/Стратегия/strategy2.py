from abc import ABC, abstractmethod


class ImageDecoder(ABC):
    @staticmethod
    @abstractmethod
    def decode(path_to_image: str) -> str:
        pass

class PNGDecoder(ImageDecoder):
    @staticmethod
    def decode(path_to_image: str) -> str:
        return 'PNG Image'

class JPEGDecoder(ImageDecoder):
    @staticmethod
    def decode(path_to_image: str) -> str:
        return 'JPG Image'

class TIFFDecoder(ImageDecoder):
    @staticmethod
    def decode(path_to_image: str) -> str:
        return 'TIFF Image'


class Image:
    @classmethod
    def open(cls, image_path: str) -> 'Image':
        ext = image_path.rsplit('.', 1)[-1].lower()
        if ext in ('png', ):
            decoder = PNGDecoder
        elif ext in ('jpg', 'jpeg'):
            decoder = JPEGDecoder
        elif ext in ('tiff', ):
            decoder = TIFFDecoder
        else:
            raise ValueError("couldn't decode this image format")
        byterange = decoder.decode(image_path)
        return cls(byterange, image_path)

    def __init__(self, byterange, filename):
        self._filename = filename
        self._byterange = byterange

    def __str__(self):
        byterange = " ".join(hex(ord(char))[2:] for char in self._byterange)
        return f'<Image: path={self._filename},' \
               f' bytes={byterange[:9]}...>'


pic1 = 'figure.png'
pic2 = 'wallpaper.jpg'
pic3 = 'sprite.tiff'

print(Image.open(pic1))
print(Image.open(pic2))
print(Image.open(pic3))
