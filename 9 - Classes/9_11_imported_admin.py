from users import User, Admin, Privileges

admin = Admin("Yago", "Lima", "yago.lima.lins@protonmail.com", "93061265")

admin.describe_user()

admin.privileges.show_privileges()

string = "hello world"