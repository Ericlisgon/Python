#Exercicio de numero 2

#O custo ao consumidor de um carro novo, é a soma do custo de
#fábrica com a porcentagem do revendedor e com o custo dos
#impostos (aplicados ao custo da fabrica). Supondo que a
#porcentagem do revendedor seja de 25% do custo de fábrica e que
#os impostos custam 45% do custo de fábrica, faça um algoritmo
#que leia o valor de custo de fábrica e determine o preço do
#automóvel para o consumidor.


print('Exercício de número 2.\nMinistrado pela Professora Ecila.\n\n')
custoFabrica = float(input('Digite o custo de fabrica: '))
revendedor = (custoFabrica * 0.25)
print('Revendedor:',revendedor)
imposto = (custoFabrica * 0.45)
print('imposto:',imposto)
precoFinal = (custoFabrica + imposto + revendedor)
print('O valor final para a venda é de',precoFinal,'R$')
print('---------------------------------------------------------------------------')
# ---------------------------------------------------------------------------