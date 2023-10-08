user = {
    'name': 'Bill',
    'surname': 'Bosh',
    'age': 22
}
if 'name' in user:
    print(user['name'])
else:
    print('You forgot the name!')

if 'age' in user:
    print(f"User is {user['age']} years old.")
