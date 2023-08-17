# Array
arreglini = []

while True:
    nombre = input('Ingresa tu nombre: ')
    edad = int(input('Ingresa tu edad: '))
    
    # Guardamos los datos en el array
    arreglini.append([nombre, edad])
    
    print("\n".join([f"{nombre}: {edad}" for nombre, edad in arreglini]))
    
    print("\n¿Desea ingresar mas datos?")
    print("1) Si")
    print("2) No")
    lim = int(input("Ingresa una opcion: "))
    
    if lim == 2:
        break
