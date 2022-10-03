""" Desafio
Os estudiosos de Minas Tirith, grande cidadela de Gondor, concluíram que para
calcular o ICM para Palantír's, basta dividir a distância entre os dois
Palantír's, pela soma do diâmetro dos mesmos."""


# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao
# usuário,onde geralmente informa que tipo de informação ele está esperando
# receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os
# valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as
# condições especificadas em cada parâmetro da função ou com os valores
# predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

# Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas
# decimais no espaço #em branco abaixo:
ICM = distancia / (diametro1 + diametro2)
print("%.2f" % ICM)
