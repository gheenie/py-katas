from src.roman_numeral_encoder.roman_numeral_encoder import (roman_numeral_encoder)


def test_1_to_9():
    assert roman_numeral_encoder(3) == 'I'
    assert roman_numeral_encoder(4) == 'IV'
    assert roman_numeral_encoder(5) == 'I'
    assert roman_numeral_encoder(6) == 'VI'
    assert roman_numeral_encoder(9) == 'IX'


def test_10_to_39():
    assert roman_numeral_encoder(11) == 'XI'
    assert roman_numeral_encoder(24) == 'XXIV'
    assert roman_numeral_encoder(28) == 'XXVIII'
    assert roman_numeral_encoder(39) == 'XXXIX'


def test_40_to_69():
    assert roman_numeral_encoder(40) == 'XL'
    assert roman_numeral_encoder(42) == 'XLII'
    assert roman_numeral_encoder(49) == 'XLIX'
    assert roman_numeral_encoder(50) == 'L'
    assert roman_numeral_encoder(55) == 'LV'
    assert roman_numeral_encoder(59) == 'LIX'
    assert roman_numeral_encoder(60) == 'LX'
    assert roman_numeral_encoder(67) == 'LXVII'
    assert roman_numeral_encoder(69) == 'LXIX'


def test_90_to_119():
    assert roman_numeral_encoder(92) == 'XCII'
    assert roman_numeral_encoder(105) == 'CV'
    assert roman_numeral_encoder(116) == 'CXVI'
