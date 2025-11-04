class SaltoTemporal:
    def __init__(self):
        self._usado = False
        self._estado_guardado = None

    def guardar_estado(self, juego):
        if not self._usado:
            self._estado_guardado = {
                "dia_actual": juego.dia_actual,
                "pistas": list(juego.pistas_encontradas),
                "ubicaciones": [(u.nombre, list(u.pistas_restantes)) for u in juego.ubicaciones]
            }

    def regresar_en_el_tiempo(self, juego):
        if self._usado or not self._estado_guardado:
            return False
        estado = self._estado_guardado
        juego.dia_actual = estado["dia_actual"]
        juego.pistas_encontradas = estado["pistas"]
        for u in juego.ubicaciones:
            for nombre, pistas_restantes in estado["ubicaciones"]:
                if u.nombre == nombre:
                    u.pistas_restantes = pistas_restantes
        self._usado = True
        return True
