from src.herd_the_babies.herd_the_babies import (
    herd_the_babies)

def test_1_family():
    assert herd_the_babies('aA') == 'Aa'

def test_multiple_families_some_without_babies():
    assert herd_the_babies('aBA') == 'AaB'

def test_multiple_families():
    assert herd_the_babies('bbaBccAC') == 'AaBbbCcc'

def test_multiple_parents():
    assert herd_the_babies('bbaDDDBccddAC') == 'AaBbbCccDDDdd'
