# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# <!-- Trabalho Desenvolvido na Data Science Academy - www.datascienceacademy.com.br -->
# # <font color='blue'>Data Science Academy</font>
# # <font color='blue'>Fundamentos de Linguagem Python - Do Básico a Aplicações de IA</font>
# # <font color='blue'>Lista 2 de Exercícios</font>

# %% [markdown]
# #### Exercício 1
#
# Escreva uma função que receba os valores de três lados de um triângulo e o classifique como "Equilátero" (todos os lados iguais), "Isósceles" (dois lados iguais) ou "Escaleno" (todos os lados diferentes).

# %%
# Solução
def verificaTriangulo(l1,l2,l3):
    if l1==l2 and l2==l3:
        print("Equilátero")
    elif l1==l2 or l2==l3 or l3==l1:
        print("Isosceles")
    else:
        print("Escaleno")

verificaTriangulo(5,3,9)


# %% [markdown]
# #### Exercício 2
#
# Escreva uma função que recebe um número inteiro e exibe a tabuada de multiplicação desse número, do 1 ao 10.

# %%
# Solução
def tabuada(num1):
    for num in range(11):
        print(f"{num1}*{num}={num1*num}")
tabuada(7)

# %% [markdown]
# #### Exercício 3 
#
# Você recebeu um dicionário com os nomes dos alunos e suas respectivas notas. Escreva uma função que calcula a média da turma e retorna uma lista com os nomes dos alunos que tiveram nota acima da média.

# %%
# Solução
alunos=[{"nome":"ana", "nota":20},
       {"nome":"lais", "nota":20},
       {"nome":"bia", "nota":20}]

def mediaTurma(dict):
    soma=0
    for aluno in dict:
        soma+=aluno.get("nota")
        if aluno.get("nota")>7:
            print(f"{aluno.get("nome")}")
    media=soma/3
    return media

resultado=mediaTurma(alunos)
print(resultado)

# %% [markdown]
# #### Exercício 4
#
# Dada uma lista de números, crie uma nova lista usando list comprehension que contenha o quadrado de cada número par da lista original.

# %%
# Solução
lista1=[1,2,3,4,5]
quadrado=[x**2 for x in range(len(lista1)+1) if x%2==0]
print(f"{quadrado}")


# %% [markdown]
# #### Exercício 5
#
# Crie uma função chamada dsa_calcula_imc que aceite dois argumentos: peso (em kg) e altura (em metros). A função deve calcular o Índice de Massa Corporal (IMC) usando a fórmula IMC=peso/altura^2 e retornar o valor do IMC.

# %%
# Solução
def dsa_calcula_imc(peso,altura):
    imc=peso/altura**2
    return imc

print(f"{dsa_calcula_imc(60,1.70):.2f}")

# %% [markdown]
# #### Exercício 6
#
# Você tem uma lista de dicionários, onde cada dicionário representa uma pessoa com nome e idade. Use a função sorted() com uma expressão lambda como chave (key) para ordenar a lista de pessoas da mais nova para a mais velha.

# %%
# Solução

# %% [markdown]
# #### Exercício 7
#
# Crie uma função que receba uma lista de números inteiros e retorne um dicionário contendo a contagem de quantos números são pares e quantos são ímpares.

# %%
# Solução



# %% [markdown]
# #### Exercício 8
#
# Crie uma função que receba uma lista de strings (potenciais e-mails) e um parâmetro opcional dominio_desejado (com valor padrão "gmail.com"). A função deve retornar uma nova lista, usando list comprehension, contendo apenas os e-mails que terminam com o domínio desejado.

# %%
# Solução


# %% [markdown]
# #### Exercício 9
#
# Dada uma lista de frases, use a função map() em conjunto com uma expressão lambda para criar uma nova lista onde cada frase é convertida para letras maiúsculas e tem a palavra "PYTHON" anexada ao final.

# %%
# Solução


# %% [markdown]
# #### Exercício 10
#
# Crie um jogo onde o computador escolhe um número secreto entre 1 e 20. O jogador tem 5 tentativas para adivinhar. A cada tentativa, o programa informa se o palpite foi muito alto ou muito baixo. Se o jogador acertar, o loop deve ser interrompido com uma mensagem de vitória.

# %%
# Solução
import random
numeroSecreto= random.randint(1,20)
print("Bem vindo ao jogo de adivinhação")
for escolha in range(5):
    escolha=(int(input("Qua seu palpite?:")))
    if escolha==numeroSecreto:
             print("Você acertou!")
             break
    elif escolha>numeroSecreto:
        print("Muito alto")
    else:
        print("Muito baixo")
        
print(f"O numero é {numeroSecreto}")

# %% [markdown]
# # Fim
