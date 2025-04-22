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
    assert parse_time_description("one hour, thirty minutes and forty-five seconds") == pytest.approx(1.5125, 0.001)

def test_parse_time_description_complex():
    assert parse_time_description("2 horas, 30 minutos y 15 segundos") == pytest.approx(2.504167, 0.001)
    assert parse_time_description("tres horas y cuarenta y cinco minutos, quince segundos") == pytest.approx(3.754167, 0.001)
    assert parse_time_description("1 hora, 20 minutos, 30 segundos") == pytest.approx(1.341667, 0.001)
    assert parse_time_description("dos horas y media") == 2.5

def test_invalid_time_description():
    with pytest.raises(ValueError):
        parse_time_description("invalid description")
    with pytest.raises(ValueError):
        parse_time_description("2 horas y nada")
    with pytest.raises(ValueError):
        parse_time_description("one hour and something")

def test_comer_pepinos_fraccionarios():
    belly = Belly()
    belly.comer(2.5)
    assert belly.pepinos_comidos == 2.5

def test_comer_pepinos_negativos():
    belly = Belly()
    with pytest.raises(ValueError, match="La cantidad de pepinos no puede ser negativa."):
        belly.comer(-5)

def test_comer_mas_de_10000_pepinos():
    belly = Belly()
    with pytest.raises(ValueError, match="No se pueden comer más de 10000 pepinos."):
        belly.comer(10001)

def test_comer_tipo_no_numerico():
    belly = Belly()
    with pytest.raises(ValueError, match="La cantidad de pepinos debe ser un número."):
        belly.comer("cinco")

def test_comer_gran_cantidad_y_esperar_mucho():
    belly = Belly()
    belly.comer(1000)
    belly.esperar(10)
    assert belly.pepinos_comidos == 1000
    assert belly.tiempo_esperado == 10
    assert belly.esta_gruñendo() is True

def test_no_gruñir_con_tiempo_insuficiente():
    belly = Belly()
    belly.comer(30)
    belly.esperar(parse_time_description("1 hora, 20 minutos, 30 segundos"))
    assert belly.pepinos_comidos == 30
    assert belly.tiempo_esperado == pytest.approx(1.341667, 0.001)
    assert belly.esta_gruñendo() is False

def test_stomach_growls_after_many_cucumbers_and_two_hours():
    belly = Belly()
    belly.comer(11)
    belly.esperar(2)
    assert belly.esta_gruñendo() is True

def test_pepinos_comidos():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_comidos == 15