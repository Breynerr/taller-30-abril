#cantidad de digitos 
numero=int(input("ingrese un numero = "))
if numero < 10 :
    print("el numero tiene ", "1", str("digito"))
if numero >= 10 and numero < 100 :
    print("el numero tiene ", "2", str("digitos"))
if numero >= 100 and numero < 1000 :
    print("el numero tiene ", "3", str("digitos"))
if numero >= 1000 and numero < 10000 :
    print("el numero tiene ", "4", str("digitos"))
if numero >= 10000 and numero < 100000 :
    print("el numero tiene ", "5", str("digitos"))

