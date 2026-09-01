# Lista de compras com lista

import subprocess

lista = []

while (True):
    print("Selecione uma opcao: ")
    opcao = input("[i]inserir [a]apagar [l]listar s[sair]: ")

    if opcao == "i":
        subprocess.run("cls", shell=True)
        valor = input("Adicionar item na lista de compras: ")
        lista.append(valor)

    elif opcao == "a":
        indice_str = input("Digite o indice do item a ser apagado: ")
        try:
            indice = int(indice_str)
            del(lista[indice])
        except ValueError:
            print("Indice invalido, digite um numero valido.")
        except IndexError:
            print("Indice nao existe na lista, digite um indice valido.")
        except Exception:
            print("Erro desconhecido, tente novamente.")

    elif opcao == "l":
        subprocess.run("cls", shell=True)
        if len(lista) == 0:
            print("Lista vazia, nada para listar.")

        for i, valor in enumerate(lista):
            print(i, valor)

    elif opcao == "s":
        subprocess.run("cls", shell=True)
        print("Saindo...")
        break

    else:
        subprocess.run("cls", shell=True)
        print("Por favor, escolha i, a, l ou s. ")
