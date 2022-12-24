# imports
from PIL import Image
import os
from ImageEffects.constants import EMOJIS_DIR


class _emojioverlay:
    '''Static class'''
    EMOJI_ALPHA_VALUE = 100
    EMOJI_PADDING_VALUE = 5

    @classmethod
    def renderimage(cls, image: str, emoji: str = '') -> Image.Image:
        im = Image.open(image)
        im = im.convert('RGBA')

        emoji_im = Image.open(cls.getEmojiPath(emoji))
        emoji_im = emoji_im.crop((cls.EMOJI_PADDING_VALUE, cls.EMOJI_PADDING_VALUE, emoji_im.width -
                                 cls.EMOJI_PADDING_VALUE, emoji_im.height - cls.EMOJI_PADDING_VALUE))
        emoji_im = emoji_im.resize((im.width, im.height))
        emoji_im = emoji_im.convert('RGBA')
        emoji_im.putalpha(cls.EMOJI_ALPHA_VALUE)

        im = Image.alpha_composite(im, emoji_im)
        return im

    @classmethod
    def getEmojiPath(cls, emoji: str = '') -> str:
        '''returns the emoji image of type Image'''
        _emoji_file_name = cls.getEmojiName(emoji)
        _emoji_file_path = os.path.join(EMOJIS_DIR, _emoji_file_name)
        return _emoji_file_path

    @classmethod
    def getEmojiName(cls, emoji: str = '') -> str:
        '''returns the emoji file name.'''
        _emoji_code = "-".join(f"{ord(c):x}" for c in emoji).upper()
        emoji_name = f"{_emoji_code}.png"
        return emoji_name
