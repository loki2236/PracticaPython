# 
# Dado un entero m, imprimir un listado de los m primeros multiplos de 3 que no sean multiplos de 5
#

m = int(input("Ingrese un numero entero: "))

print("Los primeros ",m, " numeros multiplos de 3 pero no de 5: ")

x = 1
while (m > 0):
  if((x%3 == 0) and (x%5 != 0)):
    print(x)
    m -= 1
  x += 1
