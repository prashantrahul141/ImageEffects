# imports
from PIL import Image


class _rotate:
    '''Static class'''
    @staticmethod
    def renderimage(image: str, radius: int = 1) -> Image:
        im = Image.open(image).rotate(radius)
        return im
