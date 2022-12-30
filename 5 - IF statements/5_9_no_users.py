usernames = ['yago', 'yagolima', 'admin']

if usernames:
    login = input("Enter your login: ")
    if login in usernames:
        print("Hello " + login + " would you like to see a status report?")
    else:
        print("Hello guest, thank you for logging")
else:
    print("We need to register some users")