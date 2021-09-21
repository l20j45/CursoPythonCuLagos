decision = "no"
contador = 0
while decision != "si":
    contador = 0
    numero = int(input("De que numero quieres la tabla?: "))
    while contador <= 5 :
        print(str(numero) + " * " + str(contador) + ": "+ str(numero*contador))
        contador = contador + 1
    decision = input("Deseas salir?: ")
print("adios") 