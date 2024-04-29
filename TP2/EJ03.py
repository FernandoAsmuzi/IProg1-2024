clave = "iprog1"
contraseña = input("Introduce la contraseña: ")
contraseña = contraseña.lower()
if clave == contraseña:
    print("La contraseña coincide")
else:
    print("La contraseña NO coincide")


# ●¿Cuándo se visualizará en la pantalla el mensaje “coincide”?
    # cuando el valor ingresado en la variable 'contraseña' sea 'iprog1'
# ●Si ingresa en la variable contraseña iProg1, ¿Qué mensaje se verá en la pantalla?
    # el mensaje que se verá es "La contraseña NO coincide"
# ●Mejore la sentencia en la línea 3 utilizando alguna función que salve la situación anterior.
    # se introdujo la línea con el código 'contraseña = contraseña.lower()'
# ●¿Qué sucede si ingresa un número?
    # muestra el mensaje "La contraseña NO coincide"
