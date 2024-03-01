# with open('test.txt', 'r') as fh:  --- close file once operation is complete

import os

# set active directory as current location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

######

fh = open('test.txt', 'w+')
fh.write('hello!')
fh.seek(0)    # return pointer to the start of the file

# symbols_written = fh.write('hello!')
# print(symbols_written)  # 6

first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'he'
fh.close()

fh = open('test.txt', 'r')
all_file = fh.read()
print(all_file)  # 'hello!'

fh.close()

######

fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()

######

fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line)

fh.close()

####

fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
lines = fh.readlines()
print(lines)

fh.close()

######
