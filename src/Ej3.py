# 
# Dada  un  numero  entero  de  la  forma  (AAAAMMDD),  que  representa  una  fecha valida 
# Mostrar el dia, mes y año que representa. 
#

intdate = int(input("Ingrese la fecha en formato (YYYYMMDD): "))
yyyy = intdate // 10000
mm = (intdate % 10000) // 100
dd = (intdate % 10000) % 100

print("El año es: ", yyyy)
print("El mes es: ", mm)
print("El día es: ", dd)
