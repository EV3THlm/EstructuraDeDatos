def pila():
  """Implementa una pila en Python usando una lista."""
  pila = []

  def apilar(item):
    """Agrega un elemento a la pila."""
    pila.append(item)

  def desapilar():
    """Elimina el elemento superior de la pila y lo devuelve."""
    return pila.pop()

  def esta_vacia():
    """Devuelve True si la pila está vacía, False si no."""
    return len(pila) == 0

  return pila


pila = pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)

print(pila.desapilar())
print(pila.desapilar())
print(pila.desapilar())

# Salida:
# 3
# 2
# 1
