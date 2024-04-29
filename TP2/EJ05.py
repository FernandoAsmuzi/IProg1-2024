a = int(input('Ingrese primer numero: '))
b = int(input('Ingrese segundo numero: '))
c = int(input('Ingrese tercer numero: '))

if(a>b and b>c):
    print('Orden decreciente')
elif(a<b and b<c):
    print('Orden creciente')
else:
    print('No estan en orden')
    