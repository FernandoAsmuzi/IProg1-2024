a = int(input('Ingrese primer numero: '))
b = int(input('Ingrese segundo numero: '))
c = int(input('Ingrese tercer numero: '))

if(a>b and a>c):
    if(b>c):
        print(f'El orden es: {c} {b} {a}')
    else:
        print(f'El orden es: {b} {c} {a}')
elif(b>a and b>c):
    if(a>c):
        print(f'El orden es: {c} {a} {b}')
    else:
        print(f'El orden es: {a} {c} {b}')
elif(c>a and c>b):
    if(a>b):
        print(f'El orden es: {b} {a} {c}')
    else:
        print(f'El orden es: {a} {b} {c}')