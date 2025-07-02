with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

txt = ''
for line in lines:
    txt += line
    txt = txt.replace('python', 'c')

print(txt)