n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n+" entre "+m+" da un cociente "+str(int(n)//int(m)) + " y un resto " + str(int(n) % int(m)))


# el resultado para n=2 y m=5 es cociente=0 y resto=2
# no se puede obtener resultado con valor de m=0
# para calcular el resto se utiliza el operador %
# genera un error porque no se puede concatenar 