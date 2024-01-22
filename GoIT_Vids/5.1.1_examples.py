from re import sub

text = '''Python is a high-level, general-purpose programming language. \n
        Its design philosophy emphasizes code readability with the use of significant indentation. \n
        Python is dynamically typed and garbage-collected. \n
        It supports multiple programming paradigms, including structured, object-oriented and functional programming.'''

print(len(text.split(' ')))

reg_exp = r'[^A-Z a-z0-9]'
normalized_text = text.lower()
normalized_text = sub(reg_exp, '', normalized_text)
print(normalized_text)  # only words, lowercase.

words_list = normalized_text.split()

print(words_list)

unique_words = set(words_list)
n_words = len(words_list)
n_unique_words = len(unique_words)
print(n_words, n_unique_words)  # 36 words, 31 unique.

words_quantity = {}  # empty dict

for word in unique_words:
    words_quantity[word] = normalized_text.count(word)

print(words_quantity)

words_quantity_list = list(words_quantity.items())


def sort_by_quantity(element):
    return element[1]


# [('a', 21), ('it', 4), ('programming', 3), ('python', 2), ('and', 2), ('is', 2), ('highlevel', 1), ('readability', 1), ('multiple', 1), ('emphasizes', 1), ('garbagecollected', 1), ('the', 1), ('dynamically', 1), ('objectoriented', 1), ('generalpurpose', 1), ('design', 1), ('code', 1), ('language', 1), ('functional', 1), ('philosophy', 1), ('with', 1), ('supports', 1), ('typed', 1), ('use', 1), ('of', 1), ('structured', 1), ('paradigms', 1), ('indentation', 1), ('its', 1), ('including', 1), ('significant', 1)]
words_quantity_list.sort(key=sort_by_quantity, reverse=True)
print(words_quantity_list)
