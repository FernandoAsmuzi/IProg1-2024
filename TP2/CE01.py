nota = float(input('Ingrese nota: '))
print('Seleccione turno: ')
print('Presione 1 para diurno')
print('Presione 2 para vespertino')
turno = int(input('Su selección: '))

if(nota >= 3.5):
    if(turno == 1):
        resul = 'Rinde examen'
    elif(turno == 2):
        if(nota >= 6):
            resul = 'Se exime'
        else:
            resul = 'Rinde examen'
else:
        resul = 'Reprueba'

print(f'Estado del alumno: {resul}')