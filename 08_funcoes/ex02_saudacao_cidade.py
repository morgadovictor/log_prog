"""
Construa um programa/página onde o usuário irá digitar seu nome e cidade
de onde está digitando.
◆ Essas informações passarão para uma função e, caso a cidade seja “Rio de
Janeiro”, a resposta, além do nome da pessoa, escreverá “Seja Bem-vindo à
Cidade Maravilhosa”.
◆ Caso contrário, exibirá apenas o nome e a cidade digitada
(utilizar passagem de parâmetros).
"""


def saudacao(nome: str, cidade: str):
    # comparação insensível a maiúsculas
    if cidade.lower() == "rio de janeiro":
        print(f"\n{nome}, seja bem-vindo(a) à Cidade Maravilhosa!")
    else:
        print(f"\nNome: {nome} | Cidade: {cidade}.")


nome = input("Digite o seu nome: ").strip().title()
cidade = input("Digite a sua cidade: ").strip().title()

# Chama a função
saudacao(nome, cidade)
