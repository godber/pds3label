from pds3label.types import BasedInteger


def test_based_integer_init():
    int1 = BasedInteger('2#0000111111111111#')
    assert int1.based_integer_string == '2#0000111111111111#'
    assert int1.base == 2
    assert int1.value == '0000111111111111'
    assert int1.int_value == 4095


def test_based_integer_binary():
    int1 = BasedInteger('2#1001011#')
    assert int1.based_integer_string == '2#1001011#'
    assert int1.base == 2
    assert int1.value == '1001011'
    assert int1.int_value == 75


def test_based_integer_octal():
    int1 = BasedInteger('8#113#')
    assert int1.based_integer_string == '8#113#'
    assert int1.base == 8
    assert int1.value == '113'
    assert int1.int_value == 75


def test_based_integer_decimal():
    int1 = BasedInteger('10#75#')
    assert int1.based_integer_string == '10#75#'
    assert int1.base == 10
    assert int1.value == '75'
    assert int1.int_value == 75


def test_based_integer_hex():
    int1 = BasedInteger('16#4B#')
    assert int1.based_integer_string == '16#4B#'
    assert int1.base == 16
    assert int1.value == '4B'
    assert int1.int_value == 75


def test_based_integer_hex_plus():
    int1 = BasedInteger('16#+4B#')
    assert int1.based_integer_string == '16#+4B#'
    assert int1.base == 16
    assert int1.value == '+4B'
    assert int1.int_value == 75


def test_based_integer_hex_minus():
    int1 = BasedInteger('16#-4B#')
    assert int1.based_integer_string == '16#-4B#'
    assert int1.base == 16
    assert int1.value == '-4B'
    assert int1.int_value == -75
