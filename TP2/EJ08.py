# edad = int(input("Ingrese la edad (0, 110]:"))
# if edad > 0 and edad <= 12:
#     print("Es un niño")
# elif edad >12 and edad <= 18:
#     print("Es un adolescente")
# elif edad >18 and edad <= 80:
#     print("Es un adulto")
# else:
#     print("Es un anciano")

# Las salidas son: 
# para el valor 12 "Es un niño"
# para el valor 18 "Es un adolescente"

numero = int(input('Ingrese un número entero:'))
print('#')
if numero < 0:
    print('negativo')
if numero < 0 and numero >= -10:
    print(numero)
if numero > 0:
    print('positivo')
if numero > 0 and numero >= 10:
    print(numero)
print('#')

# Las salidas son:
#     para el valor -5:
#         '#'
#         'negativo'
#         '-5'
#         '#'
#     para el valor 0:
#         '#'
#         '#'
#     para el valor 10:
#         '#'
#         'positivo'
#         '10'
#         '#'