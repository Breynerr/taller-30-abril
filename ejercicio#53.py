#cuantos numero hay menores a 100 y cuantos mayores a 100
suma=0
suma2=0
i=1
n=int(input("ingrese la cantidad de numeros que quiere digitar = "))
while i<=n:
    numero = int(input(" ingresen un numero " + str(i) + "= "))
    if numero < 100:
        suma= suma+1
    elif numero >100:
        suma2= suma2+1
    i=i+1
print("los numero menores a 100 son = ",suma)
print("los numeros mayores a 100 son = ", suma2)
