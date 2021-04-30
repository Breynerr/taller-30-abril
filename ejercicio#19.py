#converit segundos a horas,minutos etccc
segundos=int(input("ingrese los segundos deseados = "))
convertir= segundos//3600
tiempo=segundos%3600
convertir2=tiempo//60
convertir3= segundos%60
print("el resultado es", convertir,":",convertir2, ":", convertir3)