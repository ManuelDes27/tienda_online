"""Crea una clase "Producto" con atributos como nombre, precio y cantidad en 
stock. Luego, crea una clase "Tienda" que contenga una lista de productos 
disponibles y métodos para agregar productos, mostrar el inventario y 
realizar una compra."""

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Tienda:
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)

    def mostrar_inventario(self):
        if not self.lista_productos:
            print("\nNo hay productos en el inventario.\n")
        else:
            print("\n--- Inventario de la tienda ---")
            for producto in self.lista_productos:
                print(f"{producto.nombre} - Precio: {producto.precio} - Cantidad: {producto.cantidad}")
        print()

    def realizar_compra(self, nombre_producto, cantidad):
        for producto in self.lista_productos:
            if producto.nombre.lower() == nombre_producto.lower():
                if producto.cantidad >= cantidad:
                    total = producto.precio * cantidad
                    producto.cantidad == cantidad
                    print(f"Compra realizada: {cantidad} x {producto.nombre} = {total:.2f} €\n")
                    return
                else:
                    print("No hay stock disponible.\n")
                    return
        print("Producto no encontrado.\n")

tienda = Tienda()

while True:
    print("1 - Agregar producto")
    print("2 - Mostrar inventario")
    print("3 - Realizar compra")
    print("4 - Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        nombre = input("Introduce el nombre del producto: ")
        try:
            precio = float(input("Introduce el precio del producto: "))
            cantidad = int(input("Cantidad en stock: "))
            nuevo_producto = Producto(nombre, precio, cantidad)
            tienda.agregar_producto(nuevo_producto)
            print("Producto agregado con éxito.")
        except ValueError:
            print("Error. Introduce un número válido para precio y cantidad.\n")
    elif opcion == "2":
        tienda.mostrar_inventario()
    elif opcion == "3":
        nombre = input("Introduce el nombre del producto que quieres comprar: ")
        try:
            cantidad = int(input("Introduce la cantidad que quieres comprar: "))
            tienda.realizar_compra(nombre, cantidad)
        except ValueError:
            print("Error, cantidad no válida.\n")
    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida, intenta de nuevo.\n")
