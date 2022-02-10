#str = string, que significa una cadena de texto, ejemplo "Perro", "Manzana" "esto es un texto"
#int = integer = Entero o numero entero osea sin decimales, 1, 2, 3, 4, 5, -25, -83
#float = floatante o que tiene numeros decimales 1.33, 13.865445, 0.3344, 0.000111212

#cuando tu dices def y luego pones nombre y los valores que recibe entre parentesis, estas escribiendo una funcion o definiendola
#def viene de Definition

numero1 = int(input("Numero1: "))
numero2 = int(input("Numero2: "))

def suma(a, b):
  return a + b

print(suma(numero1, numero2))