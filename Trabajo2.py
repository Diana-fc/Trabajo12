# Tienda de regalos Gifty inventario y registro de ventas

inventario = {
    "SKU001": {"nombre": "peluche", "precio": 10.0, "cantidad": 50},
    "SKU002": {"nombre": "taza", "precio": 5.0, "cantidad": 100},
    "SKU003": {"nombre": "camiseta", "precio": 15.0, "cantidad": 75},
    "SKU004": {"nombre": "llavero", "precio": 3.0, "cantidad": 200},
    "SKU005": {"nombre": "bufanda", "precio": 20.0, "cantidad": 30},
    "SKU006": {"nombre": "gorro", "precio": 12.0, "cantidad": 40},
    "SKU007": {"nombre": "agenda", "precio": 8.0, "cantidad": 60},
    "SKU008": {"nombre": "correa_hombre", "precio": 25.0, "cantidad": 20},
    "SKU009": {"nombre": "correa_mujer", "precio": 22.0, "cantidad": 25},
    "SKU010": {"nombre": "cuadro_pared", "precio": 30.0, "cantidad": 15},
    "SKU011": {"nombre": "juego_mesa", "precio": 18.0, "cantidad": 10},
    "SKU012": {"nombre": "juego_cartas", "precio": 7.0, "cantidad": 80},
    "SKU013": {"nombre": "rompecabezas", "precio": 14.0, "cantidad": 45},
    "SKU014": {"nombre": "pelota_futbol", "precio": 11.0, "cantidad": 35},
    "SKU015": {"nombre": "pelota_baloncesto", "precio": 13.0, "cantidad": 25},
    "SKU016": {"nombre": "set_tenis", "precio": 16.0, "cantidad": 20},
    "SKU017": {"nombre": "set_pintura", "precio": 9.0, "cantidad": 50},
    "SKU018": {"nombre": "set_jardineria", "precio": 17.0, "cantidad": 30},
    "SKU019": {"nombre": "reloj_hombre", "precio": 40.0, "cantidad": 10},
    "SKU020": {"nombre": "reloj_mujer", "precio": 35.0, "cantidad": 15},
    "SKU021": {"nombre": "mochila", "precio": 28.0, "cantidad": 20},
}

def mostrar_inventario(inventario):
    print("Inventario de Gifty:")
    for sku, producto in inventario.items():
        print(f"SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")

def vender_producto(inventario):
    sku = input("Ingrese el SKU del producto a vender: ")
    if sku in inventario:
        cantidad_vendida = int(input(f"Ingrese la cantidad de {inventario[sku]['nombre']} a vender: "))
        if cantidad_vendida <= inventario[sku]['cantidad']:
            inventario[sku]['cantidad'] -= cantidad_vendida
            total_venta = cantidad_vendida * inventario[sku]['precio']
            print(f"Venta exitosa. Total a pagar: ${total_venta:.2f}")
        else:
            print("Cantidad insuficiente en inventario.")
    else:
        print("Producto no encontrado.")

def agregar_producto(inventario):
    sku = input("Ingrese el SKU del nuevo producto: ")
    if sku in inventario:
    
        print("El SKU ya existe. No se puede agregar el producto, desea actualizarlo?")
        respuesta = input("Ingrese 's' para sí o 'n' para no: ")
        if respuesta.lower() == 's':
            nombre = input("Ingrese el nuevo nombre del producto: ")
            precio = float(input("Ingrese el nuevo precio del producto: "))
            cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            inventario[sku] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    else:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        inventario[sku] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        print(f"Producto {nombre} agregado al inventario.")

def eliminar_producto(inventario):
    sku = input("Ingrese el SKU del producto a eliminar: ")
    if sku in inventario:
        del inventario[sku]
        print("Producto eliminado del inventario.")
    else:
        print("Producto no encontrado.")

def buscar_producto(inventario):
    sku = input("Ingrese el SKU del producto a buscar: ")
    if sku in inventario:
        producto = inventario[sku]
        print(f"Producto encontrado: SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("Producto no encontrado.")    

def gestion_tienda(inventario):
    while True:
        print("\n--- Menú de Gestión de Tienda Gifty ---")
        print("1. Mostrar inventario")
        print("2. Vender producto")
        print("3. Agregar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_inventario(inventario)
        elif opcion == '2':
            vender_producto(inventario)
        elif opcion == '3':
            agregar_producto(inventario)
        elif opcion == '4':
            eliminar_producto(inventario)
        elif opcion == '5':
            buscar_producto(inventario)
        elif opcion == '6':
            print("Saliendo de tienda :)")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

gestion_tienda(inventario)

# pendiente agregar funciones de actualización de precios y cantidad, búsqueda por nombre, y reporte de ventas.
# agregar ubicación de productos en el inventario.# También se puede agregar una función para generar un reporte de ventas al final del día.
# Además, se puede implementar un sistema de autenticación para acceder a las funciones de gestión.
# Se pueden agregar más productos al inventario y mejorar la interfaz de usuario.
# También se puede considerar agregar una base de datos para almacenar el inventario y las ventas de manera persistente.
# Por último, se puede implementar un sistema de notificaciones para alertar sobre productos con bajo inventario o ventas destacadas.
# Esto permitirá una mejor gestión del inventario y una experiencia de usuario más completa.
# Fin del programa


