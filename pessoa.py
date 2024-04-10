from dataclasses import dataclasses
from datatime import date

@dataclasses
class Pessoa:
    cpf: int
    nome: str
    nascimento: date
    oculos: bool