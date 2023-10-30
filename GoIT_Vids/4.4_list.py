text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# words = text.split()
# print(words)
start = 0
words = []
for indx, char in enumerate(text):  # indexation
    if not char.lower() in alphabet:  # cheking lower register letters
        word = text[start:indx]
        words.append(word.strip())
        start = indx
print(words)
