import random 
minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas=minusculas.upper()
numeros= "1234567890"
simbolos= "`~!@#$%^&*()_-=\/+?<>"
base = minusculas+mayusculas+numeros+simbolos
longitud = 15
cantidad_password = int (input("Ingrese la cantidad de contraseñas que desea crear: "))
for _ in range (cantidad_password):
    muestra = random.sample(base,longitud)
    password = "".join (muestra)
    print (password)