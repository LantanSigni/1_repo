is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")

is_active = bool(is_active)
is_admin = bool(is_admin)
is_permission = bool(is_permission)

access = bool()
if is_admin:
    access = True
    print('Access status:', access)
elif is_active and is_permission:
    access = True
    print('Access status:', access)
else:
    access = False
    print('Access status:', access)
