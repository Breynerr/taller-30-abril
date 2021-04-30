#cuantos billetes tengo
cantidad=int(input("ingrese la cantidad de dinero = "))
if cantidad >= 100000:
    bill1=cantidad//100000
    print("tiene", bill1 ,"billetes de cien mil pesos")
    cantidad = cantidad  %100000
if cantidad >= 50000:
    bill2=cantidad//50000
    print("tiene", bill2 ,"billetes de cicuenta mil pesos")
    cantidad = cantidad%50000
if cantidad >= 20000:
    bill3=cantidad//20000
    print("tiene", bill3 ,"billetes de veinte mil pesos")
    cantidad = cantidad%20000
if cantidad >= 5000:
    bill4=cantidad//5000
    print("tiene", bill4 ,"billetes de cinco mil pesos")
    cantidad = cantidad%5000
if cantidad >= 1000:
    bill5=cantidad//1000
    print("tiene", bill5 ,"billetes  mil pesos")
    cantidad = cantidad%1000
if cantidad >= 100:
    bill6=cantidad//100
    print("tiene", bill6 ,"monedas de cien pesos")
    cantidad = cantidad%100
if cantidad >= 1:
    bill7=cantidad//1
    print("tiene", bill7 ,"monedas de un peso")
    cantidad = cantidad%1






