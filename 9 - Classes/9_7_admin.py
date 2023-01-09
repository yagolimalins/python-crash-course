class User():
    def __init__(self, first_name, last_name, email, uid):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.uid = uid

    def describe_user(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Email: " + self.email)
        print("User ID: " + self.uid)

    def greet_user(self):
        print("Hello " + self.first_name)


class Admin(User):
    def __init__(self, first_name, last_name, email, uid):
        super().__init__(first_name, last_name, email, uid)
        self.privileges = ["can post", "can delete post", "can ban user"]

    def show_privileges(self):
            for privilege in self.privileges:
                print(privilege)

admin_1 = Admin("Yago", "Lima", "yago.lima.lins@protonmail.com", "94018532")

admin_1.greet_user()
admin_1.show_privileges()