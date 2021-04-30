#numero invertido 
numero=int(input("ingrese un numero de 4 digitos = "))
if numero> 0:
    num1= numero%10 
    num= numero%100
    num2= num //10
    num3= (numero%1000)//100
    num4 = (numero%10000)//1000
print("el numero inverso es = ",num1,num2,num3,num4)


