print("Este programa mezcla dos colores.")
print(" r. Rojo a. Azul")
primera = input(" Elija un color (r o a): ")
if primera == "r":
    print(" a. Azul v. Verde")
    segunda = input(" Elija otro color (a o v): ")
    if segunda == "a":
        print("La mezcla de Rojo y Azul producen Magenta.")
    else:
        print("La mezcla de Rojo y Verde producen Amarillo.")
else:
    print(" v. Verde r. Rojo")
    segunda = input(" Elija otro color (v o r): ")
    if segunda == "v":
        print("La mezcla de Azul y Verde producen Cian.")
    else:
        print("La mezcla de Azul y Rojo producen Magenta.")
print("¡Hasta la próxima!")

# Ingresando 'a' y luego 'v' las salidas son las siguientes:
#     "Este programa mezcla dos colores."
#     "r. Rojo a. Azul"
#     " Elija un color (r o a): "
#     "v. Verde r. Rojo"
#     " Elija otro color (v o r): "
#     "La mezcla de Azul y Verde producen Cian."
#     "¡Hasta la próxima!"