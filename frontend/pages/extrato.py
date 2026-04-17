import sys
import streamlit as st

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
        page_icon="📋",
    )

    st.title("Extrato")

    with st.form("extrato_form"):
        cpf = st.text_input(
            label="CPF:",
            max_chars=11,
            placeholder="Informe o CPF do cliente",
        )

        if st.form_submit_button("Exibir extrato"):
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
                        transacoes = conta.historico.transacoes

                        st.subheader("Extrato Bancário", divider="gray")

                        if not transacoes:
                            st.info("Não foram realizadas movimentações nesta conta.")
                        else:
                            for transacao in transacoes:
                                tipo = transacao["tipo"]
                                valor = transacao["valor"]

                                is_saque = "saque" in str(tipo).lower()
                                color = "red" if is_saque else "green"
                                prefix = "-" if is_saque else "+"

                                col1, col2 = st.columns([3, 1])
                                with col1:
                                    st.markdown(f"**{tipo}**")
                                with col2:
                                    st.markdown(
                                        f"**:{color}[{prefix} R$ {valor:.2f}]**"
                                    )

                        st.divider()
                        st.metric(label="Saldo Atual", value=f"R$ {conta.saldo:.2f}")
