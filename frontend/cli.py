import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


from backend.controllers import CLIController


def main():
    cli_controller = CLIController()

    while True:
        opcao = cli_controller.menu()

        if opcao == "d":
            cli_controller.depositar()
        elif opcao == "s":
            cli_controller.sacar()
        elif opcao == "e":
            cli_controller.exibir_extrato()
        elif opcao == "nu":
            cli_controller.criar_cliente()
        elif opcao == "nc":
            cli_controller.criar_conta()
        elif opcao == "lc":
            cli_controller.listar_contas()
        elif opcao == "q":
            break
        else:
            print(
                "Operação inválida! Por favor, selecione novamente a operação desejada."
            )


if __name__ == "__main__":
    main()
