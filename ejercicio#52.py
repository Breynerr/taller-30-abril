#ingrese un numero valido
con="si"
while con=="si":
    numero=int(input("ingrese un numero entero positivo = "))
    if numero >= 0:
        print(numero)
        con="no"
    else:
        print("el numero ingresado es incorrecto")
        con="si"
