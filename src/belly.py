from features.steps.belly_steps import parse_time_description

class Belly:
    def __init__(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        if pepinos < 0:
            raise ValueError("La cantidad de pepinos no puede ser negativa.")
        print(f"He comido {pepinos} pepinos.")
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        try:
            # Intentar convertir directamente a float
            tiempo_en_horas = float(tiempo_en_horas)
        except ValueError:
            # Si falla, usar parse_time_description para interpretar la entrada
            tiempo_en_horas = parse_time_description(tiempo_en_horas)
        if tiempo_en_horas > 0:
            self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        if self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10:
            return True
        return False