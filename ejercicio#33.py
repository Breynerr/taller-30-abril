#año bisiesto
año=int(input("ingrese el año que desee = "))
if año%100 == 0 :
    if año % 400 == 0:
        print("es una año bisiesto")
else:
    print("no es un año bisiesto")