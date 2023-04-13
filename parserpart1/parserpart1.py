from urllib.parse import urlparse


def parse(query: str) -> dict:
    params = {}
    if query:
        query = urlparse(query).query
        param_list = query.split('&')
        for param in param_list:
            if '=' in param:
                key, value = param.split('=')
                params[key] = value
    return params


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page') == {}
    assert parse('') == {}
    assert parse('https://example.com/path/to/page?') == {}
    assert parse('http://example.com/?name=Dima&age=28') == {'name': 'Dima', 'age': '28'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&age=2&size=small') == {'name': 'ferret',
                                                                                                   'color': 'purple',
                                                                                                   'age': '2',
                                                                                                   'size': 'small'}
