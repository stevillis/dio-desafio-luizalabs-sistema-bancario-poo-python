import json
import streamlit as st
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))


from backend.cliente import PessoaFisica
from backend.conta import ContaCorrente

BASE_PATH = Path(__file__).parent.parent.parent / "mocks"


def mock_clientes():
    with open(file=BASE_PATH / "cliente.json", mode="r", encoding="utf-8") as f:
        clientes_json = json.load(f)

    clientes = []
    for cliente_json in clientes_json:
        cliente = PessoaFisica(
            nome=cliente_json["nome"],
            cpf=cliente_json["cpf"],
            data_nascimento=cliente_json["data_nascimento"],
            endereco=cliente_json["endereco"],
        )
        clientes.append(cliente)

    st.session_state.clientes = clientes


def mock_contas():
    with open(file=BASE_PATH / "conta.json", mode="r", encoding="utf-8") as f:
        contas_json = json.load(f)

    contas = []
    for conta_json in contas_json:
        cliente = [
            cliente
            for cliente in st.session_state.clientes
            if cliente.cpf == conta_json["cliente_cpf"]
        ][0]

        if cliente:
            conta = ContaCorrente(
                numero=conta_json["numero"],
                cliente=cliente,
                limite=conta_json["limite"],
                limite_saques=conta_json["limite_saques"],
            )
            contas.append(conta)
            cliente.adicionar_conta(conta)

    st.session_state.contas = contas


if __name__ == "__main__":
    if "mocks_carregados" not in st.session_state:
        mock_clientes()
        mock_contas()

        st.session_state.mocks_carregados = True

    st.set_page_config(
        page_title="Desafio LuizaLabs - Sistema Bancário em POO com Python",
        page_icon="🐍",
        layout="wide",
    )

    st.title("🏦 Desafio LuizaLabs - Sistema Bancário em POO")

    st.markdown("""
    ### Bem-vindo ao Sistema Bancário em POO com Python!

    O desafio proposto pela DIO (Digital Innovation One) em parceria com o LuizaLabs exigia a evolução do Sistema Bancário apresentado no Bootcamp Luizalabs - Back-end com Python - 2º Edição, aprofundando o uso de Programação Orientada a Objetos (POO) em Python.

    O objetivo foi melhorar a aplicação bancária em formato CLI apresentada no Bootcamp, tornando-a mais robusta, escalável e interativa, modelando entidades do mundo real (Clientes, Contas, Transações) de maneira elegante e com código limpo.

    Para atender ao desafio, dividi o projeto em Backend e Frontend:
    - **Backend POO:** Domínio completo construído com classes e princípios sólidos de Orientação a Objetos.
    - **Frontend Interativo:** Criei este dashboard web moderno utilizando **Streamlit**, mantendo a antiga interface de linha de comando (CLI) e disponbilizando também uma experiência visual rica com esta aplicação web.

    Um sistema bancário totalmente funcional e intuitivo. Entre as funcionalidades principais desenvolvidas, estão:
    - 👤 **Gestão de Clientes e Contas:** Cadastro e visualização de clientes e contas.
    - 💸 **Operações Financeiras:** Saques e Depósitos com validações, regras de negócio e limites diários.
    - 📄 **Extrato Dinâmico:** Acompanhamento claro e formatado do histórico de cada conta.

    ---
    ### O que você está esperando?
    👉 **Navegue pelas abas laterais** para explorar o sistema.

    ℹ️ Alguns dados já foram pré-carregados para simular operações reais.
    """)
