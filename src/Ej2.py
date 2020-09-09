# 
# Dada una terna de números naturales que representan al día, al mes y al año de una determinada  fecha
# Informarla  como  un  solo  número  natural  de  8  dígitoscon  la  forma(AAAAMMDD).
#

dd = int(input("Ingrese el dia (2 digitos): "))
mm = int(input("Ingrese el mes (2 digitos): "))
yyyy = int(input("Ingrese el año (4 digitos): "))

intdate = (yyyy*10000) + (mm*100) + dd
print("La fecha en formato entero es: ", intdate)
