s = 'Hi there!'

start = 0
end = 7

print(s.find('er', start, end))
print(s.find('q'))

v = 'Some words'
print(v.find('o'), 'position (starts from 0) number of o')
print(v.rfind('o'))
print(v.index('o'))
print(v.rindex('o'))

d = "I am learning strings in Py. Some new methods got now."
sentences = d.split(".")
print(sentences[1])
print(sentences[0])
print(sentences[2])  # should be just empty row

sent = ['  I am learning strings in Py', 'Some new methods I got here.  ']
joined = '. '.join(sent)
print(joined)

no_f = joined.lstrip()
print(no_f)
no_b = joined.rstrip()
print(no_b)
clean = joined.strip()
print(clean)

dog_t = 'All dogs bark like dogs.'
cat_t = dog_t.replace('dogs', 'cats')
print(cat_t)
cat_t1 = cat_t.replace('bark', 'meow')
print(cat_t1)
