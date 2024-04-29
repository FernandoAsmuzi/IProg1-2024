salario = float(input('Ingrese salario: '))
promedio = 0.04

primero = round(salario + salario * promedio, 2)
segundo = round(primero + primero * promedio, 2)
tercero = round(segundo + segundo * promedio, 2)

print(f'CANTIDAD DE DINERO: {salario}')
print('AHORRO')
print(f'Primero: {primero}')
print(f'Segundo: {segundo}')
print(f'Tercero: {tercero}')