"""-------------------------
 Un hombre desea saber cuanto dinero se genera 
 por concepto de intereses sobre la cantidad que 
 tiene en inversion en el banco. El decidira reinvertir
 los intereses siempre y cuando estos excedan a $7000,
 y en ese caso desea saber cuanto dinero tendra finalmente
 en su cuenta.
"""
capf = 0
p_int =input("De intereses: " )
cap   =input("De cantidad: ")
if p_int > 7000:
   capf = cap + p_int
print capf
