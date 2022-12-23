from .effects import _blur, _rotate, _ascify
from PIL import Image


class EffectsCreator:
    def __init__(self) -> None:
        pass

    def blur(self, image: str, radius: int = 1) -> Image:
        return _blur._blur.renderimage(image, radius)

    def rotate(self, image: str, radius: int = 90) -> Image:
        return _rotate._rotate.renderimage(image, radius)

    def asicfy(self, text: str = 'ascify') -> str:
        return _ascify._ascify.renderimage(text)