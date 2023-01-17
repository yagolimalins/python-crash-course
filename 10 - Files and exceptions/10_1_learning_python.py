with open('learning_python.txt') as file:
    content = file.read()
    print(content + '\n')

with open('learning_python.txt') as file:
    for line in file:
        print(line.rstrip())

print()

with open('learning_python.txt') as file:
    lines = file.readlines()

file_lines = ''
for line in lines:
    file_lines += line.rstrip() + ' '

print(file_lines)