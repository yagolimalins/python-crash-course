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

print("Só posso convidar duas pessoas para o jantar")

out_of_party = guest_list.pop()
print("Desculpe-me " + out_of_party + " mas não posso te convidar para o jantar")
out_of_party = guest_list.pop()
print("Desculpe-me " + out_of_party + " mas não posso te convidar para o jantar")
out_of_party = guest_list.pop()
print("Desculpe-me " + out_of_party + " mas não posso te convidar para o jantar")
out_of_party = guest_list.pop()
print("Desculpe-me " + out_of_party + " mas não posso te convidar para o jantar")

print(guest_list)
print(guest_list[0] + ' e ' + guest_list[1] + ' vocês ainda estão convidados para a festa')

del guest_list[0]
del guest_list[0]

print(guest_list)