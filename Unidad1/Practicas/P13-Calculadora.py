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

    def mostrar(self):
        for item in self.items:
            print(str(item))


def calculadora_polaca(elementos):
    """ Calcula una expresión en notación polaca inversa """
    pila = Pila()

    for elemento in elementos:
        try:
            numero = float(elemento)
            pila.apilar(numero)
        except ValueError:
            if elemento not in "+-*/%":
                raise ValueError("Operando no válido")

            try:
                operando2 = pila.desapilar()
                operando1 = pila.desapilar()
            except ValueError:
                raise ValueError("Faltan operandos")

            resultado = operando1 + operando2

            pila.apilar(resultado)

    return pila.desapilar()


if __name__ == "__main__":
    expresion = "2 3 +"
    elementos = expresion.split()
    resultado = calculadora_polaca(elementos)
    print(resultado)

