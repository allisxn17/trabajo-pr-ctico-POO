class Ubicacion:
    def __init__(self, nombre, pistas):
        self.nombre = nombre
        self.pistas = pistas
        self.pistas_restantes = pistas.copy()

    def obtener_pista(self):
        if self.pistas_restantes:
            return self.pistas_restantes.pop(0)
        return None

    def tiene_pistas(self):
        return len(self.pistas_restantes) > 0

    def __str__(self):
        pistas_restantes = len(self.pistas_restantes)
        return f"{self.nombre} ({pistas_restantes} pista{'s' if pistas_restantes != 1 else ''})"
