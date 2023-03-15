from src.roman_numeral_encoder.roman_numeral_encoder import (roman_numeral_encoder)


def test_1_to_9():
    assert roman_numeral_encoder(3) == 'I'
    assert roman_numeral_encoder(4) == 'IV'
    assert roman_numeral_encoder(5) == 'I'
    assert roman_numeral_encoder(6) == 'VI'
    assert roman_numeral_encoder(9) == 'IX'


def test_10_to_39():
    pass


def test_40_to_69():
    pass


def test_90_to_119():
    pass
