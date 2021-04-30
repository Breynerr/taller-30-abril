#ecuacion cuadratica
a=float(input("ingrese el valor de a = "))
b=float(input("ingrese el valor de b = "))
c=float(input("ingrese el valor de c = "))
discriminante= b**2-4*a*c
if discriminante < 0 :
    print("no tiene soluciones reales")
elif discriminante==0:
    x = -b / (2 *a)
    print ("la solucion unica es x = ",x)
else:
    x1=(-b-(discriminante**0.5))/(2*a)
    x2=(-b+(discriminante**0.5))/(2*a)
    print("tiene dos soluciones reales que son:")
    print("primera solucion = ",x1)
    print("la segunda solucion = ",x2)
