from src.alphabet_position.alphabet_position import alphabet_position


def test_only_alphabets():
    assert alphabet_position('z') == '26'
    assert alphabet_position('abc') == '1 2 3'


def test_alphabets_and_non_alphabets():
    assert alphabet_position("The sunset sets at twelve o' clock.") == '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'


def test_only_non_alphabets():
    assert alphabet_position('1234567890!@#$%^&*(),.') == ''
