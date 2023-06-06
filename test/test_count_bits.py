from src.count_bits.count_bits import (count_bits)


def test_positive_nums():
    assert count_bits(1234) == 5
    assert count_bits(12) == 2
    assert count_bits(11) == 3
    assert count_bits(100111) == 9
