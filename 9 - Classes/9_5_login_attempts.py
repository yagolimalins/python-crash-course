class User():
    def __init__(self, first_name, last_name, email, uid):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.uid = uid
        self.login_attempts = 0

    def describe_user(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Email: " + self.email)
        print("User ID: " + self.uid)

    def greet_user(self):
        print("Hello " + self.first_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("Yago", "Lima", "yago.lima.lins@protonmail.com", "82940185")

print("Tentativas de login do usuário " + user.uid + ": " + str(user.login_attempts))

user.increment_login_attempts()

print("Tentativas de login do usuário " + user.uid + ": " + str(user.login_attempts))

user.reset_login_attempts()

print("Tentativas de login do usuário " + user.uid + ": " + str(user.login_attempts))
