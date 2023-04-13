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


def parse_cookie(query: str) -> dict:
    result = {}
    if query:
        params = query.split(';')
        for param in params:
            key_value = param.split('=')
            if len(key_value) >= 2:
                key = key_value[0].strip()
                value = '='.join(key_value[1:]).strip()
                result[key] = value
    return result


if __name__ == '__main__':
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=25;') == {'name': 'John', 'age': '25'}
    assert parse_cookie('name=John=Doe;age=25;') == {'name': 'John=Doe', 'age': '25'}
    assert parse_cookie('name=John;age=25;gender=male') == {'name': 'John', 'age': '25', 'gender': 'male'}
    assert parse_cookie('name=John;age=25;gender=male;country=USA') == {'name': 'John', 'age': '25', 'gender': 'male',
                                                                        'country': 'USA'}
    assert parse_cookie('age=25;') == {'age': '25'}
    assert parse_cookie('age=25;country=USA') == {'age': '25', 'country': 'USA'}
    assert parse_cookie('country=USA') == {'country': 'USA'}
    assert parse_cookie('name=John') == {'name': 'John'}
