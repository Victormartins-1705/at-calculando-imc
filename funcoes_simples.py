
def boas_vindas():
    print("Bem-vindo(a) à disciplina ALLP")

def quadrado(numero):
    return numero ** 2

def somar(a, b):
    return a + b

def contagem(inicio=1, fim=5):
    for i in range(inicio, fim + 1):
        print(i)

def calcula_imc(peso=70, altura=1.75):
    return peso / (altura ** 2)

def par_ou_impar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

def saudacao(nome="Visitante"):
    print("Olá,", nome)

# Testes simples
boas_vindas()
print(quadrado(3))
print(somar(2, 5))
contagem()
print(calcula_imc())
par_ou_impar(4)
saudacao("Victor")
