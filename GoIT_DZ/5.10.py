import re

text = 'Did you train your dragon?'
word = 'dragon'


def find_word(text, word):
    match = re.search(f'\{word}', text)
    if match:
        start, end = match.span()
        search = [{'result': 'True'}, {'first_index': start}, {
            'last_index': end}, {'search_string': word}, {'string': text}]
        return search
    else:
        search = [{'result': 'False'}, {'first_index': None}, {
            'last_index': None}, {'search_string': word}, {'string': text}]
        return search


print(find_word(text, word))
