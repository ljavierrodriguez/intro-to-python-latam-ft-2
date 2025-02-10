# Loops
""" 

for index in collection
    codigo


while condition:
    codigo

range(start = 1, stop = 11, step = 1) # start = 0, step = 1
    

"""
numeros = [1, 2, 3, 4, 5, 6]

for i in range(1, 11):
    print(i)

for i in range(len(numeros)):
    print(numeros[i])

for numero in numeros:
    print(numero)


indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice+=1 
    #indice = indice + 1 