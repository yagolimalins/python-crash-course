import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    print(f"Welcome back, {username}!")

if get_stored_username() == None:
    get_new_username()
else:
    switch = input(f"Is your username {get_stored_username()} (Y/N): ").lower()
    if switch == 'n':
        get_new_username()

greet_user()