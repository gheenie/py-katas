"""
Assumptions:
english letters
"""


from src.caesar_cipher.caesar_cipher import (caesar_cipher)


def test_positive_num_and_over_26__letters_only():
    assert caesar_cipher('hello', 27) == 'ifmmp'


def test_negative_num_and_over_26__letters_only():
    assert caesar_cipher('hello', -27) == 'gdkkn'


def test_positive_num_and_over_26__letters_and_non_letters():
    assert caesar_cipher('hello world 123!', 27) == 'ifmmp xpsme 123!'


def test_negative_num_and_over_26__letters_and_non_letters():
    assert caesar_cipher('hello world 123!', -27) == 'gdkkn vnqkc 123!'


def test_0_returns_same_string():
    assert caesar_cipher('hello world 123!', 0) == 'hello world 123!'
