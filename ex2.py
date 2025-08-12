"""
2.	Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""


lista =[]
for i in range(10):
    l = float(input(f'Digite o {i+1}º número da lista: '))
    lista.append(l)

lista.reverse()
for i in range(10):
    print(f'Posição => {i} na lista, tem o conteúdo{lista[i]}')
    