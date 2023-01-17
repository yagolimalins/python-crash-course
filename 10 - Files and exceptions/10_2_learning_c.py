with open('learning_python.txt') as file:
    lines = file.readlines()

files_lines = ''

for line in lines:
    files_lines += line

message = files_lines.replace('classes', 'kotlin')

print(message)