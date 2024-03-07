celsius_a_f = 9/5
fahrenheit_a_c = 5/9
constante_f = 32

while True:
    print("Selecciona una opción:")
    print("1. Convertir grados Celsius a Fahrenheit")
    print("2. Convertir grados Fahrenheit a Celsius")
    print("3. Finalizar")

    opcion = int(input("Ingresa el número de la opción que quiere "))

    if opcion == 1:
        grados_c = float(input("Ingresa la temperatura en grados Celsiu: "))
        grados_f= grados_c * celsius_a_f + constante_f
        print("La temperatura en grados Fahrenhei es: ",grados_f)
    elif opcion == 2:
        grados_f = float(input("Ingresa la temperatura en grados Fahrenhei: "))
        grados_c= (grados_f - constante_f) * fahrenheit_a_c
        print("La temperatura en grados Celsiu es: ",grados_c)
    elif opcion == 3:
        print("Haz finalizado el programa")
        break
    else:
        print("Opción inválida")

