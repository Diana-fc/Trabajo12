#🛍️ Gifty — Sistema de Inventario y Ventas

Gifty es una aplicación sencilla desarrollada en Python para gestionar el inventario y las ventas de una tienda de regalos. Esta herramienta permite visualizar el inventario, registrar ventas, agregar nuevos productos y mantener organizada la información de stock a través de una interfaz de consola.

#📦 Características
- Visualización completa del inventario
- Registro de ventas con cálculo automático de monto total
- Agregado, eliminación y actualización de productos
- Búsqueda de productos por SKU
- Menú interactivo para gestión continua

#🧠 Estructura del Inventario
El inventario está representado como un diccionario en Python con claves tipo SKU (Stock Keeping Unit), cada una mapeando a un producto con nombre, precio y cantidad disponible.
inventario = {
    "SKU001": {"nombre": "peluche", "precio": 10.0, "cantidad": 50},
    ...
}


#🧰 Funcionalidades Principales
| Función | Descripción | 
| mostrar_inventario() | Muestra todos los productos con sus respectivos detalles | 
| vender_producto() | Permite registrar una venta y descuenta stock | 
| agregar_producto() | Agrega nuevos productos o actualiza existentes | 
| eliminar_producto() | Elimina productos del inventario | 
| buscar_producto() | Muestra información de un producto específico por su SKU | 
| gestion_tienda() | Menú principal para interactuar con el sistema | 


#🔄 Mejoras Futuras
- Actualización de precios y cantidades
- Búsqueda por nombre de producto
- Reportes de ventas diarios
- Registro de ubicación del producto
- Sistema de autenticación
- Persistencia con base de datos
- Notificaciones para inventario bajo o ventas destacadas

#▶️ Cómo ejecutar
- Asegúrate de tener Python 3 instalado.
- Ejecuta el script en tu terminal con:
python tienda_gifty.py


- Navega por el menú para gestionar el inventario.
