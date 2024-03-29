import re
from re import search, findall, sub


my_str = 'the first line\nthe second line'
print(my_str)

translate_map = {ord('Є'): 'ie', ord('і'): 'y'}
print('єдині пєльмєні'.translate(translate_map))
# єдинy пєльмєнy

url_regexp = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
# <re.Match object; span=(0, 22), match='https://www.google.com'>
result = search(url_regexp, 'https://www.google.com')
print(result)
# <re.Match object; span=(29, 51), match='https://www.google.com'>
result = search(
    url_regexp, 'Here you can find some info: https://www.google.com Take care!')
print(result)
# (29, 51)
print(result.span())

my_simple_regexp = r'.\d'
# span=(0, 2) - only 1 result
result = search(my_simple_regexp, 'a1  asd  10')
# ['a1', '1'] - 2 results now
result = findall(my_simple_regexp, 'a1  asd  10')
# '*  asd *0' - substitute tuple above for *
print(sub(my_simple_regexp, '*', 'a1  asd  10'))
