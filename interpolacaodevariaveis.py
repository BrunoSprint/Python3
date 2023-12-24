# Existem 3 formas de Interpolar Variáveis em Strings.
# 1° Usando o sinal %  2° Usando o método FORMAT  3° Utilizando f strings.

# A primeira não é recomendade em PY3.


# %   método de difícil manutensão para Strings longas.

nome = "Michael Douglas"
idade = 70
profissao = "Ator"
ator_star = "5"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou no Nivel %s de Ator-Estrela." % (nome, idade, profissao, ator_star))



# Método Format, Baixa matutenabilidade.

nome = "Michael Douglas"
idade = 70
profissao = "Ator"
ator_star = "5"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou no Nivel {} de Ator-Estrela.".format(nome, idade, profissao, ator_star))




# Método Format, Baixa matutenabilidade. Método Númerado.

nome = "Michael Douglas"
idade = 70
profissao = "Ator"
ator_star = "5"

print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou no Nivel {3} de Ator-Estrela.".format(nome, idade, profissao, ator_star))




# Método Format, Baixa matutenabilidade. Método Nomeado.

nome = "Michael Douglas"
idade = 70
profissao = "Ator"
ator_star = "5"

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou no Nivel {ator_star} de Ator-Estrela.".format(nome=nome, idade=idade, profissao=profissao,ator_star=ator_star))



# f-string

PI = 3.14159

print(f"valor de PI: {PI:.2f}")

print(f"valor de PI: {PI:10.3f}")







