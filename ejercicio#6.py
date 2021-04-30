#cinco notas obtenidas
i=1
while i <= 5 :
    nota= float(input("ingrese una nota "+ str(i) + " " ))
    if nota >=0 or nota <= 5:
        if i == 1 :
            notafinal1= nota*0.15
        if i == 2 :
            notafinal2= nota*0.2
        if i == 3 :
            notafinal3= nota*0.15
        if i == 4 :
            notafinal4= nota*0.3
        if i == 5 :
            notafinal5= nota*0.2
        i= 1+i
notaf=(notafinal1+notafinal2+notafinal3+notafinal4+notafinal5)
print("la nota final es = ",notaf)
if notaf >= 3:
    print ("el estudiante aprobo, eres un crack")
else:
    print("el estudiante reprobo, eres debil te falta odio")

        
