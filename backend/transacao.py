from abc import (
    ABC,
    abstractmethod,
)


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self): ...

    @classmethod
    @abstractmethod
    def registrar(self, conta): ...


class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta) -> None:
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta) -> None:
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)
