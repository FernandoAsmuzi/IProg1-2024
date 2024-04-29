print('Valores de punto 1')
x1 = float(input('Ingrese x1: '))
y1 = float(input('Ingrese y1: '))
z1 = float(input('Ingrese z1: '))

print('Valores de punto 2')
x2 = float(input('Ingrese x2: '))
y2 = float(input('Ingrese y2: '))
z2 = float(input('Ingrese z2: '))

d = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5

print(f'La distancia entre los puntos es {d}')

