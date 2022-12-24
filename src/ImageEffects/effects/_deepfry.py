# imports
from PIL import Image, ImageEnhance


class _deepfry:
    '''Static class'''
    LOWER_RESOLUTION = (512, 512)
    SATURATION_ENHANCE_SCALE = 2.0
    RED_BAND_INCREASE_RATIO = 10.0
    BLUE_BAND_INCREASE_RATIO = 0.8

    @classmethod
    def renderimage(cls, image: str) -> Image.Image:
        im = Image.open(image)

        # lowering resolution
        imSmall = im.resize(cls.LOWER_RESOLUTION, resample=Image.Resampling.BILINEAR)
        im = imSmall.resize(im.size, Image.Resampling.NEAREST)

        # increasing saturation
        _converter = ImageEnhance.Color(im)
        im = _converter.enhance(cls.SATURATION_ENHANCE_SCALE)

        # increasing red band's saturation.
        r, g, b = im.split()
        r = r.point(lambda i: i * cls.RED_BAND_INCREASE_RATIO)
        b = b.point(lambda i: i * cls.BLUE_BAND_INCREASE_RATIO)
        im = Image.merge('RGB', (r, g, b))

        return im
