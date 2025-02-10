# Functions
""" 
1. Funciones Declaradas

def funcName(params?):
    codigo

    
2. Funciones Lambda

lambda params : return

"""

def sumar(a, b):
    return a + b

restar = lambda a, b : a - b


numeros = [1, 2, 3, 4, 5]

# map(funcion, lista )
resultado = list(map(lambda num: num**2, numeros)) # [1, 4, 9, 16, 25]

def cuadrado(num):
    return num**2

resultado2 = list(map(cuadrado, numeros))


resultado3 = list(filter(lambda num: num %  2 == 0, numeros)) 

print(resultado2)
print(resultado3)

# Paramestros Posicionales
def nombre_completo(nombre, apellido):
    return f"{nombre} {apellido}"

print(nombre_completo("John", "Doe")) # John Doe

# Parametros por defecto
def nombre_completo(nombre = "John", apellido="Doe"):
    return f"{nombre} {apellido}"

print(nombre_completo()) # John Doe


# Parametros Keyword:
def nombre_completo(nombre = "John", apellido="Doe"):
    return f"{nombre} {apellido}"

print(nombre_completo(apellido="Doe", nombre="Jane")) # Jane Doe


# Empaquetamiento de Argumentos
def totalizar(*args): # args = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    return sum(args)

print(totalizar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)) # 55


# Empaquetamiento de Argumentos Keyword

def informacion(**kargs):
    print(kargs)
    return f"Nombre: {kargs["nombre"]} {kargs["apellido"]}"


print(informacion(nombre="Luis", apellido="Rodriguez", edad=43))