#-------------------------
"""
En un almacen se hace un 20% de descuento a los 
clientes cuya compra supere los $1000
? Cual sera la cantidad que pagara una persona por
su compra?
"""
compra = input("importe de la compra: ")
descuento = 0
if compra > 1000:
   descuento = compra * 0.20
cantidad = compra - descuento
print(" Descuento = ", descuento)
print(" Importe total = ", cantidad)

