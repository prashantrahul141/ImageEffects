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

    OUTPUTS = [
        "Lorem",
        "Lorem Ipsum",
        "Lorem ipsum dolor",
        "Lorem ipsum dolor sit\namet, consectetur\nadipiscing",
        "Lorem ipsum dolor sit\namet, consectetur\nadipiscing elit. Sed\neleifend, odio nec\nfinibus interdum,\ndui mi convallis dui,\nsed aliquet"
    ]

    for _index, i in enumerate(OUTPUTS):
        assert _caption1.format_text(INPUTS[_index]) == OUTPUTS[_index]
