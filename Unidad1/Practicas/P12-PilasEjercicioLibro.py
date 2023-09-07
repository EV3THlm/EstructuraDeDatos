class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, x):
        """ Agrega el elemento 'x' a la pila """
        self.items.append(x)

    def desapilar(self):
        if self.es_vacia():
            raise ValueError("La pila está vacía")
        return self.items.pop()

    def es_vacia(self):
        return len(self.items) == 0

def imprimir_pila(pila):
    for item in pila.items:
        print(str(item))


p = Pila()

print("Menú de la pila")
print("1. Apilar")
print("2. Desapilar")
print("3. Imprimir")
print("4. Salir")

while True:
    opción = input("Elige una opción: ")

    if opción == "1":
        n = input("Introduce un número a apilar: ")
        p.apilar(n)

    elif opción == "2":
        p.desapilar()

    elif opción == "3":
        imprimir_pila(p)

    elif opción == "4":
        break

    else:
        print("Opción no válida")
