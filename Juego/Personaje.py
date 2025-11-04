import random

class Personaje:
    def __init__(self, nombre):
        self._nombre = nombre
        self._es_impostor = False
        self._comportamientos_dia = []

    def get_nombre(self):
        return self._nombre

    def es_impostor(self):
        return self._es_impostor

    def set_impostor(self, valor):
        self._es_impostor = valor

    def agregar_comportamiento(self, comportamiento):
        self._comportamientos_dia.append(comportamiento)

    def get_ultimo_comportamiento(self):
        return self._comportamientos_dia[-1] if self._comportamientos_dia else "No hay registro"

    def declarar_dia(self, pistas_encontradas, ubicacion_investigada):
        if self._es_impostor:
            return self._declarar_impostor(pistas_encontradas, ubicacion_investigada)
        else:
            return self._declarar_paciente_normal(pistas_encontradas, ubicacion_investigada)

    def _declarar_impostor(self, pistas, ubicacion):
        declaraciones = [
            f"Estuve en {ubicacion} haciendo mis ejercicios de relajación",
            f"Pasé el día en {ubicacion} meditando sobre mi recuperación",
            f"En {ubicacion} practiqué mis técnicas de control mental",
            f"Dediqué el día en {ubicacion} a organizar mis pensamientos"
        ]
        if any("labial" in pista.lower() for pista in pistas):
            declaraciones.extend([
                f"En {ubicacion} noté que alguien había estado maquillándose",
                f"Vi algo rojo en {ubicacion} pero no le presté atención"
            ])
        if any("reloj" in pista.lower() for pista in pistas):
            declaraciones.extend([
                f"En {ubicacion} me fijé en la hora frecuentemente",
                f"El tiempo pasa lento aquí, lo noté en {ubicacion}"
            ])
        if any("llave" in pista.lower() for pista in pistas):
            declaraciones.extend([
                f"En {ubicacion} pensé en lo importante que son las cerraduras",
                f"{ubicacion} me recordó que debemos mantener todo seguro"
            ])
        return random.choice(declaraciones)

    def _declarar_paciente_normal(self, pistas, ubicacion):
        declaraciones = [
            f"Estuve en {ubicacion} viendo la televisión",
            f"En {ubicacion} conversé con otros pacientes",
            f"Pasé el día en {ubicacion} leyendo revistas",
            f"En {ubicacion} ayudé a ordenar algunas cosas",
            f"Dediqué la tarde en {ubicacion} a escribir en mi diario",
            f"En {ubicacion} participé en actividades grupales"
        ]
        if any("labial" in pista.lower() for pista in pistas):
            declaraciones.extend([
                f"En {ubicacion} noté que había cosas de maquillaje",
                f"Vi colores llamativos en {ubicacion} durante el día"
            ])
        return random.choice(declaraciones)

    def interrogar(self, pistas_encontradas):
        if self._es_impostor:
            respuestas = [
                "No recuerdo nada fuera de lo normal hoy",
                "Estuve concentrado en mi terapia todo el día",
                "Solo hice lo que normalmente hacemos aquí",
                "Me sentí un poco ansioso pero es normal en mi condición"
            ]
            if any("labial" in pista.lower() for pista in pistas_encontradas):
                respuestas.extend([
                    "¿Maquillaje? No, yo no uso esas cosas",
                    "No sé nada sobre productos de belleza"
                ])
            if any("reloj" in pista.lower() for pista in pistas_encontradas):
                respuestas.extend([
                    "Siempre pierdo la noción del tiempo aquí",
                    "Los relojes me ponen nervioso, evito mirarlos"
                ])
        else:
            respuestas = [
                "Hoy fue un día como cualquier otro",
                "Me sentí bastante bien durante el día",
                "Participé en todas las actividades programadas",
                "Conversé con varios compañeros hoy",
                "Estuve un poco distraído pero nada grave"
            ]
            if any("labial" in pista.lower() for pista in pistas_encontradas):
                respuestas.extend([
                    "Vi a alguien con las manos manchadas hoy",
                    "Noté un olor peculiar en el aire"
                ])
        return random.choice(respuestas)

