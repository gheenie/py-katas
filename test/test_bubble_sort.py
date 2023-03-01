from src.bubble_sort.bubble_sort import (bubble_sort)

def test_sorting_works_on_list_of_nums():
    assert bubble_sort([1, 4, 2, 3]) == [1, 2, 3, 4]
