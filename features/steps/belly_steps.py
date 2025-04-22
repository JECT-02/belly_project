from behave import given, when, then
import re
import random
from datetime import datetime, timedelta

numeros = {
    "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
    "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
    "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
    "veintiuno": 21, "veintidós": 22, "veintitrés": 23, "veinticuatro": 24,
    "veinticinco": 25, "veintiséis": 26, "veintisiete": 27, "veintiocho": 28,
    "veintinueve": 29, "treinta": 30, "cuarenta": 40, "cincuenta": 50, 
    "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90, "cien": 100,
    "media": 0.5,
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90, "hundred": 100, "half": 0.5
}

def convertir_palabra_a_numero(palabra, original_desc):
    try:
        return float(palabra)
    except ValueError:
        palabra = palabra.lower().strip()
        if palabra in numeros:
            return numeros[palabra]
        
        palabras = palabra.replace('-', ' ').split()
        total = 0
        current = 0
        for p in palabras:
            if p in ["and", "y"]:
                continue
            if p in numeros:
                value = numeros[p]
                if value >= 100:
                    current *= value
                else:
                    current += value
            else:
                # Usamos la descripción original en el mensaje de error
                raise ValueError(f"No se pudo interpretar la descripción del tiempo: '{original_desc.strip('"')}'")
        total += current
        return total

def parse_time_description(desc):
    original = desc
    desc = desc.lower().strip().replace('"', '').replace(',', ' ').replace(' y ', ' ').replace(' and ', ' ')
    desc = re.sub(r'\s+', ' ', desc)
    
    if not re.search(r'(hora|horas|hour|hours|minuto|minutos|minute|minutes|segundo|segundos|second|seconds)', desc):
        raise ValueError(f"No se pudo interpretar la descripción del tiempo: '{original.strip('"')}'")
    
    time_units = {
        "hora": 1, "horas": 1, "hour": 1, "hours": 1,
        "minuto": 1/60, "minutos": 1/60, "minute": 1/60, "minutes": 1/60,
        "segundo": 1/3600, "segundos": 1/3600, "second": 1/3600, "seconds": 1/3600
    }
    
    tokens = desc.split()
    valor_acumulado = []
    total = 0
    ultima_unidad = None
    
    for token in tokens:
        if token in time_units:
            if not valor_acumulado:
                raise ValueError(f"Unidad '{token}' sin valor en '{original.strip('"')}'")
            valor = ' '.join(valor_acumulado)
            cantidad = convertir_palabra_a_numero(valor, original)  # Pasamos la descripción original
            for unit_name, unit_value in time_units.items():
                if token.startswith(unit_name):
                    total += cantidad * unit_value
                    ultima_unidad = unit_name
                    break
            valor_acumulado = []
        else:
            valor_acumulado.append(token)
    
    if valor_acumulado:
        if ultima_unidad:
            valor = ' '.join(valor_acumulado)
            cantidad = convertir_palabra_a_numero(valor, original)  # Pasamos la descripción original
            for unit_name, unit_value in time_units.items():
                if ultima_unidad.startswith(unit_name):
                    total += cantidad * unit_value
                    break
        else:
            raise ValueError(f"Valor sin unidad al final: '{' '.join(valor_acumulado)}' en '{original.strip('"')}'")
    
    if total == 0:
        raise ValueError(f"No se pudo calcular un tiempo válido a partir de: '{original.strip('"')}'")
    
    return total

def generar_tiempo_aleatorio(expresion):
    match = re.match(r'un tiempo aleatorio entre (\d+) y (\d+) horas', expresion.lower().strip())
    if not match:
        raise ValueError(f"No se pudo parsear la expresión: {expresion}")
    lower = int(match.group(1))
    upper = int(match.group(2))
    tiempo_aleatorio = random.uniform(lower, upper)
    print(f"Tiempo aleatorio elegido: {tiempo_aleatorio} horas")
    return tiempo_aleatorio

@given('que he comido {cukes:d} pepinos')
def step_given_eaten(context, cukes):
    try:
        context.belly.comer(cukes)
    except ValueError as e:
        context.error = str(e)

@given('que planeo comer {cukes:d} pepinos y esperar {time_description}')
def step_given_plan(context, cukes, time_description):
    try:
        time_description = time_description.strip()
        try:
            total_time = float(time_description.replace('"', '').replace(',', '.'))
        except ValueError:
            total_time = parse_time_description(time_description)
        context.predicted_cukes = cukes
        context.predicted_time = total_time
    except ValueError as e:
        context.error = str(e)

@when('espero {time_description}')
def step_when_wait(context, time_description):
    time_description = time_description.strip()
    
    if time_description.lower().startswith("un tiempo aleatorio entre"):
        total_time = generar_tiempo_aleatorio(time_description)
    else:
        try:
            total_time = float(time_description.replace('"', '').replace(',', '.'))
        except ValueError:
            try:
                total_time = parse_time_description(time_description)
            except ValueError as e:
                context.error = str(e)  # Guardamos el error para los escenarios
                return
    
    try:
        context.belly.esperar(total_time)
    except ValueError as e:
        context.error = str(e)

@when('han pasado {time_description} desde la última comida')
def step_when_time_passed(context, time_description):
    time_description = time_description.strip()
    try:
        total_time = float(time_description.replace('"', '').replace(',', '.'))
    except ValueError:
        total_time = parse_time_description(time_description)
    
    # Configurar el mock para devolver un tiempo futuro usando context.mock_clock
    base_time = context.belly.last_meal_time
    if base_time is None:
        base_time = datetime(2023, 1, 1, 12, 0, 0)
    context.mock_clock.get_current_time.return_value = base_time + timedelta(hours=total_time)

@when('pregunto cuántos pepinos más necesito para gruñir')
def step_ask_pepinos_faltantes(context):
    context.faltantes = context.belly.pepinos_faltantes()

@when('pregunto cuánto tiempo ha transcurrido')
def step_ask_tiempo_transcurrido(context):
    context.tiempo_transcurrido = context.belly.tiempo_transcurrido()

@then('mi estómago podría gruñir')
def step_then_podria_gruñir(context):
    assert isinstance(context.belly.esta_gruñendo(), bool)

@then('mi estómago debería gruñir')
def step_then_deberia_gruñir(context):
    assert context.belly.esta_gruñendo() is True

@then('mi estómago no debería gruñir')
def step_then_no_deberia_gruñir(context):
    assert context.belly.esta_gruñendo() is False

@then('debería recibir un error que dice "{error_message}"')
def step_then_error(context, error_message):
    assert hasattr(context, 'error')
    assert context.error == error_message

@then('debería haber comido {expected:d} pepinos')
def step_then_pepinos_comidos(context, expected):
    assert context.belly.pepinos_comidos == expected

@then('debería predecir que mi estómago gruñirá')
def step_then_predict_gruñir(context):
    assert context.belly.predecir_gruñido(context.predicted_cukes, context.predicted_time) is True

@then('debería decirme que necesito {expected:d} pepinos más')
def step_then_pepinos_faltantes(context, expected):
    assert context.faltantes == expected

@then('debería decirme que han pasado {expected:g} horas')
def step_then_tiempo_transcurrido(context, expected):
    assert context.tiempo_transcurrido == expected