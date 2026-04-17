# def gestionar_inventario(inventario_inicial):
#     inventario = inventario_inicial
#     print("Sistema de ventas iniciado")
#     print(f"El inventario contiene {inventario} hamburguesas")

#     while inventario > 0:
#         if inventario <= 10:
#             print(f"Advertencia de inventario: solo quedan {inventario} hamburguesas")

#         num_hamburguesas = int(input("Cuantas hamburguesas quiere el cliente? "))

#         if num_hamburguesas > inventario:
#             print(f"No hay suficientes hamburguesas para satisfacer el pedido. Solo quedan {inventario} hamburguesas")
#         else:
#             inventario -= num_hamburguesas
#             print(f"Pedido de {num_hamburguesas} hamburguesas procesado. Quedan {inventario} hamburguesas en el inventario")

#     print("El inventario se ha agotado. No se pueden procesar más pedidos.")


# gestionar_inventario(100)

def gestionar_inventario():
    print("--- 🍔 BIENVENIDO A BURGER-PYTHON 🍔 ---")
    
    while True: # Bucle de recarga (el restaurante sigue abierto)
        inventario = 100
        print(f"\n[SISTEMA] Inventario recargado. Tienes {inventario} hamburguesas listas.")
        
        # Bucle de ventas (mientras haya stock)
        while inventario > 0:
            if inventario <= 10:
                print("🚨 ¡CUIDADO! Solo quedan", inventario, "hamburguesas.")
            try:
                pedido = int(input("\n¿Cuántas hamburguesas quiere el cliente? "))
                
                if pedido < 0:
                    print("❌ Error: No puedes pedir cantidades negativas.")
                elif pedido > inventario:
                    print(f"❌ No tenemos suficiente. Solo quedan {inventario}.")
                else:
                    inventario -= pedido
                    print(f"✅ Venta exitosa. Quedan {inventario} en stock.")
            except ValueError:
                print("❌ Por favor, ingresa un número válido.")
        # Cuando el inventario llega a 0, salimos del bucle interior y venimos aquí:
        print("\n--- 🛑 EL STOCK SE HA AGOTADO ---")
        respuesta = input("¿Deseas recargar el inventario para seguir vendiendo? (si/no): ").lower()
        
        if respuesta != "si":
            print("Cerrando el sistema. ¡Gracias por usar Burger-Python!")
            break # Rompe el bucle exterior y termina el programa
# Llamamos a la función para empezar
gestionar_inventario()