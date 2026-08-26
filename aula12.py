

nome = 'Guilherme Lopes'
altura = 1.81
peso = 80

imc = peso/(altura**2)

print(nome,'tem',altura,'de altura')
print('Pesa',peso,'kg e seu IMC e:')
print(imc)


print('------------------------------------------')


print('Utilizando f-strings!!!')
linha_1 = f'{nome} tem {altura:.2f} de altura'
print(linha_1)
linha_2 = f'Pesa {peso} kg e seu IMC e:'
print(linha_2)
linha_3 = f'{imc:.2f}'
print(linha_3)