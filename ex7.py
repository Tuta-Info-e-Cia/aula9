"""
7.	Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

numeros = []
for i in range(5):
    while True:
        try:
            num = int(input(f"Digite o {i+1}º número inteiro: "))
            numeros.append(num)
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
soma = sum(numeros)
multiplicacao = 1
for num in numeros:
    multiplicacao *= num
print("\nNúmeros digitados:", numeros)
print("Soma dos números:", soma)
print("Multiplicação dos números:", multiplicacao)
