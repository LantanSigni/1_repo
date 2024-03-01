from re import sub


text = 'Alex\nKdfe23\t\f\v.\r'


def real_len(text):
    symbol_to_exclude = r'[\n, \f, \r, \t, \v]'
    clean_text = len(sub(symbol_to_exclude, '', text))
    return clean_text


print(real_len(text))
