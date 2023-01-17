while True:
    pool = ''
    name = input('Enter your name: ')
    reason = input('Why do you like programming? ')
    with open('programming_pool.txt', 'a') as file:
        file.write(name + ': ' + reason + '\n')