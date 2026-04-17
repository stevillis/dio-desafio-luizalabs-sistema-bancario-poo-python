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
        page_title="Desafio Luizalabs - Sistema Bancário em POO com Python",
        page_icon="🐖",
    )

    st.title("Depositar")

    if "depositar_form_loaded" not in st.session_state:
        st.session_state["depositar_form_loaded"] = False

    if not st.session_state["depositar_form_loaded"]:
        if st.button(label="Novo Depósito", type="secondary", use_container_width=True):
            st.session_state["depositar_form_loaded"] = True
            st.rerun()
    else:
        with st.form("depositar_form"):
            cpf = st.text_input(
                label="CPF:",
                max_chars=11,
                placeholder="Informe o CPF do cliente",
                key="cpf_widget",
            )

            valor_deposito = st.number_input(
                "Informe o valor do depósito",
                min_value=0.0,
                max_value=5000.0,
                step=10.0,
            )

            if st.form_submit_button("Depositar"):
                if not cpf:
                    st.error("O CPF é obrigatório!")
                else:
                    cliente = streamlit_controller.filtrar_cliente(cpf)
                    if not cliente:
                        st.error("Cliente não encontrado!")
                    else:
                        conta = streamlit_controller.recuperar_conta_cliente(
                            cliente=cliente
                        )
                        if not conta:
                            st.error("Cliente não possui conta!")
                        else:
                            if conta:
                                if valor_deposito > 0:
                                    sucesso, mensagem = streamlit_controller.depositar(
                                        cliente=cliente,
                                        conta=conta,
                                        valor_deposito=valor_deposito,
                                    )
                                    if sucesso:
                                        st.success(mensagem)
                                        time.sleep(2)
                                        del st.session_state["depositar_form_loaded"]
                                        st.rerun()
                                    else:
                                        st.error(mensagem)
                                else:
                                    st.error(
                                        "O valor do depósito deve ser maior que zero!"
                                    )

        if st.button(label="Voltar", use_container_width=True, type="tertiary"):
            del st.session_state["depositar_form_loaded"]
            st.rerun()
