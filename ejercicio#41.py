#indicar si al menos dos numeros son iguales
numero1 = int(input(" ingrese el numero1 = "))
numero2 = int(input(" ingrese el numero2 = "))
numero3 = int(input(" ingrese el numero3 = "))
if numero1==numero2:
    print("el numero 1 y el son iguales")
elif numero2== numero3:
    print("el numero 2 y el 3 son iguales")
elif numero1== numero3:
    print("el numero 1 y el 3 son iguales ")
else:
    print("no hay numeros iguales")