# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(10,2,3)
print(f"A multiplicacao desses numero e igual a : {multiplicacao}")


print("-------------------------------------------------------------------------------------------------------------------")

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def paridade(numero):
    multiplo_dois = numero % 2 == 0

    if multiplo_dois:
        return f"{numero} e par."
    return f"{numero} e impar."

print(paridade(2))
print(paridade(15))
print(paridade(40))
print(paridade(99))



