from .effects import _blur, _rotate, _ascify, _caption1, _caption2
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
