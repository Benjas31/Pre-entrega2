
class Cliente():

  def __init__(self, nombre, edad, mail, nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.mail = mail
    self.nacionalidad = nacionalidad
    self.regcompras = []

  def comprar(self, objeto, precio):
    self.regcompras.append({"Objeto": objeto, "Costo": precio})

  def ver_compras(self):
    if self.regcompras == []:
      print("No hay ninguna compra registrada!")
    else:
      print(f"Estas son las compras registradas del cliente {self.nombre}")
      for i in self.regcompras:
        print(i)

  def __str__(self):
    return f"El cliente {self.nombre} fue creado exitosamente!"