angulo = float(input('Ingrese angulo en radianes: '))
PI = 3.141592

sexagecimal = round(angulo * 180 / PI, 2)
centesimal = round(angulo * 200 / PI, 2)

print(f'Sexagecimal: {sexagecimal}')
print(f'Centesimal: {centesimal}')