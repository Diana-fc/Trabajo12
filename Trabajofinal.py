inventario = {}
print(inventario) 

ventas = {sku: 0 for sku in inventario.keys()} 

print(ventas) 

def mostrar_inventario(inventario): 

    print("Inventario de Gifty:") 

    for sku, producto in inventario.items(): 

        print(f"SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")  

mostrar_inventario(inventario) 
def vender_producto(inventario): 

    while True: 

        sku = input("\nIngrese el SKU del producto a vender: \n(Si quiere volver al menú, ingrese 0)\n") 

        if sku == '0': 

            return

        if not sku.isdigit() or len(sku) != 3: print("El SKU debe ser un número de tres dígitos. Ejemplo: 001, 002.")  

        continue

    if sku in inventario: 

        while True: 
            try: 
                cantidad_vendida = int(input(f"Ingrese la cantidad de {inventario[sku]['nombre']} a vender (hay {inventario[sku]['cantidad']}): ")) 

                if cantidad_vendida <= 0: 
                    print("La cantidad debe ser mayor a cero.") 
                    continue 

                if cantidad_vendida <= inventario[sku]['cantidad']: 
                    inventario[sku]['cantidad'] -= cantidad_vendida 
                    ventas[sku] += cantidad_vendida 
                    total_venta = cantidad_vendida * inventario[sku]['precio'] 
                    print(f"Venta exitosa. Total a pagar: ${total_venta:.2f}") 
                    break 
                else: 
                    print("Cantidad insuficiente en inventario.") 
            except ValueError: 
                print("Ingrese un número válido.") 
    else: 
        print("Producto no encontrado.") 

def agregar_producto(inventario): nuevo_sku = str(max([int(sku) for sku in inventario.keys()]) + 1).zfill(3) print(f"\nEl SKU asignado automáticamente es: {nuevo_sku}") nombre = input("Ingrese el nombre del producto: ") 

while True: 
    try: 
        precio = float(input("Ingrese el precio del producto: ")) 
        if precio <= 0: 
            print("El precio debe ser mayor a cero.") 
            continue 
        break 
    except ValueError: 
        print("Ingrese un valor numérico válido.") 
 
while True: 
    try: 
        cantidad = int(input("Ingrese la cantidad del producto: ")) 
        if cantidad <= 0: 
            print("La cantidad debe ser mayor a cero.") 
            continue 
        break 
    except ValueError: 
        print("Ingrese un número entero válido.") 
 
inventario[nuevo_sku] = {"nombre": nombre, "precio": precio, "cantidad": cantidad} 
print(f"Producto {nombre} agregado al inventario con SKU {nuevo_sku}.") 
  

def actualizar_producto(inventario): 
    while True: 
        sku = input("\nIngrese el SKU del producto a actualizar: \n(Si quiere volver al menú, ingrese 0)\n") 
        if sku == '0': 
            return

    if not sku.isdigit() or len(sku) != 3: 
        print("El SKU debe ser un número de tres dígitos. Ejemplo: 001, 002.") 
        continue
 
    if sku not in inventario: 
        print("Producto no encontrado. Ingrese un SKU válido.") 
        continue 
 
    producto = inventario[sku] 
    print(f"\nProducto actual: SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}") 
 
    nombre = input("Ingrese el nuevo nombre del producto: \n(Si quiere dejar el nombre actual presione ENTER)\n") 
    if nombre.strip() == "": 
        nombre = inventario[sku]['nombre'] 
 
    while True: 
        try: 
            precio_input = input("Ingrese el nuevo precio del producto: \n(Si quiere dejar el nombre actual presione ENTER)\n") 
            if precio_input.strip() == "": 
                precio = inventario[sku]['precio'] 
                break 
            precio = float(precio_input) 
            if precio <= 0: 
                print("El precio debe ser mayor a cero.") 
                continue 
            break 
        except ValueError: 
            print("Ingrese un valor numérico válido.") 
 
    while True: 
        try: 
            cantidad_input = input("Ingrese la nueva cantidad del producto: \n(Si quiere dejar la cantidad actual presione ENTER)\n") 
            if cantidad_input.strip() == "": 
                cantidad = inventario[sku]['cantidad'] 
                break 
            cantidad = int(cantidad_input) 
            if cantidad < 0: 
                print("La cantidad no puede ser negativa.") 
                continue 
            break 
        except ValueError: 
            print("Ingrese un número entero válido.") 
 
    inventario[sku] = {"nombre": nombre, "precio": precio, "cantidad": cantidad} 
    print(f"\nProducto {sku} actualizado correctamente.") 
    return 
  

def eliminar_producto(inventario): 
    while True: sku = input("\nIngrese el SKU del producto a eliminar: \n(Si quiere volver al menú, ingrese 0)\n") if sku == '0': return 

    if not sku.isdigit() or len(sku) != 3: 
        print("El SKU debe ser un número de tres dígitos. Ejemplo: 001, 002.") 
        continue 
     
    if sku not in inventario: 
        print("Producto no encontrado. Ingrese un SKU válido.") 
        continue 
     
    producto = inventario[sku] 
    print(f"\nDatos del producto a eliminar: SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}") 
     
    confirmar = input(f"\n¿Está seguro que desea eliminar este producto? (s = sí / n = no): ").lower() 
    if confirmar == 's': 
        del inventario[sku] 
        print(f"Producto {sku} eliminado del inventario.") 
    elif confirmar == 'n': 
        print("Operación cancelada. No se eliminó ningún producto.") 
    else: 
        print("Opción no válida. Por favor ingrese 's' o 'n'.") 
        continue 
     
    while True: 
        otro = input("\n¿Desea eliminar otro producto? (s = sí / n = no): ").lower() 
        if otro == 's': 
            break 
        elif otro == 'n': 
            return 
        else: 
            print("Opción no válida. Por favor ingrese 's' o 'n'.") 
  

