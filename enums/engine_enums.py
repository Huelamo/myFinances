from enum import Enum

class RegisterHeaders(Enum):
    DATE = 'Fecha'
    CATEGORY = 'Categoria'
    AMOUNT = 'Importe'

class ExpendituresCategories(Enum):
    Hogar = 'hogar'
    Suministros = 'suministros'
    Supermercado = 'supermercado'
    Viajes = 'viajes'
    Transporte = 'transporte'
    Restaurantes = 'restaurantes'
    Ocio = 'ocio'
    Regalos = 'regalos'
    Suscripciones = 'suscripciones'
    Caprichos = 'caprichos'
    Ropa = 'ropa'
    Formacion = 'formacion'
    Salud = 'salud'
    Gato = 'gato'
    Otros = 'otros'

class IncomeCategories(Enum):
    Salario = 'salario'
    Rentas = 'rentas'
    Otros = 'otros'
