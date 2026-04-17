import pandas as pd
import textwrap

from .cliente import PessoaFisica
from .conta import ContaCorrente
from .transacao import Deposito, Saque


class UIController:
    def __init__(self, clientes=None, contas=None):
        self._clientes = clientes if clientes is not None else []
        self._contas = contas if contas is not None else []

    @property
    def clientes(self):
        return self._clientes

    @property
    def contas(self):
        return self._contas


class CLIController(UIController):
    def filtrar_cliente(self, cpf):
        clientes_filtrados = [
            cliente for cliente in self.clientes if cliente.cpf == cpf
        ]
        return clientes_filtrados[0] if clientes_filtrados else None

    def recuperar_conta_cliente(self, cliente):
        if not cliente.contas:
            print("Cliente não possui conta!")
            return None

        # FIXME: flitrar conta do cliente pelo número
        return cliente.contas[0]

    def _rotear_transacao(self, tipo_transacao) -> None:
        cpf = input("Informe o CPF do cliente: ")
        cliente = self.filtrar_cliente(cpf)

        if not cliente:
            print("Cliente não encontrado!")
            return None

        conta = self.recuperar_conta_cliente(cliente)
        if not conta:
            return None

        valor_deposito = float(input("Informe o valor do depósito: "))
        transacao = tipo_transacao(valor_deposito)

        cliente.realizar_transacao(conta, transacao)

    def depositar(self):
        self._rotear_transacao(Deposito)

    def sacar(self):
        self._rotear_transacao(Saque)

    def exibir_extrato(self):
        cpf = input("Informe o CPF do cliente: ")
        cliente = self.filtrar_cliente(cpf)

        if not cliente:
            print("Cliente não encontrado!")
            return None

        conta = self.recuperar_conta_cliente(cliente)
        if not conta:
            return None

        print("\n==================== EXTRATO ====================")
        transacoes = conta.historico.transacoes

        extrato = ""
        if not transacoes:
            extrato = "Não foram realizadas movimentações."
        else:
            for transacao in transacoes:
                extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

        print(extrato)
        print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
        print("\n========================================")

    def criar_cliente(self):
        cpf = input("Informe o CPF do cliente: ")
        cliente = self.filtrar_cliente(cpf)

        if cliente:
            print("Já existe cliente com esse CPF!")
            return None

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (DD/MM/YYYY): ")
        endereco = input(
            "Informe o endereço (logradouro, numero - bairro - cidade/siga estado): "
        )

        cliente = PessoaFisica(
            nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco
        )

        self.clientes.append(cliente)

        print("\n===== Cliente criado com sucesso! =====")

    def criar_conta(self):
        cpf = input("Informe o CPF do cliente: ")
        cliente = self.filtrar_cliente(cpf)

        if not cliente:
            print("Cliente não encontrado! Fluxo de criação de conta encerrado.")
            return None

        numero_conta = len(self.contas) + 1
        conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
        self.contas.append(conta)
        cliente.contas.append(conta)

        print("\n===== Conta criada com sucesso! =====")

    def listar_contas(self):
        for conta in self.contas:
            print("=" * 100)
            print(textwrap.dedent(str(conta)))

    def menu(self):
        menu_str = """\n
        ==================== MENU ====================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova conta
        [lc]\tListar contas
        [nu]\tNovo usuário
        [q]\tSair
        => """
        return input(textwrap.dedent(menu_str))


class StreamlitController(UIController):
    def __init__(self, clientes, contas):
        super().__init__(clientes, contas)

    def filtrar_cliente(self, cpf):
        clientes_filtrados = [
            cliente for cliente in self.clientes if cliente.cpf == cpf
        ]
        return clientes_filtrados[0] if clientes_filtrados else None

    def criar_cliente(self, nome, cpf, data_nascimento, endereco):
        cliente = PessoaFisica(
            nome=nome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            endereco=endereco,
        )

        self.clientes.append(cliente)

    def criar_conta(self, cliente):
        numero_conta = len(self.contas) + 1
        conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
        self.contas.append(conta)
        cliente.contas.append(conta)

    def listar_contas(self):
        numeros_list = []
        agencias_list = []
        titulares_list = []
        for conta in self.contas:
            numeros_list.append(conta.numero)
            agencias_list.append(conta.agencia)
            titulares_list.append(conta.cliente.nome)

        return pd.DataFrame(
            {
                "Agência": agencias_list,
                "Titular": titulares_list,
                "C/C": numeros_list,
            }
        )
