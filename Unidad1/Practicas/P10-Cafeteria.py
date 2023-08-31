# Definición de arreglos
alimentos = ["Hamburguesa", "Pizza", "Ensalada", "Sandwich", "Pasta"]
bebidas = ["Agua", "Refresco", "Jugo", "Cafe", "Te"]
alumnos = []

# Método para agregar alumnos
def agregar_alumno():
    nombre = input("\nIngresa el nombre del alumno: ")
    alumnos.append({"nombre": nombre, "pedidos": []})

def agregar_pedido():
    nombre = input("\nIngresa el nombre del alumno: ")
    
    # Buscamos el nombre del alumno en el arreglo
    alumno = None
    for a in alumnos:
        if a["nombre"] == nombre:
            alumno = a
            break
    
    if alumno is None:
        print("Alumno no encontrado.")
        return
    
    # Solicitamos el alimento
    alimento = input("Ingresa el alimento: ")
    
    # Buscamos el alimento en el arreglo
    if alimento not in alimentos:
        print("Alimento no disponible.")
        return
    
    cantidad = int(input("Ingresa la cantidad: "))
    
    # Agregamos el pedido al arreglo del alumno
    alumno["pedidos"].append({
        "alimento": alimento,
        "cantidad": cantidad
    })

def imprimir_todos():
    for alumno in alumnos:
        print("\nAlumno:", alumno["nombre"])
        
        for pedido in alumno["pedidos"]:
            print("-", pedido["alimento"], pedido["cantidad"])

def main():
    while True:
        print("\n##__ MENU CAFETERIA __##")
        print("1) Agregar alumno")
        print("2) Agregar pedido")
        print("3) Imprimir todos")
        print("4) Salir")
        opcion = int(input("Ingresa una opción: "))
        
        if opcion == 1:
            agregar_alumno()
        elif opcion == 2:
            agregar_pedido()
        elif opcion == 3:
            imprimir_todos()
        elif opcion == 4:
            print("\n¡Saliendo del programa...!")
            break
        else:
            print("Opción inválida. Ingresa una opción válida.")

if __name__ == "__main__":
    main()
