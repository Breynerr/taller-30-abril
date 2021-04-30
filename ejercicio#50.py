#suma y promedio de n numeros
i = 1
suma=0
contador=0
n=int(input("ingrese la cantidad de numeros que quiere digitar = "))
while i<=n:
    numero = int(input(" ingresen un numero " + str(i) + "= "))
    if numero >= 0:
        i += 1
        suma= suma+numero
    else:
        print("Numero invalido")
promedio=suma/n
print("la suma es =", suma)
print("el promedio es =", promedio)