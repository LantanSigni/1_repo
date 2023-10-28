import os
import time

('C:\\_My repos\\Example', ['1 Folder', '2 Folder'], [
 'Picture.jpg', 'Text.txt', 'Text_again.txt'])

spisok = []

for address, dirs, files in os.walk('C:\\_My repos\Example'):
    # spisok.append(address) - print all folder only
    for file in files:
        full = os.path.join(address, file)
        # if '.txt' in full:  --- show only txt files
        #     spisok.append(full)
        if time.time() - os.path.getctime(full) < 86400:
            spisok.append(full)

print(spisok)
