usuarios = {'Marcela', 'David', 'Elvira', 'Juan', 'Marcos'}
administradores = {'Juan', 'Marcela'}
administradores.discard('Juan')
administradores.add('Juan')
print(administradores)

for user in usuarios: 
    if(user in administradores):
        print('user admin '+ user)
    else:
     print(user)
        