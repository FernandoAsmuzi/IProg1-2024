edad = int(input('Ingresar edad: '))

if(edad >= 0):
    if(edad >= 0 and edad < 18):
        print('Se trata de un menor de edad')
    else:
        print('Se trata de un mayor de edad')
else:
    print('Error, el número es negativo')