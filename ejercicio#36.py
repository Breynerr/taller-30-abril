cond="no"
while cond == "no":
    numero=int(input("ingrese un numero de 0 a 10 = "))
    if numero>= 0 and numero <= 10:
        if numero == 0:
          print("es el numero cero")
        if numero == 1:
          print("es el numero uno")
        if numero == 2:
          print("es el numero dos")
        if numero == 3:
          print("es el numero tres")
        if numero == 4:
           print("es el numero cuatro")
        if numero == 5:
           print("es el numero cinco")
        if numero == 6:
           print("es el numero seis")
        if numero == 7:
           print("es el numero siete")
        if numero == 8:
           print("es el numero ocho")
        if numero == 9:
           print("es el numero nueve")
        if numero == 10:
           print("es el numero diez")
           cond= "si"
    else:
        print("ingresó un numero incorrecto")
        cond="no"

