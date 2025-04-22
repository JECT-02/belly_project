from datetime import datetime
from features.steps.belly_steps import parse_time_description
from src.clock import Clock

class Belly:
    MIN_CUCUMBERS = 10
    MIN_WAIT_HOURS = 1.5

    def __init__(self, clock_service=None):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0
        self.clock_service = clock_service or Clock()
        self.last_meal_time = None

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0
        self.last_meal_time = None

    def comer(self, pepinos):
        if not isinstance(pepinos, (int, float)):
            raise ValueError("La cantidad de pepinos debe ser un número.")
        if pepinos < 0:
            raise ValueError("La cantidad de pepinos no puede ser negativa.")
        if pepinos > 10000:
            raise ValueError("No se pueden comer más de 10000 pepinos.")
        self.pepinos_comidos += pepinos
        self.last_meal_time = self.clock_service.get_current_time()

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
        return self.pepinos_comidos > self.MIN_CUCUMBERS and self.tiempo_esperado >= self.MIN_WAIT_HOURS

    def pepinos_comidos(self):
        return self.pepinos_comidos

    def predecir_gruñido(self, cant_pepinos, tiempo):
        if not isinstance(cant_pepinos, (int, float)):
            raise ValueError("La cantidad de pepinos debe ser un número.")
        if cant_pepinos < 0:
            raise ValueError("La cantidad de pepinos no puede ser negativa.")
        if cant_pepinos > 10000:
            raise ValueError("No se pueden comer más de 10000 pepinos.")
        if tiempo < 0:
            raise ValueError("El tiempo de espera no puede ser negativo.")
        if tiempo > 100000:
            raise ValueError("El tiempo de espera no puede exceder 100000 horas.")
        return cant_pepinos > self.MIN_CUCUMBERS and tiempo >= self.MIN_WAIT_HOURS

    def pepinos_faltantes(self):
        if self.tiempo_esperado < self.MIN_WAIT_HOURS or self.esta_gruñendo():
            return 0
        return max(0, self.MIN_CUCUMBERS + 1 - self.pepinos_comidos)

    def tiempo_transcurrido(self):
        if self.last_meal_time is None:
            return 0
        current_time = self.clock_service.get_current_time()
        elapsed_seconds = (current_time - self.last_meal_time).total_seconds()
        return elapsed_seconds / 3600  # Convertir a horas