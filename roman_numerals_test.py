
from roman_numerals import func
from roman_numerals import convert_to_roman_numeral
def test_answer():
    assert func(3) == 5

def test_convert_one():
    assert convert_to_roman_numeral(1) == 'I'
