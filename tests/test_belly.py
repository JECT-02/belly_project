import pytest
from src.belly import Belly
from features.steps.belly_steps import parse_time_description

def test_parse_time_description():
    assert parse_time_description("1 hora") == 1.0
    assert parse_time_description("30 minutos") == 0.5
    assert parse_time_description("3600 segundos") == 1.0
    assert parse_time_description("1 hora y 30 minutos") == 1.5
    assert parse_time_description("90 minutos") == 1.5
    assert parse_time_description("1 hora, 30 minutos y 45 segundos") == pytest.approx(1.5125, 0.001)
    assert parse_time_description("media hora") == 0.5
    assert parse_time_description("2 horas") == 2.0
    assert parse_time_description("50 minutos") == 50 / 60
    assert parse_time_description("20 segundos") == 20 / 3600

def test_parse_time_description_with_english():
    assert parse_time_description("two hours") == 2.0
    assert parse_time_description("thirty minutes") == 0.5
    assert parse_time_description("one hour and fifteen minutes") == 1.25

def test_invalid_time_description():
    with pytest.raises(ValueError):
        parse_time_description("invalid description")

def test_comer_pepinos_fraccionarios():
    belly = Belly()
    belly.comer(2.5)  # Comer 2.5
    assert belly.pepinos_comidos == 2.5

def test_comer_pepinos_negativos():
    belly = Belly()
    with pytest.raises(ValueError, match="La cantidad de pepinos no puede ser negativa."):
        belly.comer(-5)  # Intentar comer -5

def test_comer_mas_de_100_pepinos():
    belly = Belly()
    with pytest.raises(ValueError, match="No se pueden comer más de 100 pepinos."):
        belly.comer(101)  # Intentar comer 101

def test_comer_tipo_no_numerico():
    belly = Belly()
    with pytest.raises(ValueError, match="La cantidad de pepinos debe ser un número."):
        belly.comer("cinco")  # Intentar comer un string