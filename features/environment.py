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