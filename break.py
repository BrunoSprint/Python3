while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    # no caso, quando atingir o numero 10, havera o BREAK a condição de parada.

    print(numero)

for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")







# while True : enquanto verdade, pode criar um laço infinito.
    


# o método de interrupção : KeyboardInterrupt