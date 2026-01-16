#Los bucles nos sirven para iterar (repetir) cierto bloque de codigo mientras se favorezca a una "condicion"


#BUCLE FOR
frutas = ["Manzana", "Fresa", "Mora", "Sandía", "Frambuesa"]

for fruta in frutas:
    print (fruta)

for i in range (5): #Aqui se itera del 1 al 4
    print (i)

#BUCLE WHILE
contador = 0

while contador < 6:
    print(contador)
    contador = contador + 1  #tambien se puede poner "contador += 1"
    #Es importante aumentar el contador, de no ser así se crearía un bucle infinito o sin salida 

