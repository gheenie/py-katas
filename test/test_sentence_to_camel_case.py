from sentence_to_camel_case.sentence_to_camel_case import sentence_to_camel_case


def test_returns_a_single_word_in_upper_if_true():
    expected = 'This'
    result = sentence_to_camel_case('this', True)
    print(f'Result is: {result}')
    assert result == expected
