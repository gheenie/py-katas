from src.sum_ascii.sum_ascii import (
    sum_ascii)

def test_one_item():
    assert sum_ascii(['John']) == 'John'

def test_multiple_items____different_cases():
    assert sum_ascii(['jjjj', 'ZZZZ', 'zzza']) == 'ZZZZ'
