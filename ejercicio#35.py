#usuario y contraseña
con="si"
pregunt=str(input("necesitas crear una cuenta primero ¿quieres hacerlo? = "))
if pregunt == "si":
    usuario=input("crea un usuario = ")
    contraseña=input("crea una contraseña = ")
    print("cuenta creada...")
    print("iniciando sesion....")
    while con == "si":
        usuario1=input("ingrese su usuario = ")
        contraseña1=input("ingrese su contraseña= ")
        if usuario==usuario1:
            if contraseña==contraseña1:
                print("ha inicado sesion senor/@",usuario)
                con="no"
        else:
            print("usuario o contraseña incorrecta")
            con="si"    
else:
    print("necesitas crear primero una cuenta. cuelve pronto....")