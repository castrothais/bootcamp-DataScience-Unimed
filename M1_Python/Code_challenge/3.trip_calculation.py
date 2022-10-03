""" Entrada
O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na
viagem em horas e o segundo é a velocidade média durante a mesma em km/h.

Saída
Imprima a quantidade de litros necessária para realizar a viagem, com três
dígitos após o ponto decimal

 """
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

# TODO:  Calcule quantidade de litros necessária para realizar a viagem e
# imprima com TRÊS dígitos após o ponto decimal

tempo_gasto_viagem = int(valores[0])
velocidade_media = int(valores[1])
COMBUSTIVEL_POR_KM = 12

distancia_total = tempo_gasto_viagem * velocidade_media
litros_necessario = distancia_total / COMBUSTIVEL_POR_KM
print('%.3f' % litros_necessario)
