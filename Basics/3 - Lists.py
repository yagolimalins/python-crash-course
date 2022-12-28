#  Lists

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0].title()) #  Acessando índice 0 e capitalizando o item
print(bicycles[-1].upper())

print("My first bicycle was a " + bicycles[0].title() + ".") #  Concatenando em uma string

#  Inserir elementos em uma lista

bicycles.insert(0, 'caloi')
print(bicycles)

#  Remover elementos de uma lista

del bicycles[0] #  Keyword pode deletar objetos, variáveis, listas, itens de listas, dicionários etc
print(bicycles)

#  Remover usando pop()

popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)

first_owned = bicycles.pop(0)
print(first_owned)
print(bicycles)

# Remover um item pelo valor da variável

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

#  Ordenar com sort()

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#  Ordenar temporariamente com sorted()

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#  Print em uma lista em ordem reversa reverse()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#  Descobrir o tamanho de uma lista len()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))