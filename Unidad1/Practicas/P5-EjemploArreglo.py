factura = ['pan', 'huevos', 100, 1234];

# print array (lista)
print(f'{factura}'); #Imprime la lista completa
print(f'{factura[0]}'); #Imprime el primer valor (en la posicion 0)

#print(f'{factura[3]}'); #Imprime el tercer valor (en la posicion 3)
#print(f'{len(factura)}'); # imprime el tamaño de la lista
#print(f'{len(factura)-1}'); #Imprime el tamaño de la lista sin contar la posicion 4

# Cambiamos el valor de la posicion 1
factura[1] = 'carne';
print(f'{factura}');

# Agregamos otro arreglo dentro del arreglo que ya tenemos 

nuevo_array = ['Prueba1', 'Prueba2', 'Prueba3']; #nuevo arreglo
factura[2] = nuevo_array;
print(f'{factura}');
print(f'{len(factura)}'); # el tamaño del array no cambia, ya que el nuevo array lo toma como un dato