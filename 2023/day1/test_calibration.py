from calibration import get_calibration_value, get_first_char

digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

reverse = {label[::-1]: val for label, val in digits.items()}

def test_get_calibration_value():
    # Value = 28
    line = 'ABC2kjhasdk34kjhasdk8kjh'
    value = get_calibration_value(line)
    assert value == 28

    assert get_calibration_value('seven908') == 78
    assert get_calibration_value('ninenine') == 99
    assert get_calibration_value('423eight') == 48 

def test_get_first_char():

    # Should get 2
    line = "ababababa234sadasdsad"
    value = get_first_char(line, digits)
    assert value == 2

    assert get_first_char("one234five", digits) == 1
    assert get_first_char("evif432eno", reverse) == 5


if __name__ == "__main__":
    test_get_calibration_value()
    test_get_first_char()
    print("Test passed!!")