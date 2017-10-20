#-------------------------
"""
Determinar si un alumno aprueba o reprueba un curso,
sabiendo que aprobara si su promedio de 3 calificaciones
es mayor o igual a 70; reprueba en caso contrario.
"""
print("Verificar el promedio de 3 calificaciones")
calif01 = input(" De 1er calificacion ")
calif02 = input(" De 2do calificacion ")
calif03 = input(" De 3er calificacion ")
promedio = (calif01+calif02+calif03) / 3
if promedio >= 70:
    print("Si aprobo con ", promedio)
else:
    print("No aprobo con ", promedio)
