class Privileges():
    def __init__(self):
        self.privileges = ["can post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
