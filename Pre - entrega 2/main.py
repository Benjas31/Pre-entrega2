from paquete.cliente import *
from paquete.basedatos import *

cliente_1 = Cliente("Benja", 20, "benja@coder.com", "Argentina")
cliente_2 = Cliente("Manuel", 43, "nahuel@coder.com", "Perú")
cliente_3 = Cliente("Zoe", 23, "zoe@coder.com", "Alemania")

print(cliente_1)
cliente_1.ver_compras()

print("*" * 50)

cliente_1.comprar("Maletin", 100)
cliente_2.comprar("Maletin2", 200)
cliente_3.comprar("Maletin3", 300)
cliente_1.comprar("Paraguas", 1000)

bd = BaseDatos()

bd.registrar_compras(cliente_1)
bd.registrar_compras(cliente_2)
bd.registrar_compras(cliente_3)

print("*" * 50)

cliente_1.ver_compras()
cliente_2.ver_compras()
cliente_3.ver_compras()