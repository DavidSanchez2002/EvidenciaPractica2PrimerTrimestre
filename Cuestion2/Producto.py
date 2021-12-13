class Producto():
    _nombre=''
    _temporada=''
    _unidades=0
    _precio=0

    def __init__(self,nombre,temporada,unidades,precio):
        self._nombre=nombre
        self._temporada=temporada
        self._unidades=unidades
        self._precio=precio

    def get_nombre(self):
       return self._nombre
    def set_nombre(self,nombre):
       self._nombre=nombre

    def importe(self,unidades,precio=9.95,iva=1.21):
         total=f"El precio + Iva es: {round((unidades*precio)*iva,2)}€" if unidades<self._unidades else "No hay suficientes productos a la venta"
         return total

producto1 = Producto("camisa","primavera",15,9.95)


print(producto1.get_nombre())

producto1.set_nombre("pantalon")

print(producto1.get_nombre())

print(producto1.importe(5))
print(producto1.importe(200))