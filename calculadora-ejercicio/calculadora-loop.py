print("Bievenidos a la calculadora.\nPara salir escribe Salir\nLas operaciones son suma, multi, div y resta.")

while True :
    n1 = input("Ingresa el primer número: ")
    operacion = input("Ingresa operación: ")
    
    if (operacion == "salir"):
        break

    n2 = input("Ingresa el segundo número: ")

    n1 = int(n1)
    n2 = int(n2)

    if (operacion == "suma"): 
        suma = n1 + n2
        print(f'el resultado de la suma es {suma}')

    elif (operacion == "multi"): 
        multi = n1 * n2
        print(f'el resultado de la multiplicación es {multi}')

    elif (operacion == "div"): 
        if (n2 == 0 ):
            print(f'no puedes dividir por 0')
        else:
            div = n1 / n2
            print(f'el resultado de la división es {div}')

    elif (operacion == "resta"): 
        resta = n1 - n2
        print(f'el resultado de la resta es {resta}')

    else: 
        print(f'no es posible realizar la operación {operacion}')








#importante no olvidar poner la f antes de las comillas triples y que las variables coincidan con sus nombres dentro del {}

