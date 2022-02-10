from ntpath import join
from os import sep


cadena1 = "árbol"
telefono="644-4623050"

#print(cadena1)
#print(cadena1[1])

#for letra in cadena1:
#  print(letra)

numero = 55

#print(len(cadena1))

#for
#for index in range(len(telefono)):
  #print(telefono[index], end='')
  #if(index == 1):
    #print(telefono[index], end='-', sep='')
#print()

#regular expresion
#nuevaCadena =  telefono.split(sep='-', maxsplit=2)

#print(nuevaCadena)

#foreach
#for letra in telefono:
#  print(telefono, end='-')

'''abc = 'abcdefg'

print(abc[0:0])
print(abc[0:1])
print(abc[0:2])
print(abc[0:3])

print(abc[1:1])
print(abc[1:2])
print(abc[1:3])

print(abc[1:3])'''

alphabet = "abcdefghijfffklmnopqrstuvwxyz"

correo = 'jfcarocota@gmail.com'

#print("fff" not in alphabet)
#print("F" in alphabet)
#print("1" in alphabet)
#print("ghi" in alphabet)
#print("Xyz" in alphabet)
#
#print('@' in correo)

#correo[3]='k'
#print(correo[3])

# Demonstrando min() - Ejemplo 1:
#print(min("aAbByYzZ"))


# Demonstrando min() - Ejemplo 2 y 3:
t = 'Los Caballeros Que Dicen "¡Ni!"'
#print('[' + min(t) + ']')

t = [0, 1, 2]
#print(min(t))

#reverseMail = list(correo)
#reverseMail.pop()
#print(reverseMail)

#print(correo.capitalize())
#print(correo.upper())

#print('['+ correo.center(50) +']')
#print(f'[{correo.center(50, "*")}]')

#print(correo.endswith('.com'))
#print(correo.find('k'))
#print(correo.index('k'))

nombreCompleto = ["Jesus", "Francisco", "Caro", "Cota"]
myname = " ".join(nombreCompleto)
#print(myname.replace("Jesus", "").lstrip().lower())

# Demostración del método rfind():
#print("tau tau tau".rfind("ta"))
#print("tau tau tau".rfind("ta", 9))
#print("tau tau tau".rfind("ta", 3, 9))

paises = ["México", "Honduras", "Argentina", "Chile", "Perú", "Brasil"]

print(sorted(paises))