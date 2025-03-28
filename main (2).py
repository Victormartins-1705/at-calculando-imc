import random


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


nomes = ["victor", "emilly", "Carlos", "Daniela", "Eduardo", "Helena"]
nome = random.choice(nomes)
idade = random.randint(18, 60)
peso = round(random.uniform(50, 120), 2)
altura = round(random.uniform(1.5, 2.0), 2)

imc = calcular_imc(peso, altura)

print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.2f}")
