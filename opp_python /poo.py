from rich import print
from rich.traceback import install
from abc import ABC, abstractmethod

install()


class RH:
    def __init__(self, nome="funcionario", setor="vazio", cargo="vazio"):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        print(
            f"Meu nome {self.nome}, trabalho como {self.cargo} no setor de {self.setor}"
        )


funcionario = RH("Matheus", "TI", "Dev junio")

funcionario.apresentacao()


class pessoa(ABC):
    @abstractmethod
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1
        return self.idade

    @abstractmethod
    def estudar(self):
        pass


class aluno(pessoa):
    def __init__(self, nome="", idade=1, turma=1):
        super().__init__(nome, idade)
        self.turma = turma

    def infos(self):
        return f"Nome: {self.nome} com idade = {self.idade} da turma: {self.turma}"
    def estudar(self):
        return super().estudar()


aluno1 = aluno("Matheus", 21, 5)
print(aluno1.infos())
aluno1.aniversario()
print(aluno1.idade)
