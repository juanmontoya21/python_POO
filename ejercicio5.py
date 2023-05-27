class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_total(self, cantidad):
        return self.precio * cantidad


class ProductoDescuento(Producto):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self.descuento = descuento

    def calcular_total(self, cantidad):
        precio_descuento = self.precio - (self.precio * self.descuento)
        return precio_descuento * cantidad


def mostrar_informacion(producto, cantidad):
    print("Nombre: ", producto.nombre)
    print("Precio unitario: $", producto.precio)
    print("Cantidad: ", cantidad)
    print("Total a pagar: $", producto.calcular_total(cantidad))
    print()


producto1 = Producto("Camisa", 500)
producto2 = ProductoDescuento("Pantalón", 800, 0.2)

mostrar_informacion(producto1, 3)
mostrar_informacion(producto2, 2)
