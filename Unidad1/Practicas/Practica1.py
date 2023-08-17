# print('Hello World');

"""
nombre = str (input ('Ingresa tu nombre: '));
edad = int(input('Ingresa tu edad: '));
print(f"\nBienvenido!, {nombre}");
print(f"\nTienes {edad} años");
"""
lim = 1
i = 0;
while i <= lim:
  nombre = str (input ('Ingresa tu nombre: '));
  edad = int(input('Ingresa tu edad: '));
  print(f"\nBienvenido!, {nombre}");
  print(f"\nTienes {edad} años");

  print('\n¿Desea ingresar otros datos?');
  print('1) Si');
  print('2) No');
  lim = int (input('Ingresa tu opcion: '));

  if lim == 2:
    break
