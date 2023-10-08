import os

while True:
    site = input("Enter website address\n")

    if site == 'end':
        break

    if 'https://' in site:
        os.system('start ' + site)
        print('if')

    elif 'www.' in site:
        site = 'https://' + site
        os.system('start ' + site)
        print('elif')

    else:
        site = 'https://www.' + site
        os.system('start ' + site)
        print('else')
