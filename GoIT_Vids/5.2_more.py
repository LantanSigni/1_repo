from re import search
result = search('^Hello', 'Hello world')  # look for string starting from
print(result)

result = search('world$', 'Hello world')  # look for string ending on
print(result)

result = search('world', 'Hello world')  # look for string with world
print(result)

result = search('l*', 'Hello world')  # look for 0+ l symbols
print(result)

# look for world, worlds, worldss, etc
# * is +0 and more repeats of the symbol
result = search('worlds*', 'Hello worldssss')
print(result)

# 1 and more times. world will not work here
result = search('worlds+', 'Hello worlds')
print(result)

result = search('worlds?', 'Hello world')  # 0 or 1 times for s
print(result)

# looking for 3 times s - sss only!
result = search('worlds{3}', 'Hello worldsss')
print(result)

result = search('worlds{3,6}', 'Hello worldsssss')  # 3-6 times s
print(result)

result = search('worl(ds)?', 'Hello worlds')  # for multiple symbols
print(result)

result = search('world(s|e)', 'Hello worlde')  # s or e
print(result)

result = search('world[seo]', 'Hello worldo')  # s or e or o
print(result)
