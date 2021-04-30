#valor del pasaje en avion
distancia=int(input("ingrese la distancia del recorrido en km (la distancia minima es de 20 km)= "))
estadia=int(input("ingrese la cantidad de dias de su estadia = "))
cantidadacobrar= distancia*5000
if cantidadacobrar>= 100000:
    print("el valor del pasaje es = ",cantidadacobrar, str("dolares"))
else:
    print("la distancia minima es de 20 km")
if distancia > 1000 and estadia > 7:
    descuento1=cantidadacobrar*0.15
    descuento2=cantidadacobrar-descuento1
    print("------------------------------------------------------------------------------------------")
    print("se le hizo hizo un descuento de = ",descuento1, str("dolares"))
    print("se le hizo hizo un descuento y el valor total es = ",descuento2, str("dolares"))
