# coding: latin-1
# ç substituido por "c"
import math
import os

# os.system('cls')
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print('Bem vindo, por favor, digite o numero correspondente de cada modo para das inicio\n')
print('Soma - 1')
print("Subtracao - 2")
print('Divisao - 3')
print('Raiz quadrada - 4')
print('Sucessor e Antecessor - 5')
print('Multiplicacao - 6')
escUser = raw_input('\nDigite um numero correspondente do modulo: ')

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')


#soma
if escUser == '1':
    print('Voce entro no modo soma\n')
    n1 = int(input('Digite o primeiro numero da soma: '))
    n2 = int(input('Digite o segundo numero da soma: '))
    soma = n1 + n2
    print('{} + {} = {}').format(n1,n2,soma)

#subtracao
if escUser == '2':
    print('Voce entro no modo subtracao\n')
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    sub = n1 - n2
    print('{} - {} = {}').format(n1,n2,sub)

#divisao
if escUser == '3':
    print('Voce entrou no modo de divisao\n')
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    divisao = n1 / n2
    print('{} / {} = {}').format(n1,n2,divisao)

#raiz quadrada
if escUser == '4':
    print('Voce entrou no modo raiz\n')
    n1 = int(input('Digite o numero para saber sua raiz: '))
    raiz = math.sqrt(n1)
    print('A raiz de {} eh: {}').format(n1,raiz)

#Sucessor e Antecessor
if escUser == '5':
    print('Voce entrou no modo Sucessor e Antecessor\n')
    n1 = int(input('Digite o numero que voce gostaria de saber o Sucessor e Antecessor: '))
    sucss = n1 + 1
    antcss = n1 - 1
    print('\nO sucessor de {} eh: {}\nE o antecessor eh {}').format(n1,sucss,antcss)

#Multiplicacao
if escUser == '6':
    print('Voce entrou no modo de Multiplicacao\n')
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    mult = n1 * n2
    print('{} * {} = {}').format(n1,n2,mult)
