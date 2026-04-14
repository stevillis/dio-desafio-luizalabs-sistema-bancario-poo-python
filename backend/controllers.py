from .cliente import PessoaFisica
from .conta import ContaCorrente
from .transacao import Deposito, Saque


def _rotear_transacao(clientes, tipo_transacao) -> None:
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return None

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return None

    valor_deposito = float(input("Informe o valor do depósito: "))
    transacao = tipo_transacao(valor_deposito)

    cliente.realizar_transacao(conta, transacao)


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta!")
        return None

    # FIXME: flitrar conta do cliente pelo número
    return cliente.contas[0]


def depositar(clientes):
    _rotear_transacao(clientes, Deposito)


def sacar(clientes):
    _rotear_transacao(clientes, Saque)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return None

    conta = recuperar_conta_cliente(cliente)
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


def criar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Já existe cliente com esse CPF!")
        return None

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, numero - bairro - cidade/siga estado): "
    )

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
    )

    clientes.append(cliente)

    print("\n===== Cliente criado com sucesso! =====")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado! Fluxo de criação de conta encerrado.")
        return None

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n===== Conta criada com sucesso! =====")
