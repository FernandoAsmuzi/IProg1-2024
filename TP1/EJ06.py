cant = float(input('Ingrese cantidad en pesos: '))
dolar = 202.30
euro = 214.30

dolarTotal = round(cant / dolar, 3)
euroTotal = round(cant / euro, 2)

print(f'Cantidad en dolares: {dolarTotal}')
print(f'Cantidad en euros: {euroTotal}')