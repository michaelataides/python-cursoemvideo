a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaço? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())

print('\nO tipo primitivo da entrada é {}\n'
     'Só tem espaço? {}\n'
      'É um número? {}\n'
      'É alfabético? {}\n'
      'É alfanumérico? {}\n'
      'Está em maiúsulas? {}\n'
      'Está em minúsculas? {}\n'
      .format(type(a),a.isspace(),a.isnumeric(),a.isalpha(),a.isalnum(),a.isupper(),a.islower())




      )