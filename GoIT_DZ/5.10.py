import re


def find_word(text, word):
    match = re.search(word, text)
    if match is not None:
        start, end = match.span()
        search = {'result': True, 'first_index': start,
                  'last_index': end, 'search_string': word, 'string': text}
        return search
    else:
        search = {'result': False, 'first_index': None,
                  'last_index': None, 'search_string': word, 'string': text}
        return search


text = 'Did you train your dragon?'
word = 'dragon'

result = find_word(text, word)
print(result)
