filename = 'alice.txt'
with open(filename, encoding='utf-8') as file_object:
    lines = file_object.read()
    line = lines.lower().count('the ')
    print(line)