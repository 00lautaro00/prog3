class Instrumento:
    def __init__(self, id, precio, tipo):
        self.id = id
        self.precio = precio
        self.tipo = tipo

    def __str__(self):
        return f"ID: {self.id}, Precio: {self.precio}, Tipo: {self.tipo}"


class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []  

    def agregar_instrumento(self, instrumento):
        self.instrumentos.append(instrumento)

    def listar_instrumentos(self):
        for instrumento in self.instrumentos:
            print(instrumento)

    def instrumentos_por_tipo(self, tipo):
        return [inst for inst in self.instrumentos if inst.tipo == tipo]

    def borrar_instrumento(self, id):
        for instrumento in self.instrumentos:
            if instrumento.id == id:
                self.instrumentos.remove(instrumento)
                return True
        return False

    def porc_instrumentos_por_tipo(self):
        total_instrumentos = len(self.instrumentos)
        if total_instrumentos == 0:
            return {"Percusión": 0, "Viento": 0, "Cuerda": 0}

        conteo = {"Percusión": 0, "Viento": 0, "Cuerda": 0}
        for instrumento in self.instrumentos:
            if instrumento.tipo in conteo:
                conteo[instrumento.tipo] += 1

        return {tipo: (cantidad / total_instrumentos) * 100 for tipo, cantidad in conteo.items()}


class Fabrica:
    def __init__(self):
        self.sucursales = []

    def agregar_sucursal(self, sucursal):
        self.sucursales.append(sucursal)

    def obtener_sucursal(self, nombre):
        for sucursal in self.sucursales:
            if sucursal.nombre == nombre:
                return sucursal
        return None

    def listarInstrumentos(self):
        for sucursal in self.sucursales:
            print(f"Sucursal: {sucursal.nombre}")
            sucursal.listar_instrumentos()

    def instrumentosPorTipo(self, tipo):
        resultado = []
        for sucursal in self.sucursales:
            resultado.extend(sucursal.instrumentos_por_tipo(tipo))
        return resultado

    def borrarInstrumento(self, id):
        for sucursal in self.sucursales:
            if sucursal.borrar_instrumento(id):
                print(f"Instrumento con ID {id} eliminado de la sucursal {sucursal.nombre}")
                return True
        print(f"Instrumento con ID {id} no encontrado.")
        return False

    def porcInstrumentosPorTipo(self, nombre_sucursal):
        sucursal = self.obtener_sucursal(nombre_sucursal)
        if sucursal:
            porcentajes = sucursal.porc_instrumentos_por_tipo()
            print(f"Porcentajes de instrumentos por tipo en la sucursal {nombre_sucursal}:")
            for tipo, porcentaje in porcentajes.items():
                print(f"{tipo}: {porcentaje:.2f}%")
        else:
            print(f"Sucursal con nombre {nombre_sucursal} no encontrada.")


fabrica = Fabrica()

sucursal1 = Sucursal("Sucursal Norte")
sucursal2 = Sucursal("Sucursal Sur")

sucursal1.agregar_instrumento(Instrumento("A123", 1000, "Viento"))
sucursal1.agregar_instrumento(Instrumento("B456", 1500, "Percusión"))
sucursal2.agregar_instrumento(Instrumento("C789", 1200, "Cuerda"))

fabrica.agregar_sucursal(sucursal1)
fabrica.agregar_sucursal(sucursal2)

fabrica.listarInstrumentos()

instrumentos_viento = fabrica.instrumentosPorTipo("Viento")
print("\nInstrumentos de tipo Viento:")
for instrumento in instrumentos_viento:
    print(instrumento)

fabrica.borrarInstrumento("B456")

fabrica.porcInstrumentosPorTipo("Sucursal Norte")
