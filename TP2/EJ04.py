edad = int(input('Ingrese edad: '))
cant = int(input('Ingrese cantidad de finchas: '))
FICHA = 35

if (edad < 4 or edad >= 10):
    print('No se permite el ingreso')
else:
    if (edad >= 4 and edad < 7):
        precio = (FICHA * 0.8) * (cant + 5)
        print(f'El precio es: {precio}')
    elif(edad >= 7 and edad < 10):
        precio = FICHA * 1.15 * cant
        print(f'El precio es: {precio}')
        
