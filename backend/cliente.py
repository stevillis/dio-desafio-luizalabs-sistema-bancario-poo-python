from datetime import datetime


class Cliente:
    def __init__(self, endereco: str) -> None:
        self._endereco = endereco
        self._contas = []

    @property
    def contas(self) -> list:
        return self._contas

    def realizar_transacao(self, conta, transacao) -> None:
        transacao.registrar(conta)

    def adicionar_conta(self, conta) -> None:
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        self.cpf = cpf
