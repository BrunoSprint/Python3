# Argumetação: etapa1: IF / if-else / elif  etapa2: IF aninhado  etapa3: IF ternário
# A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

# if simples: cria uma etrutura condicional simples,composta por um unico desvio, podemos utilizar a palavra reservada if.
# O comando ira testar a expressão lógica, em caso de verdadeiro as ações presentes no bloco de codigo do if serão executadas.
#exemplo:

saldo = 2000.0
saque = float(input("Informe o valor do Saque: "))

if saldo >= saque:
    print("Realizando Saque!")

else:
    print("Saldo Insuficiente")


# if / else : Estrutura condicionada com dois devios, palavras reservadas if&else. 
# Se a Expressão lógica for testada no if for verdadeira, o bloco de código do if será executado, o contrario else será execuado.






#  IF/elif/else: em alguns cenarios usamos mais de dois desvios, elif é composto de uma nova expressão lógica, que será testada
# no caso de verdadeiro, o bloco de código elif será executado.
# Não existe um máximo de elifs, porem evite grandes estruturas condicionais, pois almentam a complexidade do codigo.



opcao = init(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao ==1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o Extrato...")

else:
    sys.exit("Opção Inválida")
















