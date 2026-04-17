import streamlit as st
import time
import sys

from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from backend.controllers import StreamlitController
from frontend.session_manager import get_clientes_from_session, get_contas_from_session


if __name__ == "__main__":
    clientes = get_clientes_from_session()
    contas = get_contas_from_session()

    streamlit_controller = StreamlitController(clientes, contas)

    st.set_page_config(
        page_title="Desafio Luizalabs - Sistema Bancário em POO com Python",
        page_icon="📝",
    )

    st.title("Criar Cliente")

    if "criar_cliente_form_loaded" not in st.session_state:
        st.session_state["criar_cliente_form_loaded"] = False

    if not st.session_state["criar_cliente_form_loaded"]:
        if st.button(label="Novo Cliente", type="secondary", use_container_width=True):
            st.session_state["criar_cliente_form_loaded"] = True
            st.rerun()
    else:
        with st.form("cadastro_cliente"):
            nome = st.text_input(
                label="Nome Completo:",
                max_chars=150,
                placeholder="Informe o nome completo",
            )

            cpf = st.text_input(
                label="CPF:",
                max_chars=11,
                placeholder="Informe o CPF do cliente",
            )

            data_nascimento = st.date_input(
                label="Data de Nascimento:",
                min_value=date(1900, 1, 1),
                max_value="today",
                format="DD/MM/YYYY",
            )

            endereco = st.text_area(
                label="Endereço:",
                max_chars=200,
                placeholder="Informe o endereço (logradouro, numero - bairro - cidade/sigla estado)",
            )

            if st.form_submit_button("Criar Cliente", type="secondary"):
                if not nome:
                    st.error("O Nome é obrigatório!")
                if not cpf:
                    st.error("O CPF é obrigatório!")

                if cpf and nome:
                    cliente_existente = streamlit_controller.filtrar_cliente(cpf)
                    if cliente_existente:
                        st.error("Já existe cliente com esse CPF!")
                    else:
                        streamlit_controller.criar_cliente(
                            nome,
                            cpf,
                            data_nascimento.strftime("%d/%m/%Y"),
                            endereco,
                        )

                        st.success("Cliente criado com sucesso!")
                        time.sleep(2)
                        del st.session_state["criar_cliente_form_loaded"]
                        st.rerun()

        if st.button(label="Voltar", use_container_width=True, type="tertiary"):
            del st.session_state["criar_cliente_form_loaded"]
            st.rerun()
