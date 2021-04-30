#indicar ciertas cantidades
suma=0
suma2=0
suma3=0
suma4=0
suma5=0
i=1
n=int(input("ingrese la cantidad de numeros que quiere digitar = "))
while i<=n:
    numero = int(input(" ingresen un numero " + str(i) + "= "))
    if numero <=0:
        suma= suma+1
    if numero >=0:
        suma2= suma2+1
    if numero%2 ==0:
        suma3=suma3+1
    else:
        suma4=suma4+1
    if numero%8 ==0:
        suma5=suma5+1
    i=i+1
print("los numeros negativos que hay son = ",suma)
print("los numeros positivos que hay son = ", suma2)
print("los numeros pares que hay son = ",suma3)
print("los numeros impares que hay son = ",suma4)
print("los numeros multiplos de 8 que hay son = ",suma5)