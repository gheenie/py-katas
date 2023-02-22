from src.get_distinct_letters.get_distinct_letters import (
    get_distinct_letters)


def test_no_distinct_letters():
    assert get_distinct_letters('eaf', 'fae') == ''

def test_distinct_letters_from_second_word():
    assert get_distinct_letters('eaf', 'faeop') == 'op'

def test_distinct_letters_from_first_word():
    assert get_distinct_letters('opeaf', 'fae') == 'op'

def test_distinct_but_multiple_letters_from_first_word():
    assert get_distinct_letters('opeafop', 'fae') == 'op'

def test_distinct_letters_from_both_words__multiple_from_first():
    assert get_distinct_letters('opeafop', 'qfaew') == 'opqw'

def test_empty_string_from_one_word():
    assert get_distinct_letters('hello', '') == 'ehlo'

def test_specific_examples():
    assert get_distinct_letters('hello', 'worldoo') == 'dehrw'
