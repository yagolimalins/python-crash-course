cidades = ['Maceió', 'Arapiraca', 'Delmiro Gouveia', 'Penedo', 'Palmeira dos Indios']

print(cidades)
print(cidades[3])
cidades.insert(2, 'Marechal Deodoro')
print(cidades)
cidades.append('Anadia')
print(cidades)
del cidades[-1]
print(cidades)
cidade_poppada = cidades.pop(2)
print(cidade_poppada)
print((cidades))
cidades.remove('Arapiraca')
print(cidades)

cidades.sort()
print(cidades)
cidades.sort(reverse=True)
print(cidades)

cidades = ['Maceió', 'Arapiraca', 'Delmiro Gouveia', 'Penedo', 'Palmeira dos Indios']
print(sorted(cidades))
print(cidades)
cidades.reverse()
print(cidades)
cidades.reverse()
print(cidades)
print(len(cidades))