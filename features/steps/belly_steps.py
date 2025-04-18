from behave import given, when, then
import re

# Diccionario para convertir palabras numéricas a números
numeros = {
    "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
    "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
    "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
    "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
    "ochenta": 80, "noventa": 90, "cien": 100, "media": 0.5
}

def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        palabra = palabra.lower()
        if palabra in numeros:
            return numeros[palabra]
        raise ValueError(f"No se pudo convertir la palabra '{palabra}' a un número.")

def parse_time_description(time_description):
    time_description = time_description.strip('"').lower().replace('y', ' ').replace(',', ' ').strip()
    if time_description == 'media hora':
        return 0.5
    # Expresión regular para capturar horas, minutos y segundos
    pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?')
    match = pattern.fullmatch(time_description)
    if match:
        hours_word = match.group(1)
        minutes_word = match.group(2)
        seconds_word = match.group(3)
        # Convertir palabras a números
        hours = convertir_palabra_a_numero(hours_word or "0")
        minutes = convertir_palabra_a_numero(minutes_word or "0")
        seconds = convertir_palabra_a_numero(seconds_word or "0")
        # Calcular el tiempo total en horas
        total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        return total_time_in_hours
    # Lanzar un error si no se puede interpretar la descripción
    raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

@given('que he comido {cukes:d} pepinos')
def step_given_eaten_cukes(context, cukes):
    context.belly.comer(cukes)

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    total_time_in_hours = parse_time_description(time_description)
    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."