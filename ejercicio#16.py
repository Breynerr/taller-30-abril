#calcular la distancia entre dos puntos 
i=1
while i <=2:
    x=int(input("ingrese el valor del punto x" + str(i)+ str ("= ")))
    y=int(input("ingrese el valor del punto y" + str(i)+ str ("=")))
    if x > 0 and y > 0:
        if i >0 or   i <=2:
            if i==1:
                 x1= x
                 y1=y
            if i==2:
                x2=x
                y2=y
            i=i+1
    else:
        print("ingreso un valor incorrecto, vuelva a intentarlo")
distancia= (((x2-x1)**2) + ((y2-y1)**2))**0.5
print("la distancia entre los dos puntos es  = ", distancia)