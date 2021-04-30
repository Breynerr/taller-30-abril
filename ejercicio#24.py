#par positivo, par negativo
numero=int(input("ingrese un numero = "))
if numero >= 0:
    if numero %2==0:
        print("es un numero par  positivo")
    else:
        print("es un numero impar positivo")
if numero <= 0:
    if numero %2==0:
        print("es un numero par  negativo")
    else:
        print("es un numero impar negativo")