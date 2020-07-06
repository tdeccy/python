#1 Criar if para entrar em um "modulo" da calculadora
#2 Criar os modulos da calcoladora (mais, menos, divisao etc..)
#3 Encrementar a calculadora


import math
import os

# os.system('cls')
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('Bem vindo, por favor, digite o numero correspondente de cada modo para das inicio\n')
print('Soma - 1')
print('Subtracao - 2')
print('Divisao - 3')
print('Raiz quadrada - 4')
escUser = raw_input('\nDigite um numero correspondente do modulo: ')

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')


#soma
if escUser == '1':
    print('voce entro no modo soma')
    n1 = int(input('Digite o primeiro numero da soma: '))
    n2 = int(input('Digite o segundo numero da soma: '))
    soma = n1 + n2
    print('{} + {} = {}').format(n1,n2,soma)

#subtracao
if escUser == '2':
    print('Voce entro no modo subtracao')
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    sub = n1 - n2
    print('{} - {} = {}').format(n1,n2,sub)

#divisao
if escUser == '3':
    print('Voce entrou no modo de divisao')
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    divisao = n1 / n2
    print('{} / {} = {}').format(n1,n2,divisao)

#raiz quadrada
if escUser == '4':
    print('Voce entrou no modo raiz')
    n1 = int(input('Digite o numero para saber sua raiz: '))
    raiz = math.sqrt(n1)
    print('A raiz de {} eh: {}').format(n1,raiz)