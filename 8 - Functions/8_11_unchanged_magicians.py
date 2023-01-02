magicians = ['houdini', 'copperfield', 'henning']
great_magicians = []


def show_magicians(magicians_list):
    for magician in magicians_list:
        print(magician.title())


show_magicians(magicians)


def make_great(magicians_list):
    while magicians_list:
        current_magician = magicians_list.pop()
        great_magician = "Great " + current_magician
        great_magicians.append(great_magician)
        if not magicians_list:
            break


make_great(magicians[:])
print(magicians)
show_magicians(great_magicians)
