
cond= "si"
suma=0
i=1
while cond == "si":
    productos=input("ingrese el nombre del producto " + str(i) + ("= ") )
    precio=int(input("ingrese el precio del producto " + str(i) + ("= ") ))
    suma = suma + precio 
    total= suma
    valordeliva= total*0.19
    totalconiva= valordeliva+total
    cond=input("¿quieres agregar otro producto?, no, si = ")
    i=i+1
print("el valor original de la compra es = " , total , str("pesos colombianos"))
print("el valor del iva es = " , valordeliva , str("pesos colombianos"))
print("el valor total de la compra con iva es = " , totalconiva , str("pesos colombianos"))
if totalconiva > 150000:
    descuent= totalconiva*0.05
    descuento= totalconiva-descuent
    print("el descuyento es de", descuent)
    print ("el valor total con el descuento es ",descuento)
