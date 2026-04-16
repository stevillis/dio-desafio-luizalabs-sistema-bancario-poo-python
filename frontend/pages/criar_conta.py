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

    with st.form("cadastro_cliente"):
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

                    st.balloons()

                    st.success(
                        "Conta criada com sucesso! Redirecionando para a página inicial..."
                    )

                    time.sleep(3)

                    st.switch_page("pages/home.py")
