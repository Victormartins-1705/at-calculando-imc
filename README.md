#atividade Faça um algoritmo que calcule o IMC e exiba na tela.

altura = float(input('digite sua altura'))
peso = float(input('digite seu peso'))
imc = peso /(altura * altura)
imc = '{:.1f}'.format(imc)
imc = float(imc)

if imc < 19.5:
    print('abaixo do peso')
