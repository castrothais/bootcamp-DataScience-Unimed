# ADICIONAR ELEMENTO NA LISTA
lista = []
lista.append("Bootcamp ciencia de dados")
lista.append(3)
print(lista)


# LIMPANDO LISTA
lista_clear = [1, "Python", [40, 30, 20]]
lista_clear.clear()
print(lista_clear)  # []


# COPIA LISTA
"""ID diferentes, lista nova"""
lista_cores = ["amarelo", "rosa", "vemelho"]
lista_cores.copy()
print(lista_cores)  # ["amarelo", "rosa", "vemelho"]


# NÚMERO DE VEZES QUE O ELEMENTO ESPECIFICADO APARECE
semana = ["sabado", "domingo", "segunda", "quinta", "quinta", "terça"]
print(semana.count("sabado"))  # 1
print(semana.count("quinta"))  # 2


# EXTENDER A LISTA COM MAIS DE 1 ELEMENTO
linguagens = ["python", "js", "c"]
linguagens.extend(["java", "csharp"])
print(linguagens)  # ["python", "js", "c", "java", "csharp"]


# RETORNA O INDEX DO ELEMENTO
"""Não retorna todas as ocorrências, apenas a primeira"""
animais = ["cachorro", "galinha", "gato", "gavião"]
print(animais.index("cachorro"))  # 0
print(animais.index("gavião"))  # 3


# REMOVE O ULTIMO ITEM OU ESPECIFICADO
nomes = ["thais", "mayu", "gabriel", "lara", "vinicius"]
print(nomes.pop())  # vinicius
print(nomes.pop())  # lara
print(nomes.pop(0))  # thais
print(nomes.pop())  # gabriel


# REMOVE
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.remove("c")
print(linguagens)  # ["python", "js", "java", "csharp"]


# REVERSE
cozinha = ["panela", "talher", "copo", "comida"]
cozinha.reverse()
print(cozinha)  # ['comida', 'copo', 'talher', 'panela']

# ORDENAR A LISTA - sort() que modifica a lista em si
"""Ordem alfabética"""
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

"""Espelhamento"""
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

"""Ordenar por tamanho de cada item"""
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(
    key=lambda x: len(x)
)  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

"""Ordenar por tamanho do maior pro menor"""
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)
# ["python", "csharp", "java", "js", "c"]
print(linguagens)


# TAMANHO DO ARRAY
cidades = ["Sao Paulo", "Rio de Janeiro", "Vitoria", "Belo Horizonte"]
print(len(cidades))  # 4


# ORDERNAR - sorted() cria uma nova lista
linguagens = ["python", "js", "c", "java", "csharp"]

print(
    sorted(linguagens, key=lambda x: len(x))
)  # ["c", "js", "java", "python", "csharp"]
print(
    sorted(linguagens, key=lambda x: len(x), reverse=True)
)  # ["python", "csharp", "java", "js", "c"]
