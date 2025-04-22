# language: es

Característica: Saber si mi estómago gruñirá después de comer pepinos

  Como usuario que ha comido pepinos,
  Quiero saber si mi estómago va a gruñir después de esperar un tiempo suficiente,
  Para poder tomar una acción.

@spanish
Escenario: Comer suficientes pepinos y esperar el tiempo adecuado
  Dado que he comido 20 pepinos
  Cuando espero 2 horas
  Entonces mi estómago debería gruñir

@spanish
Escenario: Comer pocos pepinos y no esperar suficiente tiempo
  Dado que he comido 5 pepinos
  Cuando espero 1 hora
  Entonces mi estómago no debería gruñir

@spanish
Escenario: Comer suficientes pepinos pero esperar poco tiempo
  Dado que he comido 15 pepinos
  Cuando espero 1 hora
  Entonces mi estómago no debería gruñir

@spanish
Escenario: Comer suficientes pepinos y esperar con formato complejo
  Dado que he comido 25 pepinos
  Cuando espero "1 hora, 30 minutos y 45 segundos"
  Entonces mi estómago debería gruñir

@english
Escenario: Comer suficientes pepinos y esperar en inglés
  Dado que he comido 30 pepinos
  Cuando espero "two hours and thirty minutes"
  Entonces mi estómago debería gruñir

@spanish @random
Escenario: Comer suficientes pepinos y esperar un tiempo aleatorio
  Dado que he comido 20 pepinos
  Cuando espero un tiempo aleatorio entre 1 y 3 horas
  Entonces mi estómago podría gruñir

@spanish
Escenario: Intentar comer una cantidad negativa de pepinos
  Dado que he comido -1 pepinos
  Entonces debería recibir un error que dice "La cantidad de pepinos no puede ser negativa."

@spanish
Escenario: Intentar comer más de 10000 pepinos
  Dado que he comido 10001 pepinos
  Entonces debería recibir un error que dice "No se pueden comer más de 10000 pepinos."

@spanish
Escenario: Intentar esperar un tiempo negativo
  Dado que he comido 20 pepinos
  Cuando espero -1 hora
  Entonces debería recibir un error que dice "El tiempo de espera no puede ser negativo."

@spanish
Escenario: Intentar esperar un tiempo excesivo
  Dado que he comido 20 pepinos
  Cuando espero 100001 horas
  Entonces debería recibir un error que dice "El tiempo de espera no puede exceder 100000 horas."

@spanish
Escenario: comer muchos pepinos y gruñir
  Dado que he comido 42 pepinos
  Cuando espero 2 horas
  Entonces mi estómago debería gruñir

@spanish
Escenario: comer pocos pepinos y no gruñir
  Dado que he comido 10 pepinos
  Cuando espero 2 horas
  Entonces mi estómago no debería gruñir

@spanish
Escenario: comer muchos pepinos y esperar menos de una hora
  Dado que he comido 50 pepinos
  Cuando espero media hora
  Entonces mi estómago no debería gruñir

@spanish
Escenario: comer pepinos y esperar en minutos
  Dado que he comido 30 pepinos
  Cuando espero 90 minutos
  Entonces mi estómago debería gruñir

@spanish
Escenario: comer pepinos y esperar en diferentes formatos
  Dado que he comido 25 pepinos
  Cuando espero 2.5 horas
  Entonces mi estómago debería gruñir

@spanish
Escenario: comer pepinos y esperar con segundos
  Dado que he comido 20 pepinos
  Cuando espero "1 hora 30 minutos 45 segundos"
  Entonces mi estómago debería gruñir

@spanish
Escenario: comer pepinos y esperar con tiempo decimal
  Dado que he comido 15 pepinos
  Cuando espero 0.5 horas
  Entonces mi estómago no debería gruñir

@spanish
Escenario: comer pepinos y esperar con tiempo decimal mayor
  Dado que he comido 15 pepinos
  Cuando espero 2.75 horas
  Entonces mi estómago debería gruñir

@spanish @random
Escenario: comer pepinos y esperar un tiempo aleatorio entre 1 y 3 horas
  Dado que he comido 20 pepinos
  Cuando espero un tiempo aleatorio entre 1 y 3 horas
  Entonces mi estómago podría gruñir

@spanish
Escenario: comer una gran cantidad de pepinos y esperar mucho tiempo
  Dado que he comido 1000 pepinos
  Cuando espero 10 horas
  Entonces mi estómago debería gruñir

@spanish
Escenario: esperar con múltiples separadores y unidades
  Dado que he comido 20 pepinos
  Cuando espero "2 horas, 30 minutos y 15 segundos"
  Entonces mi estómago debería gruñir

@spanish
Escenario: esperar con descripción compleja en español
  Dado que he comido 25 pepinos
  Cuando espero "tres horas y cuarenta y cinco minutos, quince segundos"
  Entonces mi estómago debería gruñir

@spanish
Escenario: esperar con descripción compleja con comas y espacios
  Dado que he comido 30 pepinos
  Cuando espero "1 hora, 20 minutos, 30 segundos"
  Entonces mi estómago no debería gruñir

@spanish
Escenario: Saber cuántos pepinos he comido
  Dado que he comido 15 pepinos
  Entonces debería haber comido 15 pepinos

@spanish
Escenario: Predecir si mi estómago gruñirá tras comer y esperar
  Dado que planeo comer 12 pepinos y esperar 1.5 horas
  Entonces debería predecir que mi estómago gruñirá

@criterio_nuevo @spanish
Escenario: Calcular pepinos faltantes con tiempo suficiente
  Dado que he comido 8 pepinos
  Cuando espero 2 horas
  Y pregunto cuántos pepinos más necesito para gruñir
  Entonces debería decirme que necesito 3 pepinos más

@criterio_nuevo @spanish
Escenario: Calcular pepinos faltantes con tiempo insuficiente
  Dado que he comido 15 pepinos
  Cuando espero 1 hora
  Y pregunto cuántos pepinos más necesito para gruñir
  Entonces debería decirme que necesito 0 pepinos más

@criterio_nuevo @spanish
Escenario: Calcular pepinos faltantes cuando ya gruñe
  Dado que he comido 20 pepinos
  Cuando espero 2 horas
  Y pregunto cuántos pepinos más necesito para gruñir
  Entonces debería decirme que necesito 0 pepinos más

@spanish
Escenario: Verificar tiempo transcurrido desde la última comida
  Dado que he comido 10 pepinos
  Cuando han pasado 2 horas desde la última comida
  Y pregunto cuánto tiempo ha transcurrido
  Entonces debería decirme que han pasado 2 horas

@spanish
Escenario: Intentar esperar con descripción de tiempo inválida
  Dado que he comido 20 pepinos
  Cuando espero "invalido"
  Entonces debería recibir un error que dice "No se pudo interpretar la descripción del tiempo: 'invalido'"

@spanish
Escenario: Intentar esperar con descripción incompleta
  Dado que he comido 20 pepinos
  Cuando espero "2 horas y nada"
  Entonces debería recibir un error que dice "No se pudo interpretar la descripción del tiempo: '2 horas y nada'"

@spanish
Escenario: Parsear tiempo con números en palabras
  Dado que he comido 20 pepinos
  Cuando espero "dos horas y media"
  Entonces mi estómago debería gruñir

@spanish
Escenario: Comer cero pepinos y esperar
  Dado que he comido 0 pepinos
  Cuando espero 2 horas
  Entonces mi estómago no debería gruñir