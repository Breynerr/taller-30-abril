#mayor_menor
i = 1
mayor=0
menor=0
suma=0
while i<=3:
    numero = int(input(" ingresen un numero " + str(i) + "= "))
    if numero >= 0:
        if numero > 0:
            if numero> mayor:
                mayor =numero 
            if numero < menor or i == 1:
                menor = numero
            if i==1:
              numero1= numero
            if i==2:
              numero2= numero
            if i==3:
              numero3= numero
            i += 1
    else:
       print("escribio mal el numero")
suma= numero1+ numero2
if suma> numero3:
    print ("la suma de los dos primeros numeros es mayor al tercer numero ingresado = ")
else:
    print("la suma de los dos primeros numeros es menor al tercer numero  ingresado ")
print("El número MAYOR es el " + str(mayor))
print("El número MENOR es el " + str(menor))
