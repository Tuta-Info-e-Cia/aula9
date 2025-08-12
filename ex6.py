"""
6.	Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""

medias = []
for i in range(10):
    print(f"\nAluno {i+1}:")
    notas = []
    for j in range(4):
        while True:
            try:
                nota = float(input(f"Digite a {j+1}ª nota: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida! Digite uma nota entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite um número.")
    media = sum(notas) / 4
    medias.append(media)
alunos_aprovados = sum(1 for m in medias if m >= 7.0)
print("\nMédias dos alunos:", medias)
print("Número de alunos com média maior ou igual a 7.0:", alunos_aprovados)

