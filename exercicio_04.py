#Exercicio de numero 4

#Um Cliente de um banco tem um saldo positivo de R$ 500,00.
#Fazer um algoritmo que leia um cheque que entrou e calcule o
#saldo, mostrando o saldo na tela.

print('Exercício de número 4.\nMinistrado pela Professora Ecila.\n\n')

saldo = 500.00
print('Seu saldo é de',saldo)
escolha = int(input('Se deseja fazer um DEPÓSITO digite 1 \nSe deseja fazer um SAQUE digite 2:'))

while(escolha == 1):
    entrada = float(input('Digite o valor do depósito:'))
    saldo = (saldo + entrada)
    print('Saldo atual é de', saldo)
    escolha = int(input('Deseja fazer mais algum deposito, digite 1 \nSe deseja fazer um SAQUE digite 2 \nSe deseja FINALIZAR digite 0'))

while(escolha == 2):
    saida = float(input('Digite o valor do saque:'))
    saldo = (saldo - saida)
    print('Saldo atual é de', saldo)
    escolha = int(input('Deseja fazer mais algum deposito, digite 1 \nSe deseja fazer um SAQUE digite 2 \nSe deseja FINALIZAR digite 0'))
print('---------------------------------------------------------------------------')
# ---------------------------------------------------------------------------