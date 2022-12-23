from effects import _blur


class EffectsCreator:
    def __init__(self) -> None:
        pass

    def blur(self, image: str, radius: int = 1):
        return _blur._blur.renderimage(image, radius)
