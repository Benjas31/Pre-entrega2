import json

class BaseDatos:

    def registrar_compras(self, cliente):
        nombre_archivo = f"{cliente.nombre}.json"
        with open(nombre_archivo, "w") as outfile:
            compras_texto = json.dumps(cliente.regcompras)
            outfile.write(compras_texto)
