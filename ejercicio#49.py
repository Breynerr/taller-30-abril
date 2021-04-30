#suma y promedio de 10 numeros
i = 1
suma=0
contador=0
while i<=10:
    numero = int(input(" ingresen un numero " + str(i) + "= "))
    if numero >= 0:
        i += 1
        suma= suma+numero
    else:
        print("Numero invalido")
promedio=suma/10
print("la suma es =", suma)
print("el promedio es =", promedio)