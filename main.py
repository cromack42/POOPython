from datetime import date
from pessoa import Pessoa
from marca import Marca
from banco import BancoDedados
from veiculo import Veiculo

if __name__ == '__main__':
    # Criando uma instância da classse BancoDeDados
    banco = BancoDedados()
    # Conecetando ao banco de classe BancoDeDados
    banco.conectar()
    # Criando as tabelas necessárias
    banco.criar_tabelas()
    # Inserindo uma pessoa
    pessoa1 = Pessoa(cpf=12345678900, nome="Raphael", nascimento="1984-07-26, oculos=True")
    banco.inserir_pessoa(pessoa1)

    # Criando uma instância de pessoa
    pessoa1 = Pessoa(cpf=12345678900, nome="Raphael", nascimento=date(1984, 7, 26), oculos=True)

    # Criando uma instância de Marca
    marca1 = Marca(id=1, nome="Fiat", sigla="FIA")

    # Criando uma instância de Veiculo
    Veiculo = Veiculo(placa="LRW1I27", cor="Cinza", propietario=pessoa1, marca=marca1)

    # Inserindo uma marca 
    marca1 = Marca(id=1, nome="FIAT", sigla="FIA")
    banco.inserir_marca(marca1)

    # Inserindo um veículo
    veiculo1 = Veiculo(placa="LRW1I27", cor="Cinza", proprietario=pessoa1, marca=marca1)
    banco.inserir_veiuclo(veiculo1)

    # Buscando todas as pessoas
    print("Pessoas:")
    for pessoa in banco.buscar_todas_pessoas():
        print(pessoa)

    # Buscando todas as marcas
    print("\nMarcas:")
    for marca in banco.banco.buscar_todas_marcas():
        print(marca)

    # Buscando todos os veículos
    print("\nVeículos:")
    for veiculo in banco.buscar_todos_veiculos():
        print(veiculo)
        
    # Fechado a conexão com o banco de dados
    banco.fechar_conexao()