def buscar_producto(inventario): 
    while True: print("\n¿Cómo desea buscar el producto?") print("1. Buscar por SKU") print("2. Buscar por nombre") print("0. Volver al menú principal") 

   opcion = input("Seleccione una opción: ") 
 
    if opcion == '0': 
        return 
 
    elif opcion == '1': 
        while True: 
            sku = input("\nIngrese el SKU del producto a buscar: \n(Si quiere volver al menú de búsqueda, ingrese 0)\n") 
            if sku == '0': 
                break 
 
            if not sku.isdigit() or len(sku) != 3: 
                print("El SKU debe ser un número de tres dígitos. Ejemplo: 001, 002.") 
                continue 
 
            if sku in inventario: 
                producto = inventario[sku] 
                print(f"\nProducto encontrado: SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}") 
            else: 
                print("Producto no encontrado.") 
             
            while True: 
                otra_busqueda = input("\n¿Desea buscar otro producto por SKU? (s = sí / n = no): ").lower() 
                if otra_busqueda == 's': 
                    break 
                elif otra_busqueda == 'n': 
                    break 
                else: 
                    print("Opción no válida. Ingrese 's' o 'n'.") 
            if otra_busqueda == 'n': 
                break 
 
    elif opcion == '2': 
        while True: 
            nombre_buscar = input("\nIngrese el nombre del producto a buscar: \n(Si quiere volver al menú de búsqueda, ingrese 0)\n").lower().strip() 
             
            if nombre_buscar == '0': 
                break 
 
            if nombre_buscar == "": 
                print("Debe ingresar un nombre válido.") 
                continue 
 
            encontrados = [] 
            for sku, producto in inventario.items(): 
                if nombre_buscar in producto['nombre'].lower(): 
                    encontrados.append((sku, producto)) 
 
            if encontrados: 
                print("\nProductos encontrados:") 
                for sku, producto in encontrados: 
                    print(f"SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}") 
            else: 
                print("No se encontraron productos con ese nombre.") 
 
            while True: 
                otra_busqueda = input("\n¿Desea buscar otro producto por nombre? (s = sí / n = no): ").lower() 
                if otra_busqueda == 's': 
                    break 
                elif otra_busqueda == 'n': 
                    break 
                else: 
                    print("Opción no válida. Ingrese 's' o 'n'.") 
            if otra_busqueda == 'n': 
                break 
 
    else: 
        print("Opción no válida. Por favor seleccione 1, 2 o 0.") 
  

def generar_reporte(inventario): print("\n--- Reporte Completo del Inventario ---") 

total_productos = sum(producto['cantidad'] for producto in inventario.values()) 
print(f"Total de productos en inventario: {total_productos}") 
 
print("\nProductos más vendidos:") 
ventas_ordenadas = sorted(ventas.items(), key=lambda x: x[1], reverse=True) 
 
productos_con_ventas = False 
for sku, cantidad_vendida in ventas_ordenadas: 
    if cantidad_vendida > 0: 
        producto = inventario[sku] 
        print(f"SKU: {sku}, Nombre: {producto['nombre']}, Vendidos: {cantidad_vendida}") 
        productos_con_ventas = True 
 
if not productos_con_ventas: 
    print("Aún no se han registrado ventas.") 
 
print("\nProductos con stock bajo (menos de 10 unidades):") 
stock_bajo = False 
for sku, producto in inventario.items(): 
    if producto['cantidad'] < 10: 
        print(f"SKU: {sku}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}") 
        stock_bajo = True 
 
if not stock_bajo: 
    print("No hay productos con stock bajo actualmente.") 
  

def gestion_tienda(inventario): while True: print("\n-------------------------------------------------") print("Bienvenido a la aplicación de inventario de Gifty") print("-------------------------------------------------") print("1. Mostrar inventario") print("2. Vender producto") print("3. Agregar producto") print("4. Actualizar producto") print("5. Eliminar producto") print("6. Buscar producto") print("7. Reporte de ventas") print("8. Salir") 

   opcion = input("Seleccione una opción: ") 
 
    if opcion == '1': 
        mostrar_inventario(inventario) 
    elif opcion == '2': 
        vender_producto(inventario) 
    elif opcion == '3': 
        agregar_producto(inventario) 
    elif opcion == '4': 
        actualizar_producto(inventario) 
    elif opcion == '5': 
        eliminar_producto(inventario) 
    elif opcion == '6': 
        buscar_producto(inventario) 
    elif opcion == '7': 
        generar_reporte(inventario) 
    elif opcion == '8': 
        break 
    else: 
        print("Opción no válida. Intente nuevamente.") 
  

gestion_tienda(inventario) 

 

 