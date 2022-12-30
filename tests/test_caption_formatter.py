from ImageEffects.utils import format_text


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
        "Lorem ipsum dolor sit amet,\nconsectetur adipiscing",
        "Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\nSed eleifend, odio nec finibus\ninterdum, dui mi convallis\ndui, sed aliquet"
    ]

    for _index, i in enumerate(OUTPUTS):
        assert format_text(21, text=INPUTS[_index]) == OUTPUTS[_index]
