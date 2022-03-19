#Exercicio de numero 5


#Uma empresa de vendas se softwares para a seu vendedor um fixo
#de R$ 800,00 por mês, mais uma comissão de 15% pelo seu valor
#de vendas no mês. Faça um algoritmo que leia o valor da venda e
#determine o salário total do funcionário. Mostre as informações
#necessárias na tela.


print('Exercício de número 5.\nMinistrado pela Professora Ecila.\n\n')

salario = 800.00
print('Seu salario é de',salario)
valorDasVendas = float(input('Digite o valor toral das vendas feitas neste mês:'))

salario = salario + (valorDasVendas * 0.15)
print('Recebimento de',salario)
print('---------------------------------------------------------------------------')
# ---------------------------------------------------------------------------