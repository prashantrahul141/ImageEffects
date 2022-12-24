# imports
import os
from PIL import Image, ImageDraw, ImageFont
from ImageEffects.constants import FONTS_DIR


class _caption1:
    '''Static class'''
    TEXT_COLOR = (255, 255, 255)
    FONT_SIZE_RATIO = 9/100  # 10%
    LINE_LENGTH = int((FONT_SIZE_RATIO * 100) * 1.5)

    @classmethod
    def renderimage(cls, image: str, text: str = 'text here') -> Image:
        if len(text) == 0:
            text = 'text here'

        im = Image.open(image)
        IMPACT_FONT = ImageFont.truetype(os.path.join(FONTS_DIR, 'impact.ttf'), int(cls.FONT_SIZE_RATIO * im.width))
        editable_im = ImageDraw.Draw(im)
        editable_im.text((0, 0), cls.format_text(text), cls.TEXT_COLOR, font=IMPACT_FONT)

        return im

    @classmethod
    def format_text(cls, text: str) -> str:
        '''takes the input string and formats if its longer than the threshold length'''
        if len(text) > cls.LINE_LENGTH:

            _text = ''
            _temp_length = 0
            _temp_str = ''

            for i in text.split(' '):
                _temp_length += len(i)
                _temp_str += i + ' '

                if _temp_length > cls.LINE_LENGTH:
                    _text += _temp_str + '\n'
                    _temp_str = ''
                    _temp_length = 0

            return _text

        return text
