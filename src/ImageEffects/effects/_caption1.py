# imports
import os
from PIL import Image, ImageDraw, ImageFont
from ImageEffects.constants import FONTS_DIR


class _caption1:
    '''Static class'''
    TEXT_COLOR = (255, 255, 255)
    FONT_SIZE_RATIO = 10/100  # 10%

    @classmethod
    def renderimage(cls, image: str, text: str = 'text here') -> Image:
        im = Image.open(image)
        IMPACT_FONT = ImageFont.truetype(os.path.join(FONTS_DIR, 'impact.ttf'), int(cls.FONT_SIZE_RATIO * im.width))
        editable_im = ImageDraw.Draw(im)
        editable_im.text((0, 0), text, cls.format_text(cls.TEXT_COLOR), font=IMPACT_FONT)
        return im

    @classmethod
    def format_text(text: str) -> str:
        _text = text

        return _text
