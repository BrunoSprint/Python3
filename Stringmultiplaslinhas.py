#String de Multiplas Linhas,é informada por 3x """,(string tripla)simples ou duplas, durante atribuição. Podem ocupar variaas linhas #de código, e todos os espaços em branco são incluídos na string final.
    




nome = "Michael Douglas"

mensagem = f"""
   Olá meu nome é {nome}.
       Eu estou práticando Python3.
           Essa mensagem tem diferentes recuos,identação.

"""


print(mensagem)







print(

    """
    =================Menu===================
    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - sair
    ========================================
        Obrigado po usar nosso Sistema!!!!
    """
)




# Use \n no final da string para fazer a quebra de linha.


# Método de string independente. ideal para agregar ou remover item de menu.

menu = "=============Star=============\n"
menu += "\n"
menu += "1 - Depositar\n"
menu += "2 - Sacar\n"
menu += "3 - Extrato\n"
menu += "4 - Logout\n"
menu += "Obrigado por últilizar nosso Sistema\n"
menu += "==============================="


print(menu)