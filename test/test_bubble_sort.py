from src.bubble_sort.bubble_sort import (bubble_sort)

def test_sorting_works_on_list_of_nums():
    assert bubble_sort([1, 4, 2, 3]) == [1, 2, 3, 4]

def test_larger_list_of_nums():
    assert bubble_sort([8, 6, 7, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_one_item_in_list():
    assert bubble_sort([8]) == [8]

def test_empty_list():
    assert bubble_sort([]) == []

def test_original_array_not_mutated():
    input = [8, 6, 7, 5, 4, 3, 2, 1]

    output = bubble_sort(input)

    assert input == [8, 6, 7, 5, 4, 3, 2, 1]
    assert output is not input
