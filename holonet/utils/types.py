from datetime import datetime, timedelta


def assert_string(value):
    assert isinstance(value, str), '%s is not a string' % str(value)


def assert_list_of_strings(value):
    assert isinstance(value, list), '%s is not a list' % str(value)
    for element in value:
        assert_string(element)


def assert_datetime(value):
    assert isinstance(value, datetime), '%s is not of type datetime' % str(datetime)


def assert_timedelta(value):
    assert isinstance(value, timedelta), '%s is not a timedelta' % str(value)


def assert_type(value, value_type):
    assert isinstance(value, value_type), '%s is not of type %s' % (str(value),
                                                                    str(value_type))
