#Exercicio de numero 8

#Analisando a fórmula:
#Prestação = valor + (valor * (taxa/100) * tempo)
#Crie um algoritmo para efetuar o cálculo do valor de uma
#prestação em atraso. (Você deverá ler o VALOR da prestação, a
#TAXA de juros imposta pelo banco, e o número de dias em
#ATRASO).



print('Exercício de número 9.\nMinistrado pela Professora Ecila.\n\n')
valor = float(input('Digite o valor da prestação:'))
taxas = float(input('Digite o valor da taxa:'))
diasEmAtraso = int(input('Digite a quantidade de dias que esta em atraso:'))

prestacao = valor + (valor * (taxas/100) * diasEmAtraso)
print('Valor da prestação:', valor)
print('Valor da taxa:',taxas)
print('Quantidades de dias atrasados',diasEmAtraso)
print('O valor da prestação é de',prestacao)
print('---------------------------------------------------------------------------')
# ---------------------------------------------------------------------------