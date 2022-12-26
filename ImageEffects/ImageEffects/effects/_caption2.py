# imports
import os
from PIL import Image, ImageDraw, ImageFont
from ImageEffects.constants import FONTS_DIR


class _caption2:
    '''Static class'''
    TEXT_COLOR = (255, 255, 255)
    FONT_SIZE_RATIO = 10/100  # 10%
    LINE_LENGTH = int(FONT_SIZE_RATIO * 100)
    FONT_HEIGHT = FONT_SIZE_RATIO * 100 * 4

    @classmethod
    def renderimage(cls, image: str, text: str = 'text here') -> Image.Image:
        if len(text) == 0:
            text = 'text here'

        im = Image.open(image)
        IMPACT_FONT = ImageFont.truetype(os.path.join(FONTS_DIR, 'impact.ttf'), int(cls.FONT_SIZE_RATIO * im.width))
        editable_im = ImageDraw.Draw(im)
        X_DISTANCE = im.width - (85/100 * im.width)
        Y_DISTANCE = cls.get_Y_dist(text)
        editable_im.text((X_DISTANCE, Y_DISTANCE), cls.format_text(text), cls.TEXT_COLOR, font=IMPACT_FONT)

        return im

    @classmethod
    def get_Y_dist(cls, text: str) -> float:
        '''get Y distance according to font height and number of lines'''
        _len = 10
        _temp_length = 0
        for i in text.split(' '):
            _temp_length += len(i)
            if _temp_length > cls.LINE_LENGTH:
                _temp_length = 0
                _len -= 1

        return _len * cls.FONT_HEIGHT

    @classmethod
    def format_text(cls, text: str) -> str:
        '''takes the input string and formats if its longer than the threshold length'''
        if len(text) > cls.LINE_LENGTH:

            _text = ''
            _temp_length = 0
            _temp_str = ''
            _last_index = 0

            for _index, _each_string in enumerate(text.split(' ')):
                _temp_length += len(_each_string)
                _temp_str += ' ' + _each_string
                _last_index = _index

                if _temp_length > cls.LINE_LENGTH:
                    _text += _temp_str + '\n'
                    _temp_str = ''
                    _temp_length = 0

            # adding left over strings
            for _each_string in text.split(' ')[_last_index - 1:]:
                _text += ' ' + _each_string

            return _text

        return text