#parar hasta que hayan 10 numero pares o hasta que hayan 20 numeros 5
suma=0
suma3=0
suma4=0
suma5=0
i="si"
while i=="si":
    numero = int(input(" ingresen un numero = "))
    if numero > 0:
        if numero ==5:
           suma= suma+1
        if suma== 20:
            i="no"
        if numero%2 ==0:
            suma3=suma3+1
            if suma3== 10:
               i="no"
        else:
            suma4=suma4+1
    else:
        print("el numero ingresado es invalido")
        i="si"
print("los numeros 5 que hay son = ",suma)
print("los numeros pares que hay son = ",suma3)
print("los numeros impares que hay son = ",suma4)