# Dadas v, w, z variables de tipo numérico entero escribir las expresiones lógicas correspondientes a los
# siguientes enunciados:
# A. v es no positivo y w es no menor o igual a cero.
# B. v, w, z son diferentes entre sí.
# C. v es no nulo y w no es mayor a z.
# D. w está estrictamente entre v y z.
# E. v es igual a w o z es no negativo pero no ambos a la vez.

# A. (v < 0) and not (w <= 0)
# B. (v != w) and (v != z) and (w != z)
# C. (v != 0) and (w <= z)
# D. (w > z and w < v) or (w < z and w > v)
# E. (v == w and not(z >= 0)) or (z >= 0 and not(v == w))