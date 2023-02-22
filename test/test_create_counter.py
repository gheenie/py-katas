from src.create_counter.create_counter import (
    create_counter)


def test_up():
    counter = create_counter(10)
    up = counter['up']

    assert up() == 11
    assert up() == 12
    assert up() == 13

def test_down():
    counter = create_counter(10)
    down = counter['down']

    assert down() == 9
    assert down() == 8
    assert down() == 7

def test_up_and_down():
    counter = create_counter(10)
    up = counter['up']
    down = counter['down']

    assert up() == 11
    assert down() == 10
    assert down() == 9
    assert up() == 10
