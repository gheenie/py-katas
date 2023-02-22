from src.lengthen_date.lengthen_date import (
    lengthen_date)


def test_current_day__suffixed_day__stringified_month():
    assert lengthen_date('21.03.2017') == 'Tuesday 21st March 2017'
    assert lengthen_date('22.02.2023') == 'Wednesday 22nd February 2023'
    