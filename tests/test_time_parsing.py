import pytest
from features.steps.belly_steps import parse_time_description

def test_parse_time_description():
    assert parse_time_description("1 hora") == 1.0
    assert parse_time_description("30 minutos") == 0.5
    assert parse_time_description("3600 segundos") == 1.0
    assert parse_time_description("1 hora y 30 minutos") == 1.5
    assert parse_time_description("90 minutos") == 1.5
    assert parse_time_description("1 hora, 30 minutos y 45 segundos") == pytest.approx(1.5125, 0.001)
    assert parse_time_description("media hora") == 0.5
    assert parse_time_description("dos horas") == 2.0
    assert parse_time_description("cincuenta minutos") == 50 / 60
    assert parse_time_description("veinte segundos") == 20 / 3600

def test_invalid_time_description():
    with pytest.raises(ValueError):
        parse_time_description("invalid description")