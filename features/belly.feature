# language: es

Característica: Característica del estómago

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

@english
Escenario: comer pepinos y esperar en inglés
  Dado que he comido 20 pepinos
  Cuando espero "two hours and thirty minutes"
  Entonces mi estómago debería gruñir
