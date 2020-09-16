# 
# Dado un numero n, imprimir los primeros n numeros de la serie de fibonacci
#

n = int(input("Ingrese un numero: "))

ant1 = 0
ant2 = 0
actual = 1

print("Los primeros ",n, " numeros de la serie de fibonacci: ")

for x in range(1,n+1):
  print(actual)
  ant1 = ant2
  ant2 = actual
  actual=ant1+ant2
