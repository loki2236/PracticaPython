#
# Dado un valor numerico, calcular su factorial
#

valor = int(input("Ingrese un numero entero: "))
fact=1
for x in range(1,valor+1):
  fact=fact*x
print("El factorial es: ", fact)
