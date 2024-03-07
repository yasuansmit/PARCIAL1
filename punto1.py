vocal_a = 0
vocal_e = 0
vocal_i = 0
vocal_o = 0
vocal_u = 0
total_vocal = 0
while True:
    user_input = input("Ingresa una letra (a, e, i, o, u) o 'f' para salir: ")
    if user_input == 'f' or "F":
        break
    if user_input == 'a':
        vocal_a += 1
        total_vocal += 1
    elif user_input == 'e':
        vocal_e += 1
        total_vocal += 1
    elif user_input == 'i':
        vocal_i += 1
        total_vocal += 1
    elif user_input == 'o':
        vocal_o += 1
        total_vocal += 1
    elif user_input == 'u':
        vocal_u += 1
        total_vocal += 1
    else:
        print("La letra ingresada no es una vocal.")
print("\nRecuento de vocales:")
print("a: ",vocal_a)
print("e: ",vocal_e)
print("i: ",vocal_i)
print("o: ",vocal_o)
print("u: ",vocal_u)
print("Total de vocales: ",total_vocal)