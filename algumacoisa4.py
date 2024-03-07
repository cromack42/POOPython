caminho_arquivo = '/workspace/Python/Manipulação/dados3.txt'

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Esta é a primeira linha.\n')
    arquivo.write('Esta é a segunda linha\n')
    
    linhas = ['Esta é a primeira linha em uma lista.\n', 'Esta é a segunda linha em uma lista.\n']
    arquivo.writelines(linhas)