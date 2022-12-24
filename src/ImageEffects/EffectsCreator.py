from .effects import _blur, _rotate, _ascify, _caption1, _caption2, _crop, _resize, _cropcircle, _pixelate, _saturate
from .effects import _deepfry
from PIL import Image


class EffectsCreator:
    def __init__(self) -> None:
        pass

    def blur(self, image: str, radius: int = 1) -> Image:
        '''blurs the image using box blur for performance'''
        return _blur._blur.renderimage(image, radius)

    def rotate(self, image: str, rotation_angle: int = 90) -> Image:
        '''rotates the image according to the radius given'''
        return _rotate._rotate.renderimage(image, rotation_angle)

    def asicfy(self, text: str = 'ascify') -> str:
        '''makes ascii art from given text'''
        return _ascify._ascify.renderimage(text)

    def caption1(self, image: str, text: str = 'text here') -> Image:
        '''adds given text to the image on the top side'''
        return _caption1._caption1.renderimage(image, text)

    def caption2(self, image: str, text: str = 'text here') -> Image:
        '''adds given text to the image on the bottom side'''
        return _caption2._caption2.renderimage(image, text)

    def crop(self, image: str) -> Image:
        '''crops image automactically'''
        return _crop._crop.renderimage(image)

    def cropcircle(self, image: str) -> Image:
        '''crops image in circle'''
        return _cropcircle._cropcircle.renderimage(image)

    def resize(self, image: str, width: int = None, height: int = None) -> Image:
        '''resize image according to given width and height'''
        return _resize._resize.renderimage(image, width, height)

    def pixelate(self, image: str, scale: int = 0) -> Image:
        '''adds pixelate effect'''
        return _pixelate._pixelate.renderimage(image, scale)

    def saturate(self, image: str, scale: int = 0) -> Image:
        '''changes saturation of image'''
        return _saturate._saturate.renderimage(image, scale)

    def deepfry(self, image: str) -> Image:
        '''makes deepfry meme from image'''
        return _deepfry._deepfry.renderimage(image)
