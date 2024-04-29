peso = float(input('Ingrese peso en kg: '))
altura = float(input('Ingrese altura en metros: '))

imc = round(peso/(altura**2), 3)

print(f'El indice de masa corporal es {imc}')