from ImageEffects.effects._caption1 import _caption1


def test_caption_formatter():
    '''tests the formatter for caption functions'''
    INPUTS = [
        "Lorem",
        "Lorem Ipsum",
        "Lorem ipsum dolor",
        "Lorem ipsum dolor sit amet, consectetur adipiscing",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifend, odio nec finibus interdum, dui mi convallis dui, sed aliquet"
    ]

    OUTPUT = [
        "Lorem"

    ]

    assert _caption1.format_text(INPUTS[0]) == OUTPUT[0]
