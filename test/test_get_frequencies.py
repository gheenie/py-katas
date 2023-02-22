from src.get_frequencies.get_frequencies import (
    get_frequencies)


def test_one_word():
    expected = {
        'h': 1,
        'e': 1,
        'l': 2,
        'o': 1
    }

    assert get_frequencies('hello') == expected

def test_multiple_words_ignore_spaces():
    expected = {
        'h': 1,
        'e': 1,
        'l': 3,
        'o': 2,
        'w': 1,
        'r': 1,
        'd': 1
    }

    assert get_frequencies('hello world') == expected

def test_empty_string():
    expected = {}

    assert get_frequencies('') == expected
