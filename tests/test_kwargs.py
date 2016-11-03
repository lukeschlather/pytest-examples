def some_function(pos1, pos2, **kwargs):
    return (pos1, pos2, kwargs)


def test_some_function():
    result = some_function(0, 1, foo=3, bar=4)
    assert result[0] == 0
    assert result[1] == 1
    assert result[2] == {"foo": 3, "bar": 4}


def test_some_function_with_kwargs():
    args = {"foo": 3, "bar": 4}
    result = some_function(0, 1, **args)
    assert result[0] == 0
    assert result[1] == 1
    assert result[2] == args
