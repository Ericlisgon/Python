#Exercicio de numero 6

#Uma empresa de desenvolvimento de softwares paga ao seu
#vendedor um salário fixo de R$ 500,00 por mês, mais um bônus de
#R$ 50,00 por sistema vendido. Faça um algoritmo que leia
#quantos softwares o funcionário vendeu e determine o salario
#total do funcionário. Mostre as informações que achar
#necessárias.



print('Exercício de número 6.\nMinistrado pela Professora Ecila.\n\n')

salario = 500.00

vendas = int(input('Digite a quantidade de sistemas vendidos:'))
salario = (salario + vendas * 50.00)
print('Salario a receber',salario,'R$')

print('---------------------------------------------------------------------------')
# ---------------------------------------------------------------------------