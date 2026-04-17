import sys
import streamlit as st
import time

from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from backend.controllers import StreamlitController
from frontend.session_manager import get_clientes_from_session, get_contas_from_session

if __name__ == "__main__":
    clientes = get_clientes_from_session()
    contas = get_contas_from_session()

    streamlit_controller = StreamlitController(clientes, contas)

    st.set_page_config(
        page_title="Desafio LuizaLabs - Sistema Bancário em POO com Python",
        page_icon="📝",
    )

    st.title("Criar Conta")

    if "criar_conta_form_loaded" not in st.session_state:
        st.session_state["criar_conta_form_loaded"] = False

    if not st.session_state["criar_conta_form_loaded"]:
        if st.button(label="Nova Conta", type="secondary", use_container_width=True):
            st.session_state["criar_conta_form_loaded"] = True
            st.rerun()
    else:
        with st.form("cadastro_conta"):
            cpf = st.text_input(
                label="CPF:",
                max_chars=11,
                placeholder="Informe o CPF do cliente",
            )

            if st.form_submit_button("Criar Conta", type="secondary"):
                if not cpf:
                    st.error("O CPF é obrigatório!")

                if cpf:
                    cliente = streamlit_controller.filtrar_cliente(cpf)
                    if not cliente:
                        st.error(
                            "Cliente não encontrado! Fluxo de criação de conta encerrado."
                        )
                    else:
                        streamlit_controller.criar_conta(cliente=cliente)

                        st.success("Conta criada com sucesso!")
                        time.sleep(2)
                        del st.session_state["criar_conta_form_loaded"]
                        st.rerun()

        if st.button(label="Voltar", use_container_width=True, type="tertiary"):
            del st.session_state["criar_conta_form_loaded"]
            st.rerun()
