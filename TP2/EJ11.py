# programa 1
valor = int(input('Ingrese valor: '))

if(valor%2==0):
    if(valor%4==0):
        print('Es múltiplo de 2 y 4')
    else: 
        print('Es múltiplo de 2')
else: 
    print('No es múltiplo de 2')


# programa 2
valor = int(input('Ingrese valor: '))

if(valor%2==0 and valor%4==0):
    print('Es múltiplo de 2 y 4')
elif(valor%2==0 and valor%4!=0):
    print('Es múltiplo de 2')
else:
    print('No es múltiplo de 2')