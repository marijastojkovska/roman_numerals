
from roman_numerals import convert_to_roman_numeral

def test_convert_one():
    assert convert_to_roman_numeral(1) == 'I'

def test_convert_two():
    assert convert_to_roman_numeral(2) == 'II'
