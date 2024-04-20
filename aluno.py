class aluno:
    def __init__(nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.notas = notas
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

if __name__ == "__main__":
    aluno1 = Aluno("Raphael", 39, [9.5, 8.7, 7.2])
    aluno2 = Aluno("Caroline", 30, [6.3, 7.3, 8.9])
    lista_alunos = [aluno1, aluno2]
    for aluno in lista_alunos:
        print(f"Nome: {aluno.nome}, Media: {aluno.calcular_media():.2f}")

