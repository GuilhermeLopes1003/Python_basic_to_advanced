"""
Faça um programa que peça ao usuario para digitar um numero inteiro, informe se esse numero é par ou impar
Caso o usuario nao digite um numero inteiro, informe que nao é um numero inteiro 
"""
entrada_num = input("Insira o numero inteiro:")

if entrada_num.isdigit():
    entrada_int = int(entrada_num)
    par_impar = entrada_int % 2 == 0
    par_impar_txt = "impar"

    if par_impar:
        par_impar_txt = "par"
    
    print(f"O numero {entrada_int} e {par_impar_txt}")
else:
    print("Vc nao digitou um numero inteiro")    


print("--------------------------------------------------------------------------------------------------")



"""
Faça um programa que pergunta a hora ao usuario e, baseando no horario descrito exiba a saudação apropriada
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

hora = input("Insire a hora exata:")

if hora.isdigit():
    hora_int = int(hora)

    if hora_int >= 0 and hora_int <= 11:
        print(f"Bom dia a hora {hora_int} esta entre 0-11")
    elif hora_int >= 12 and hora_int <= 17:
        print(f"Boa tarde a hora {hora_int} esta entre 12-17")
    else:
        print(f"Boa noite a hora {hora_int} esta entre 18-23")
else:
    print("Vc nao digitou um numero inteiro")


print("--------------------------------------------------------------------------------------------------")



"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto",
se tiver entre 5 e 6 letras, escreva "Seu nome é normal", maior que 6 escreva "Seu nome é grande".
"""

nome = input("Insira seu primeiro nome:")
nome_tam = len(nome)

if nome_tam <=4:
    print(f"Seu nome e curto: {nome}")
elif nome_tam >= 5 and nome_tam <=6:
    print(f"Seu nome e normal: {nome}")
else:
    print(f"Seu nome e grande: {nome}")
