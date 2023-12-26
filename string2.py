nome = "Michael Douglas"
idade = 70
profissao = "Ator"
ator_star = "5"


print("nome: %s idade: %d" % (nome, idade))

#método obsoleto.



nome = "Michael Douglas"
idade = 70
profissao = "Ator"
ator_star = "5"

print("nome: {} idade: {}" .format(nome,idade))


nome = "Michael Douglas"
idade = 70
profissao = "Ator"
ator_star = "5"

print("nome: {0} idade: {1}" .format(nome,idade))

nome = "Michael Douglas"
idade = 70
profissao = "Ator"
ator_star = "5"

print("nome: {nome} idade: {idade}" .format(nome=nome, idade=idade))

nome = "Michael Douglas"
idade = 70
profissao = "Ator"
ator_star = "5"

print("nome: {name} idade: {age} {name} {age}".format(age=idade, name=nome))


dados = {"nome": "Dom Ramon", "idade": 28}

print("nome: {nome} idade: {idade}".format(**dados))

#  todos os métodos acima, já não são recomendados.


# F STRING, método atualmente mais ultilizado.

nome = "Michael Douglas"
idade = 70
profissao = "Ator"
ator_star = "5"
saldo = 100


print (f"nome: {nome} idade: {idade} saldo: {saldo:2.1f}")


