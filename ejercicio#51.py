#promedio de numeros pares e impares
conta=0
i=0
conta1=0
o=0
u=1
n=int(input("ingrese la cantidad de numeros que quiere digitar = "))
while u<=n:
    numero = int(input(" ingresen un numero " + str(u) + "= "))
    if numero % 2 ==0:
        conta=conta+numero
        i=i+1
    else:
        conta1=conta1+numero
        o=o+1
    u=u+1
promedio1= conta/i
promedio2= conta1/o
print("la suma de los numeros pares = ",conta)
print("la suma de los numeros impares = ",conta1)
print("el promedio de los numeros pares es = ",promedio1)
print("el promedio de los numeros impares es = ",promedio2)