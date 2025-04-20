from features.steps.belly_steps import parse_time_description

class Belly:
    def __init__(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        if not isinstance(pepinos, (int, float)):
            raise ValueError("La cantidad de pepinos debe ser un número.")
        if pepinos < 0:
            raise ValueError("La cantidad de pepinos no puede ser negativa.")
        if pepinos > 10000:
            raise ValueError("No se pueden comer más de 10000 pepinos.")
        print(f"He comido {pepinos} pepinos.")
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        try:
            tiempo_en_horas = float(tiempo_en_horas)
        except ValueError:
            tiempo_en_horas = parse_time_description(tiempo_en_horas)
        if tiempo_en_horas < 0:
            raise ValueError("El tiempo de espera no puede ser negativo.")
        if tiempo_en_horas > 100000:
            raise ValueError("El tiempo de espera no puede exceder 100000 horas.")
        self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        return self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10