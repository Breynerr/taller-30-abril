#mayor_menor
#mayor_menor
i = 1
mayor=0
menor=0
while i<=3:
    numero = int(input(" ingresen un numero " + str(i) + "= "))
    if numero >= 0:
        if numero > 0:
            if numero> mayor:
                mayor =numero 
            if numero < menor or i == 1:
                menor = numero
            i += 1
    else:
        print("Numero invalido")
print("El número MAYOR es el " + str(mayor))
print("El número MENOR es el " + str(menor))