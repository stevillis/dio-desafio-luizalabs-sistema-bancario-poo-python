import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


from backend.controllers import (
    criar_conta,
    criar_cliente,
    depositar,
    exibir_extrato,
    sacar,
)


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def menu():
    menu = """\n
    ==================== MENU ====================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta=numero_conta, clientes=clientes, contas=contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print(
                "Operação inválida! Por favor, selecione novamente a operação desejada."
            )


if __name__ == "__main__":
    main()
