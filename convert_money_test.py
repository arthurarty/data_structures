from convert_money import convert_money


def test_int():
    ans = convert_money(15)
    assert ans == 15


def test_string():
    ans = convert_money('14')
    assert ans == 14


def test_handle_millions():
    ans = convert_money('14M')
    assert ans == 14000000


def test_handle_dollar():
    ans = convert_money('$14m')
    assert ans == 14000000


def test_handle_floats():
    ans = convert_money('3.2M')
    assert ans == 3200000
