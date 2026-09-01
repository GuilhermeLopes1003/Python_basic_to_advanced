"""
Higher order functions
Funções de primeira classe
 
Armazenamento em variáveis: funções podem 
ser atribuídas a variáveis como qualquer 
outro objeto em Python.
"""
# exemplo:
 
 
def funcao(x, y):
    return x * y
 
 
mult = funcao
print(mult(3, 6))
print(mult(4, 5))



print("-------------------------------------------------------------------------------------------------------------------")

"""
Passagem como argumentos: funções podem
ser passadas como argumentos para outras
funções. Isso é útil para criar funções
de ordem superior, que são funções que
operam em outras funções.
"""
# exemplo:
 
 
def func(soma, a, b):
    return soma(a, b)
 
 
def argumento(a, b):
    return a + b
 
 
print(func(argumento, 3, 5))



print("-------------------------------------------------------------------------------------------------------------------")
"""
Retorno de funções: funções podem retornar
outras funções. Isso é útil para criar funções
geradoras ou para criar funções que geram
outras funções com base em parâmetros.
"""
# exemplo:
 
 
def cria_multiplo(fator):
    def multiplo(x):
        return x * fator
    return multiplo
 
 
dobro = cria_multiplo(2)
triplo = cria_multiplo(3)
 
print(dobro(3))
print(triplo(3))






""" Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

"""