#Exercicio de numero 7

#Crie um algoritmo para calcular o salário líquido de um
#funcionário, considerando que seu salário bruto, incide um
#desconto de 9% em INSS para a previdência. O algoritmo deve
#mostrar o nome do funcionário, o seu salário bruto, o valor de
#desconto de INSS e o seu salário líquido.(dica.: Você deverá
#pedir (ler) o nome do funcionário e o valor do salário bruto).


print('Exercício de número 7.\nMinistrado pela Professora Ecila.\n\n')
nome = input('Digite o seu nome:')
salario = float(input('Digite o seu salário:'))
inss = salario * 0.09
salarioLiquido = salario - inss
print('Nome:',nome,'\nSalario:',salario,'\nDesconto INSS:',inss,'\nSalário líquido:',salarioLiquido)

print('---------------------------------------------------------------------------')
# ---------------------------------------------------------------------------