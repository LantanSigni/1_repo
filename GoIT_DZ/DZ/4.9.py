pin_codes = ['1101', '9034', '0011', '0011']


def is_valid_pin_codes(pin_codes):
    if not pin_codes or len(pin_codes) != len(set(pin_codes)):
        return False
    for pin in pin_codes:
        if len(pin) != 4 or not pin.isdigit():
            return False
    return True


print(is_valid_pin_codes(pin_codes))
