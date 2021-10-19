
from roman_numerals import convert_to_roman_numeral

def test_convert_one():
    assert convert_to_roman_numeral(1) == 'I'

def test_convert_two():
    assert convert_to_roman_numeral(2) == 'II'

def test_convert_three():
    assert convert_to_roman_numeral(3) == 'III'

def test_convert_four():
    assert convert_to_roman_numeral(4) == 'IV'

def test_convert_five():
    assert convert_to_roman_numeral(5) == 'V'

def test_convert_six():
    assert convert_to_roman_numeral(6) == 'VI'

def test_convert_seven():
    assert convert_to_roman_numeral(7) == 'VII'

def test_convert_eight():
    assert convert_to_roman_numeral(8) == 'VIII'

def test_convert_nine():
    assert convert_to_roman_numeral(9) == 'IX'

def test_convert_ten():
    assert convert_to_roman_numeral(10) == 'X'
