from dataclasses import class
from pessoa import Pessoa
from marca import Marca

@dataclass
class Veiculo:
    placa: str
    cor: str
    propietario: Pessoa
    marca: Marca
