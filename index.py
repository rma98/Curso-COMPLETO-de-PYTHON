# variáveis
# nome, idade, peso, e_programador = 'Robson',  24, 68.5, True
# print(f'Meu nome é {nome} e eu tenho {idade} anos. Meu peso é {peso}kg. Sou programador? {e_programador}.')
# nome = input('Seu nome: ')
# print(f'Olá {nome}, tudo bem?')
# # conversão de dados
# idade = int(input('Sua idade: '))
# peso = float(input('Seu peso: '))
# print(f'{type(nome)}\n{type(idade)}\n{type(peso)}')
# operadores aritméticos: + - * / // ** %
# nota1 = float(input('Nota 1: '))
# nota2 = float(input('Nota 2: '))
# soma = nota1 + nota2
# media = soma / 2 
# print(f'A soma entre {nota1} e {nota2} é {soma}.\nE a média é {media}.')
# # operadores relacionais: < > <= >= == !=
# operador = 5 == 5
# print(f'É verdade? {operador}')
# operadores lógicos: and or not
# operador = True and False
# oper = True or False
# op = not True
# print(f'É verdade? {operador}\nÉ verdade? {oper}\nÉ verdade? {op}')
# estrutura de decisão
# media = float(input('Digite sua média: ')) 
# if media >= 7:
#     print('Aprovado.')
# elif media >= 4:
#     print('Em recuperação.')
# else:
#     print('Rperovado.')
# estrutura de repetição
# n = 1
# while n < 11:
#     resultado = n * 5
#     if n == 6:
#         break
#     print(f'{n} x {n} = {resultado}')
#     n += 1
# print('-'*20)
# print('\tTABUADA')
# print('-'*20)
# for i in range(1, 11):
#     for x in range(1, 11):
#         resultado = i * x
#         print(f'{i} x {x} = {resultado}') 
#     print('-'*20)
# listas
# idades = [21, 22, 50, 60]
# idades.pop(1)
# idades.append(100)
# print(type(idades))
# for idade in idades:
#     print(idade)
# notas = []
# while True:
#     nota = int(input('Digite uma nota ou -1 para sair: '))
#     if nota == -1:
#         break
#     notas.append(nota)
# soma = 0
# for nota in notas:
#     print(nota)
#     soma += nota
# media = soma / len(notas)
# print(f'A soma das notas é: {soma}. E a média é {media:.1f}.')
# dicionários
# pessoa = {
#     'nome': 'Robson',
#     'idade': 24,
#     'peso': 1.68,
#     'cidade': 'Ribeirão'
# }
# print(f'{pessoa["nome"]}')
# pessoas = [{
#     'nome': 'Robson', 'idade': 24, 'peso': 1.68, 'cidade': 'Ribeirão'},
#     {'nome': 'Caio', 'idade': 22, 'peso': 1.73, 'cidade': 'Franca'}
# ]
# for pessoa in pessoas:
#     print(f'{pessoa["nome"]} tem {pessoa["idade"]} anos. Seu peso é de {pessoa["peso"]}kg. E mora em {pessoa["cidade"]}.')
# funções
# def exibe_bom_dia():
#     print('Bom dia')
#     print('Tudo bom?')
# exibe_bom_dia()
# def soma(n1, n2, n3):
#     resultado = n1 + n2 + n3
#     return resultado
# resultado = soma(5, 2, 5)
# print(resultado)
# importações
from calculos import soma, multiplicacao
total = soma(2, 5, 6)
print(total)