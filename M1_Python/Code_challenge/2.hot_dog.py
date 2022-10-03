""" Desafio: Dados o número total de cachorros-quentes consumidos e o número
total de participantes na competição, você deve escrever um programa para
determinar o número médio de cachorros-quentes consumidos pelos participantes.

Entrada
A entrada consiste de uma única linha que contém dois inteiros H e
P (1 ≤ H, P ≤ 1000) indicando respectivamente o número total de
cachorros-quentes consumidos e o número total de participantes na
competição."""

# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao
# usuário, onde geralmente informa que tipo de informação ele está esperando
# receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os
# valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as
# condições especificadas
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
valores = input().split()

# TODO:  Calcule a média de cachorros quentes consumidas por participante e
# imprima o valor com DUAS casas decimais.

H = int(valores[0])
P = int(valores[1])
media = H / P
print("%.2f" % media)
