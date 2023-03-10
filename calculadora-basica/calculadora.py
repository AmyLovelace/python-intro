n1 = input("ingresa primer numero")
n2 = input("ingresa segundo numero")

n1 = int(n1)
n2 = int(n2)
print(n1 + n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f""" 
para los número {n1} y {n2},
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multiplicacion es {multi}
el resultado de la división es {div}
"""
#importante no olvidar poner la f antes de las comillas triples y que las variables coincidan con sus nombres dentro del {}

print(mensaje)
