from src.get_century.get_century import (
    get_century)


def test_century_ending_1_to_3():
    assert get_century(38) == '1st'
    assert get_century(123) == '2nd'
    assert get_century(218) == '3rd'
    assert get_century(2004) == '21st'
    assert get_century(2114) == '22nd'
    assert get_century(2224) == '23rd'
    assert get_century(10001) == '101st'
    assert get_century(10101) == '102nd'
    assert get_century(10201) == '103rd'

def test_special_cases_11_to_13():
    assert get_century(1050) == '11th'
    assert get_century(1150) == '12th'
    assert get_century(1250) == '13th'

def test_century_ending_4_to_6():
    assert get_century(2304) == '24th'
    assert get_century(2414) == '25th'
    assert get_century(2523) == '26th'

def test_century_ending_4_to_6__year_ending_99_00_01():
    assert get_century(399) == '4th'
    assert get_century(500) == '5th'
    assert get_century(501) == '6th'

def test_century_ending_7_to_0():
    assert get_century(1677) == '17th'
    assert get_century(1777) == '18th'
    assert get_century(1877) == '19th'
    assert get_century(1977) == '20th'
    assert get_century(10000) == '100th'