#Exercicio de numero 3

#O sistema de avaliação de determinada disciplina é composto por
#três provas. A 1ª prova tem peso 2, a 2ª prova tem peso 3 e a
#3ª prova tem peso 5. Faça um algoritmo para calcular a média
#final de um aluno desta disciplina.


print('Exercício de número 3.\nMinistrado pela Professora Ecila.\n\n')
prova1 = float(input('Digite sua primeira nota(A1):'))
prova2 = float(input('Digite sua segunda nota(A2):'))
prova3 = float(input('Digite sua terceira nota(A3):'))

media = (prova1 * 2 + prova2 * 3 + prova3 * 5)/10
print('Média:',media)
print('---------------------------------------------------------------------------')
# ---------------------------------------------------------------------------