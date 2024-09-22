import os
usario_info = {}
listUser = []
bucle = 1
while bucle:
    nombre = input("ingrese nombre: ")
    edad = input("ingrese edad: ")
    direccion = input("ingrese direccion: ")
    telefono = input("ingrese telefono: ")
    usario_info = {
        "nombre": nombre,
        "edad": int(edad),
        "direccion": direccion,
        "telefono": telefono,
    }
    listUser.append(usario_info)
    bucle = int(input("desea agregar otro usuario? 0 para salir"))
os.system('cls')
for list in listUser:
    for clave, valor in list.items():
        print(f"{clave}: {valor}")



