usernames = ['yagolima', 'edgarazevedo', 'elianaqueiroz', 'aliciadalmeida', 'darlanoliveira']
new_users = ['joaosantos', 'mariasouza', 'lucasnascimento', 'luciarodrigues', 'yagolima']

for user in new_users:
    if user.lower() in usernames:
        print("The username " + user + " has been already used, enter a new one")
    elif user.lower() not in usernames:
        print("The username " + user + " is available")