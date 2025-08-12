#4.	Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

caracteres = []

vogais = ['a', 'e', 'i', 'o', 'u']

for i in range(10):
    char = input(f"Digite o {i+1}ª letra:  ").lower()
    if len(char) == 1 and char.isalpha():  # Verifica se é uma letra
        caracteres.append(char)
    else:
        print("Entrada inválida! Digite apenas uma letra.")
        exit()

consoantes = [c for c in caracteres if c not in vogais]

print(f"\nNúmero de consoantes: {len(consoantes)}")
print("Consoantes lidas:", ', '.join(consoantes))
