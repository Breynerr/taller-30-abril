#suma de numeros
suma = 0
con="si"
while con=="si":
    numero=int(input("ingrese un numero el primer numero inclusivo = "))
    numero2=int(input("ingrese un numero exclusivo = "))
    print("los  primeros numeros naturales son:")
    if numero2>numero:
        for n in range(numero,numero2):
          print(n)
          con="no"
          suma= suma+n
    else:
        print("el numero exclusivo ingresado es incorrecto, por favor increse un numero mayor al primer numero ")
        con="si"
print("La suma de los primeros es =", suma)
