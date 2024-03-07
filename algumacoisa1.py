caminho_arquivo = '/Users/aluno/Desktop/Python/Manipulação/dados.txt'

arquivo = open(caminho_arquivo, 'r')

linha1 = arquivo.readline()
print(f'Linha1: {linha1}')

linha2 = arquivo.readline()
print(f'Linha2: {linha2}')

arquivo.close()


