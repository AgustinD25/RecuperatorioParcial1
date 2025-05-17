#Recuperatorio Parcial 1
# Listas para almacenar los nombres y las cantidades de los productos
productos = []
cantidades = []

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad en stock: "))
    productos.append(nombre)
    cantidades.append(cantidad)
    print("Producto agregado con éxito.")

def ver_productos_agotados():
    agotados = False
    print("Productos agotados:")
    for i in range(len(productos)):
        if cantidades[i] == 0:
            print(productos[i])
            agotados = True
    if not agotados:
        print("No hay productos agotados.")

def consultar_stock():
    producto = input("Ingrese el nombre del producto a consultar: ")
    if producto in productos:
        index = productos.index(producto)
        # Error conceptual: Sin importar el producto, se muestra siempre el stock del primer producto.
        print(f"El stock de {producto} es: {cantidades[0]}")
    else:
        print("Producto no encontrado.")

def actualizar_stock():
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    if nombre in productos:
        index = productos.index(nombre)
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        # Error intencional: Se usa index+1 en lugar de index, lo que puede causar problemas si el producto está al final
        cantidades[index + 1] = nueva_cantidad  
        print("Stock actualizado.")
    else:
        print("Producto no encontrado.")

def ver_todos_los_productos():
    print("Listado de productos:")
    for i in range(len(productos)):
        # Error corregido: ahora se usa la variable correcta 'cantidades'
        print(f"{productos[i]} - Cantidad: {cantidades[i]}")

def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar producto")
        print("2. Ver productos agotados")
        print("3. Consultar stock de un producto")
        print("4. Actualizar stock")
        print("5. Ver todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_productos_agotados()
        elif opcion == "3":
            consultar_stock()
        elif opcion == "4":
            actualizar_stock()
        elif opcion == "5":
            ver_todos_los_productos()
        elif opcion == "6":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()
