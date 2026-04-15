frutas = {"manzanas": 10, "bananas": 5}#inicializamos el diccionario con dos cajas de frutas
frutas["bananas"] = 13 #actualizamos el número de bananas a 13
frutas["naranjas"] = 7 #agregamos un nuevo tipo de fruta, una nueva caja que tiene como cantidad 7 naranjas
print(frutas) #imprimimos el diccionario completo
print(f"Hay {frutas['manzanas']} manzanas en la caja.") #imprimimos la cantidad de manzanas usando su clave