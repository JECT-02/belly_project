from behave import given, when, then
import re

# Diccionario de palabras numéricas
numeros = {
    # Español
    "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
    "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
    "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
    "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
    "ochenta": 80, "noventa": 90, "cien": 100, "media": 0.5,
    # Inglés
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90, "hundred": 100, "half": 0.5
}

def convertir_palabra_a_numero(palabra):
    try:
        return float(palabra)
    except ValueError:
        palabra = palabra.lower()
        if palabra in numeros:
            return numeros[palabra]
        palabras = palabra.split()
        total = 0
        current = 0
        decimal_part = False
        decimal_factor = 0.1
        for p in palabras:
            if p in ["point", "coma", "punto"]:
                decimal_part = True
                continue
            if p in ["and", "y"]:
                continue
            if p in numeros:
                value = numeros[p]
                if decimal_part:
                    total += value * decimal_factor
                    decimal_factor /= 10
                elif value == 100 and current != 0:
                    current *= value
                else:
                    current += value
            else:
                raise ValueError(f"No se pudo convertir la palabra '{palabra}' a número.")
        return total + current

def parse_time_description(desc):
    desc = desc.lower().strip().replace('"', '')
    time_units = {
        "hora": 1, "horas": 1, "hour": 1, "hours": 1,
        "minuto": 1/60, "minutos": 1/60, "minute": 1/60, "minutes": 1/60,
        "segundo": 1/3600, "segundos": 1/3600, "second": 1/3600, "seconds": 1/3600,
    }
    total_hours = 0.0
    # Separar por unidad
    partes = re.split(r'(hora[s]?|hour[s]?|minuto[s]?|minute[s]?|segundo[s]?|second[s]?)', desc)
    i = 0
    while i < len(partes) - 1:
        valor = partes[i].strip()
        unidad = partes[i+1].strip()
        if valor:
            cantidad = convertir_palabra_a_numero(valor)
            total_hours += cantidad * time_units[unidad]
        i += 2
    return total_hours

# PASOS DE TEST

@given('que he comido {cukes:d} pepinos')
def step_given_eaten_cukes(context, cukes):
    context.belly.comer(cukes)

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    try:
        total_time = float(time_description.replace('"', '').replace(',', '.'))
    except ValueError:
        total_time = parse_time_description(time_description)
    context.belly.esperar(total_time)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."