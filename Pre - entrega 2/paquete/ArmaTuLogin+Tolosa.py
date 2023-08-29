basedatos = {}

def registrar(basedatos):
  usuario = input("Ingrese su nombre de usuario: ")
  contraseña = input("Ingrese su contraseña: ")
  basedatos[usuario] = contraseña
  print("Usted se ha registrado exitosamente!")

def leerbase(basedatos):
  if basedatos == {}:
    print("No hay nada almacenado")
  else:
    print("Las credenciales almacenadas son:")
    for i in basedatos:
      print("Usuario:", i , "Contraseña:", basedatos[i])

def entrar(basedatos):
  usuario = input("Ingrese su nombre de usuario: ")
  contraseña = input("Ingrese su contraseña: ")
  if usuario not in basedatos:
    print("El usuario no se encuentra registrado")
    return
  else:
    chequeo_password = basedatos[usuario]
    if chequeo_password == contraseña:
      print("Ha ingresado!\nBienvenido/a " + usuario)
    else:
      print("Contraseña incorrecta")
