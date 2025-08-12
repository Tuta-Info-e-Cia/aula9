"""
1.	Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

#criar uma lista
lista =[]
#varrer a lista para entrar com os 5 numeros da lista
for i in range(5):
    l = int(input(f'Digite o {i+1}º número da lista: '))
    #gravando os numeros na lista
    lista.append(l)
#imprimir o conteudo da lista
    
for i in range(5):
    print(f'Posição => {i} na lista, tem o conteúdo{lista[i]}')
    