#Exercicio de numero 8

#Considerando que para um consórcio, sabe-se o número total de
#prestações, a quantidade de prestações pagas e o valor atual da
#prestação, escreva um algoritmo que determine o total pago pelo
#consorciado e o saldo devedor.


print('Exercício de número 8.\nMinistrado pela Professora Ecila.\n\n')
numeroPrestacao = int(input('Digite a quantidade de prestações:'))
valorPrestacao = float(input('Digite o valor das prestações:'))
qtdPrestacaoPagas = int(input('Digite a quantidade de prestações que foram pagas:'))
qtdParcelasQueFaltam = numeroPrestacao - qtdPrestacaoPagas

print('Quantidade de prestações:',numeroPrestacao)
print('Valor das prestações',valorPrestacao)
print('Quantidade de prestações que foram pagas:',qtdPrestacaoPagas)
print('Quantidade de parcelas que faltam:',qtdParcelasQueFaltam)
divida = (qtdParcelasQueFaltam * valorPrestacao)
print('Valor da divida(O que falta pagar)',divida)
print('---------------------------------------------------------------------------')
# ---------------------------------------------------------------------------