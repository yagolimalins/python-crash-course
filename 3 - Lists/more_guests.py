guest_list = ['Edgar', 'Eliana', 'Alicia']

for i in guest_list:
    print(i + " venha para minha festa")

print(guest_list[1] + " não conseguiu vir a minha festa")

guest_list[1] = 'Joana'

for i in guest_list:
    print(i + " venha para minha festa")

print("Consegui uma mesa maior para minha festa!")

guest_list.insert(0, 'Maria')
guest_list.insert(2, 'João')
guest_list.append('José')

for i in guest_list:
    print(i + " venha para minha festa")