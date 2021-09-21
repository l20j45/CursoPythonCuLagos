descuento = 0
totalManzanas = int(input("Ingresa el total de manzanas: "))
costoManzanas = int(input("Ingresa el costo de manzanas: "))
costoTotal = totalManzanas * costoManzanas
if totalManzanas == 18:
    print("aplicaste el descuento secreto")
    costoTotal = costoTotal-(costoTotal*.15)
elif totalManzanas >= 10:
    print("aplicaste el descuento")
    costoTotal = costoTotal-(costoTotal*.10)
else :
    print("sin descuento")
print("Costo " + str(costoTotal))