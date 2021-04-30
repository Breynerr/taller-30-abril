#un número decimal e imprima su parte entera y su parte decimal por aparte
numero=float(input("ingrese un numero = "))
numeroentero= numero//1
numerodecimal= numero - numeroentero
print("el numero entero es = ", numeroentero)
print("el numero decimal es = ", numerodecimal)