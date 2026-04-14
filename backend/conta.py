from datetime import datetime
from .transacao import Saque


class Conta:
    def __init__(self, numero: int, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero(self) -> int:
        return self._numero

    @property
    def agencia(self) -> str:
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor) -> bool:
        if valor > self.saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            return False

        if valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True

        print("Operação falhou! O valor informado é inválido.")
        return False

    def depositar(self, valor) -> bool:
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True

        print("Operação falhou! O valor informado é inválido.")
        return False


class ContaCorrente(Conta):
    def __init__(
        self, numero: int, cliente, limite: float = 500, limite_saques: int = 3
    ):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor) -> bool:
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        if valor > self._limite:
            print("Operação falhou! O valor do saque excede o limite.")
            return False

        if numero_saques >= self._limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            return False

        return super().sacar(valor)

    def __str__(self):
        return f"""
        Agência:\t{self._agencia}
        C/C:\t{self._numero}
        Titular:\t{self.cliente.nome}"""


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self) -> list:
        return self._transacoes

    def adicionar_transacao(self, transacao) -> None:
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%y %H:%M:%S"),
            }
        )
