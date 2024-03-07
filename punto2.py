numero = int(input("Ingresa un número entero positivo: "))

if numero <= 0:
    print("El número debe ser positivo.")
else:
    i = 1
    while i <= 10:
        resultado = numero * i
        print(numero, "X", i, "=", resultado )
        i += 1