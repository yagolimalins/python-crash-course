from collections import OrderedDict

glossary = OrderedDict()

glossary['print'] = 'Imprime informação na tela'
glossary['del'] = 'Deleta informações'
glossary['for'] = 'Usado para iterações principalmente em listas'
glossary['if'] = 'Usado para testar condições'
glossary['while'] = 'Usado para loops sob determinada condição'
glossary['set'] = 'Seleciona todos os valores unicos de uma lista'

for key, value in glossary.items():
    print(key + ": " + value)