caminho_arquivo = 'C:\Workspace/vscode/arquivo.py'

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Esta é a primeira linha.\n')
    arquivo.write('Esta é a segunda linha\n')
    
    linhas = ['Esta é a primeira linha em uma lista.\n', 'Esta é a segunda linha em uma lista.\n']
    arquivo.writelines(linhas)