caminho_arquivo = '/workspace/Python/Manipulação/dados2.txt'

arquivo = open(caminho_arquivo, 'r')
linhas = arquivo.readline()
for i, linha in enumerate(linhas, start=1):
    print(f'Linha {i}: {linha}')