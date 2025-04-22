from behave import fixture, use_fixture
from src.belly import Belly
from unittest.mock import Mock
from datetime import datetime

@fixture
def belly_setup(context, *args, **kwargs):
    # Crear un mock para el clock_service
    mock_clock = Mock()
    base_time = datetime(2023, 1, 1, 12, 0, 0)
    mock_clock.get_current_time.return_value = base_time
    context.belly = Belly(clock_service=mock_clock)
    context.mock_clock = mock_clock  # Guardar el mock para usarlo en los pasos
    yield context.belly
    # Limpiar después del escenario
    context.belly = None
    context.mock_clock = None

def before_scenario(context, scenario):
    use_fixture(belly_setup, context)
"""
# features/environment.py

from unittest.mock import MagicMock
from src.belly import Belly
import time

def before_scenario(context, scenario):
    # Creamos un mock del reloj para poder simular tiempo
    fake_clock = MagicMock()
    # Valor inicial del reloj
    initial_time = 10000.0
    fake_clock.return_value = initial_time
    
    context.current_time = initial_time

    def advance_time(hours):
        # Convierte horas a segundos
        context.current_time += (hours * 3600)
        fake_clock.return_value = context.current_time

    context.advance_time = advance_time

    # Instanciamos Belly con el servicio de reloj mockeado
    context.belly = Belly(clock_service=fake_clock)
    context.exception = None

def after_scenario(context, scenario):
    # Limpieza al final del escenario
    pass

"""
