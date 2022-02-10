edad = 28
nombre = "Issac"

edadLegal = 18

if edad >= edadLegal:
  print(f'Felicidades {nombre} por tur mayoría de edad')
else:
  print(f'Hola {nombre}, aún eres menor de edad')

steps = 10

for i in range(steps):
  print(f"paso numero #{i}")

i = 0

while(i < steps):
  i += 1
  print("running")