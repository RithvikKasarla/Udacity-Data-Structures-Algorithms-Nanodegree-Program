class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    try:
        users = group.get_users()
    except:
        return "Not a Group"
    if user in users:
        return True
    else:
        for group in group.get_groups():
            if is_user_in_group(user, group):
                return True
    return False


if __name__ == "__main__":
    print(is_user_in_group("sub_child_user",parent)) #true
    print(is_user_in_group("USER",parent))#False
    print(is_user_in_group("sub_child_user", "NOT A Group")) #Not a Group