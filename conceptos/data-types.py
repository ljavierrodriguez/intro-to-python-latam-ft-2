# Data Types
""" 

String
Int
Float
Boolean

None (undefined, null)
Array:
    List
    Tuples
    Set

Dict

function

"""

nombre = "John"
apellido = 'Doe'
nombre_completo = f"{nombre} {apellido}"

saldo = 1000
temp = -10.5

active = True
open = False

direccion = None
users = None

# List
notas = [1, 2, 3, 4, 5, 6]
numeros = list(1, 2, 3, 4, 5)

# Tuples
status = ('active', 'inactive', 'suspended', 'canceled', 'approved', 'pending')
options = (1, 2, 3, 4)

# Set
frutas = {"Manzana", "Pera", "Uva", "Banana"}
frutas2 = set("Manzana", "Pera", "Uva")

notas[0]
status[0]

# Dict

persona = {
    "nombre": "John",
    "apellido": "Doe"
}

persona["nombre"]
persona["apellido"]

estudiante = dict(nombre="John", apellido="Doe")


def nombre_funcion():
    pass