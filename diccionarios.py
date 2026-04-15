# frutas = {"manzanas": 10, "bananas": 5}#inicializamos el diccionario con dos cajas de frutas
# frutas["bananas"] = 13 #actualizamos el número de bananas a 13
# frutas["naranjas"] = 7 #agregamos un nuevo tipo de fruta, una nueva caja que tiene como cantidad 7 naranjas
# print(frutas) #imprimimos el diccionario completo
# print(f"Hay {frutas['manzanas']} manzanas en la caja.") #imprimimos la cantidad de manzanas usando su clave

#Fusionar 2 diccionarios
# datos_basicos = {"nombre": "GamerX", "nivel": 15}
# datos_extra = {"puntos": 2500, "nivel": 16}
# datos_perfil = datos_basicos.copy() #creamos una copia del primer diccionario para no modificarlo
# datos_perfil.update(datos_extra) #fusionamos el segundo diccionario en la copia del primero, actualizando el nivel a 16
# print(datos_perfil) #imprimimos el diccionario fusionado, que contiene los datos combinados de ambos diccionarios

#Creamos la ficha tecnica de un influencer usando un diccionario
# campaña_verano = {
#     "cliente": "SuperSoda",
#     "presupuesto": 50000,
#     "redes": ["Instagram", "TikTok"],
#     "objetivo_kpi": "Aumentar seguidores",
#     "finalizada": False
# }
# #Pedimos los datos del cliente usando las claves del diccionario
# print(f"Campaña para el cliente: {campaña_verano['cliente']}")
# #Actualizamos el presupuesto de la campaña
# campaña_verano["presupuesto"] = 60000
# campaña_verano["responsable"] = "Sara"#Agregamos una nueva clave-valor al diccionario para indicar el responsable de la campaña
# print(f"Actualizacion de la campaña: {campaña_verano}")