anio = int(input('Ingrese año: '))

if((anio%4==0)):
    if((anio%100==0) and (anio%400==0)):
        print('El año ingresado es bisiesto')
    elif(anio%100!=0):
        print('El año ingresado es bisiesto')
    else:
        print('El año ingresado no es bisiesto')
else:
    print('El año ingresado no es bisiesto')