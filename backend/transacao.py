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

    def registrar(self, conta):
        sucesso, mensagem = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

        return sucesso, mensagem


class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self) -> float:
        return self._valor

    def registrar(self, conta):
        sucesso, mensagem = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

        return sucesso, mensagem
