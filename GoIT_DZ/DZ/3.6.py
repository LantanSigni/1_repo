def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        a = ' '
        string = a * (length - len(string)) + string
        return string


print(format_string('acaaaaaaaaaa', 12))
print(format_string('abaa', 15))
