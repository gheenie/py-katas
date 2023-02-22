from src.years_of_growth.years_of_growth import (
    years_of_growth)


def test_correct_result():
    assert years_of_growth(1000, 2000, 2, 12) == 25

def test_0_growth():
    assert years_of_growth(1000, 2000, 0, 12) == 84

def test_0_growth_0_migration():
    assert years_of_growth(1000, 2000, 0, 0) == 'infinite'
