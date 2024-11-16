def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    number_str = 0
    strings_positions = {}
    for string in strings:
        number_bytes =file.tell()
        file.write(f'{string}\n')
        number_str += 1
        strings_positions[(number_str, number_bytes)] = string
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('file_name.txt', info)
for elem in result.items():
  print(elem)