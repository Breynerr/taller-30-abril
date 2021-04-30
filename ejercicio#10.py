#calcular el promedio de 3 numeros
i=1
while i<=3:
    numero=int(input("ingrese el numero" + str(i) + " "))
    if i >=0 or i<=3:
        if i==1:
            numero1=numero
        if i==2:
            numero2=numero
        if i==3:
            numero3=numero
        i=i+1
promedio= (numero1+numero2+numero3)/3
print("el promedio es igual = ", promedio)