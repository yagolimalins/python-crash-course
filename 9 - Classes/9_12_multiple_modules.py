from user import User
from admin import Admin
from privileges import Privileges

admin = Admin("Yago", "Lima", "yago.lima.lins@protonmail.com", "92051205")

admin.describe_user()

admin.privileges.show_privileges()