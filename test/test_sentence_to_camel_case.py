from src.sentence_to_camel_case.sentence_to_camel_case import (
    sentence_to_camel_case)


def test_returns_a_single_word_in_upper_if_true():
    expected = 'This'
    result = sentence_to_camel_case('this', True)
    print(f'Result is: {result}')
    assert result == expected

def test_returns_a_single_word_in_lower_if_false():
    expected = 'this'
    result = sentence_to_camel_case('this', False)
    print(f'Result is: {result}')
    assert result == expected

def test_all_spaced_words_capitalised_if_true():
    expected = 'ThisSentence'
    result = sentence_to_camel_case('this sentence', True)
    print(f'Result is: {result}')
    assert result == expected

def test_all_except_1st_spaced_words_capitalised_if_false():
    expected = 'thisSentence'
    result = sentence_to_camel_case('this sentence', False)
    print(f'Result is: {result}')
    assert result == expected

    expected = 'thisBiggerStrangeSentence'
    result = sentence_to_camel_case('This Bigger strange Sentence', False)
    print(f'Result is: {result}')
    assert result == expected

def test_empty_string():
    expected = ''
    result = sentence_to_camel_case('', False)
    print(f'Result is: {result}')
    assert result == expected
