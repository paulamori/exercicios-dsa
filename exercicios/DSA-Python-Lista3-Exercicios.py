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
# # <font color='blue'>Lista 3 de Exercícios</font>

# %% [markdown]
# Classificamos os 10 exercícios nas seguintes categorias:
#
# - (Nível Baby)
# - (Nível Aprendiz)
# - (Nível Iniciante)
# - (Nível Iniciante Plus)
# - (Nível Pro)
# - (Nível Master)
# - (Nível Ninja)
# - (Nível Ninja Pro Master)
# - (Nível Ninja Pro Master das Galáxias)
# - (Nível Ninja Pro Master das Galáxias Plus)
#
# Divirta-se. :-)

# %%
# Importa o NumPy
import numpy as np

# %% [markdown]
# #### Exercício 1: Selecionando uma Coluna Específica (Nível Baby)
#
# Dado a matriz 4x4 abaixo, crie um novo array contendo apenas os elementos da terceira coluna.

# %%
# Cria a matriz
matriz = np.array([
    [1, 2, 3, 4],#0
    [5, 6, 7, 8],#1
    [9, 10, 11, 12],#2
    [13, 14, 15, 16]
])

# %%
# Solução
novoArray = matriz[:,2]
print(f"{novoArray}")


# Saída esperada: [ 3  7 11 15]

# %% [markdown]
# #### Exercício 2: Extraindo um Bloco (Submatriz) (Nível Aprendiz)
#
# A partir da mesma matriz do exercício 1, extraia o bloco central 2x2, que contém os números 6, 7, 10 e 11.

# %%
# Solução

novoBloco=matriz[1:3,1:3]
print(f"{novoBloco}")

# Saída esperada:
# [[ 6  7]
#  [10 11]]

# %% [markdown]
# #### Exercício 3: Produto de Matrizes (Nível Iniciante)
#
# Dadas as duas matrizes A e B abaixo, calcule o produto matricial entre A e B.

# %%
# Cria as matrizes
A = np.array([[1, 2, 3], [4, 5, 6]])       # Matriz 2x3
B = np.array([[7, 8], [9, 10], [11, 12]])  # Matriz 3x2

# %%
# Solução
produto=A@B
print(f"{produto}")


# Saída esperada:
# [[ 58  64]
#  [139 154]]

# %% [markdown]
# #### Exercício 4: Selecionando Linhas Pares e Colunas Ímpares (Nível Iniciante Plus)
#
# Dada a matriz 9x9 abaixo, crie um novo array que contenha apenas os valores das linhas de índice par e as colunas de índice ímpar.

# %%
# Cria a matriz
matriz = np.arange(81).reshape(9, 9)

# %%
# Solução
array3=matriz[::2,1::2]
print(f"{array3}")

# Saída esperada:
# [[ 1  3  5  7]
#  [19 21 23 25]
#  [37 39 41 43]
#  [55 57 59 61]
#  [73 75 77 79]]

# %% [markdown]
# #### Exercício 5: Somando Valor a Uma Submatriz (Nível Pro)
#
# Dada a matriz abaixo (preenchida com zeros) adicione o valor 5 apenas ao bloco central 2x2.

# %%
# Cria a matriz
matriz = np.zeros((4, 4), dtype = int)

# %%
# Solução

matriz[1:3,1:3]=5
print(matriz)

# Saída esperada:
# [[0 0 0 0]
#  [0 5 5 0]
#  [0 5 5 0]
#  [0 0 0 0]]

# %% [markdown]
# #### Exercício 6: Normalização de Uma Matriz (Nível Master)
#
# Normalize a matriz abaixo. 
#
# A normalização (Z-score) é feita subtraindo a média de todos os elementos de cada elemento e, em seguida, dividindo pelo desvio padrão. 
#
# Fórmula: (X - media) / desvio_padrao.

# %%
# Cria a matriz
matriz = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# %%
# Solução
normal= (matriz - matriz.mean())/np.std(matriz)
print(f"{normal}")


# %% [markdown]
# #### Exercício 7: Substituindo Valores com Base em Uma Condição (Nível Ninja)
#
# Dada a matriz abaixo, crie uma nova matriz onde todos os números maiores que 8 sejam substituídos pelo valor -1. Crie uma cópia da matriz antes de fazer a operação.

# %%
# Cria a matriz
dados = np.arange(16).reshape(4, 4)

# %%
# Solução
copia=dados
dados[dados>8]=-1
print(f"{dados}")


# Saída esperada:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8 -1 -1 -1]
#  [-1 -1 -1 -1]]

# %% [markdown]
# #### Exercício 8: Inversa de Uma Matriz (Nível Ninja Pro Master)
#
# Calcule a matriz inversa da matriz A. Depois, verifique seu trabalho calculando o produto de A pela sua inversa (o resultado deve ser a matriz identidade).
#
# A matriz inversa de uma matriz quadrada A é outra matriz, chamada A⁻¹, que quando multiplicada por A resulta na matriz identidade (uma matriz que tem 1 na diagonal principal e 0 nos outros elementos). Em outras palavras, A × A⁻¹ = I. A inversa só existe para matrizes quadradas que não sejam singulares, ou seja, que tenham determinante diferente de zero. Ela é usada para resolver sistemas lineares, desfazer transformações e em várias aplicações de álgebra linear.
#
# O determinante é um número único calculado a partir dos elementos de uma matriz quadrada (mesmo número de linhas e colunas) que resume algumas propriedades fundamentais da matriz. Ele indica, por exemplo, se a matriz é invertível (determinante diferente de zero) ou singular (determinante igual a zero).

# %%
# Cria a matriz
A = np.array([[4, 7], [2, 6]])

# %%
# Solução
inversa = np.linalg.inv(A)
print(f"{inversa}")
teste = np.round(A @ inversa, decimals=10)
print(f"{teste}")


# %% [markdown]
# #### Exercício 9: Resolvendo Um Sistema de Equações Lineares (Nível Ninja Pro Master das Galáxias)
# <!-- Trabalho Desenvolvido na Data Science Academy - www.datascienceacademy.com.br -->
# Resolva o seguinte sistema de equações lineares:
#
# 2x + y = 8
#
# x + 3y = 7
#
# Represente o sistema na forma matricial Ax = b e encontre o vetor x (que contém os valores de x e y).

# %%
# Solução

coeficientes = np.array([[2,1],
                        [1,3]])
resultados = np.array([8,7])
solucao= np.linalg.solve(coeficientes,resultados)
print(f"{solucao}")

# Saída esperada: [3.4 1.2]

# %% [markdown]
# #### Exercício 10: Extraindo a Borda de Uma Matriz (Nível Ninja Pro Master das Galáxias Plus)
#
# Dada uma matriz 5x5, crie um novo array 1D contendo todos os elementos da borda da matriz, em sentido horário, começando pelo canto superior esquerdo.

# %%
# Cria a matriz
matriz = np.arange(25).reshape(5, 5)
print(f"{matriz}")

# %%
# Solução

superior= matriz[0,:]
inferior = matriz[:,4]
colDireita=matriz[1:-1,-1]
colEsquerda=matriz[1:-1,0]
novo=np.concatenate([superior,colDireita,inferior[::-1],colEsquerda[::-1]])

print(f"{novo}")

# Saída esperada: [ 0  1  2  3  4  9 14 19 24 23 22 21 20 15 10  5]

# %% [markdown]
# # Fim
