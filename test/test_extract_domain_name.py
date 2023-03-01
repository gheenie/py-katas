from src.extract_domain_name.extract_domain_name import (extract_domain_name)


def test_reasonable_url():
    assert extract_domain_name('https://www.reddit.com/') == 'reddit.com'


def test_url_without_www():
    assert extract_domain_name('https://github.com/northcoders/de-py-katas') == 'github.com'


def test_url_with_long_queries():
    input = 'https://www.google.com/search?q=cats&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjO9Mrw2_v6AhXtTEEAHWYIBi8Q_AUoAXoECAIQAw&biw=1440&bih=764&dpr=2'

    assert extract_domain_name(input) == 'google.com'


def test_url_without_dotcom():
    assert extract_domain_name('https://github.co/northcoders/de-py-katas') == ''


def test_empty_url():
    assert extract_domain_name('') == ''
