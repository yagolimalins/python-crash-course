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
        
user = User("Yago", "Lima", "yago.lima.lins@protonmail.com", "83920306")

user.describe_user()

user.greet_user()

user = User("Edgar", "Azevedo", "edgar-azevedo@protonmail.com", "02860195")

user.describe_user()

user.greet_user()