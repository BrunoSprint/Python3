"""
Estruturas de Reptição, são utilizadas para repetir um trecho código um determinado número de vezes. Esse número é determinado atráves de uma expressão lógica.

# Exemplo sem Repetição:  Receba um número do teclado e exiba os 2 números seguintes
# a = int(input("Valor Inteiro: ")) //  a += 1  //  a += 1 ...


Comando FOR é usado para percorrer um objesto iterável, faz sentido usar quando sabemoso número exato de vezes que nosso bloco de código deve ser executado.

# Exemplo:
texto = input ("Informe um texto: ")
VOGAIS = " AEIOU "

for letra in texto:
    if letra.upper() in VOGAIS:              "upper converte para MAIUSCULO"
        print(letra, end="")


print() # adiciona uma quebra de linha.

"""

# exemplo de separadorr de vogais.

texto = " "
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, and=" ")

else:
    print()        # Adiciona uma quebra de linha.
    print("executa no final do laço")








































