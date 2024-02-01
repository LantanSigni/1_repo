class User:
    def __init__(self, user_name):
        self.name = user_name

    # def find_myself_in_list(self, user_list):
    #     return user_list.count(self) != 0

    def find_myself_in_set(self, user_set):  # Змінився метод
        return self in user_set


class AccessControlList:
    def __init__(self, denied_users, allowed_users):
        self.denied = denied_users
        self.allowed = allowed_users

    def __add__(self, other):
        new_denied = self.denied | other.denied
        new_allowed = self.allowed | other.allowed
        return AccessControlList(new_denied, new_allowed)

    def request_access(self, user):
        # if user.find_myself_in_list(self.denied):
        if user.find_myself_in_set(self.denied):
            print('Access denied!')
            return False
        # elif user.find_myself_in_list(self.allowed):
        elif user.find_myself_in_set(self.allowed):
            print("Access granted.")
            return True
        else:
            print('Access denied!')
            return False


if __name__ == '__main__':
    alice = User('Alice')
    bob = User('Bob')
    carl = User('Carl')
    david = User('David')
    # user_list = [alice, bob, carl]
    # denied_user_list = [bob, carl, bob]
    # allowed_user_list = [alice, bob, carl]
    # denied_users_set = {bob, carl}  # Замість списку - множина!
    # allowed_users_set = {alice, bob, carl}  # Замість списку - множина!
    # print(alice.find_myself_in_list(user_list))  # True
    # print(david.find_myself_in_list(user_list))  # False
    # acl = AccessControlList(denied_user_list, allowed_user_list)
    # acl = AccessControlList(denied_users_set, allowed_users_set)
    # print(acl.request_access(alice))  # True
    # print(acl.request_access(bob))  # False
    # print(acl.request_access(david))  # False
    denied_users_set = {bob}
    allowed_users_set = {alice, bob}
    acl1 = AccessControlList({bob}, {alice, david})
    acl2 = AccessControlList({carl}, {alice, bob})
    acl3 = acl1 + acl2  # Ось тут відбувається виклик магічного методу __add__

    print("denied users:")
    for user in acl3.denied:
        print(user.name)

    print("allowed users:")
    for user in acl3.allowed:
        print(user.name)
