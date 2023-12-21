


"""
    Range é uma função built-in do PY, é usada para produzir uma sequncia de números inteiros a partir de um ínicio (Inclusivo) para um fim (Exclusivo). Se usarmos range (i,j) será produzido:
    i, i+1, i+2, i+3, ..., j-1.
ele recebe 3 argumentos: stop (obrigatorio), start (opcional) e step (opcional)



    """

range = (4)

list(range(0,4))



for numero in range (0, 11):
    print(numero, end=" ")


# exemplo da tabuada do 5
                # 0 = start / 51 = Stop / 5 = Step 
    
for numero in range(0, 51, 5):
    print(numero, and=" ")