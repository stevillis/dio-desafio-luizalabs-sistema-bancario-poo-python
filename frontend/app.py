import streamlit as st

if __name__ == "__main__":
    pages = {
        "": [
            st.Page("pages/home.py", title="Home"),
        ],
        "Cadastro de Usuário": [
            st.Page("pages/criar_cliente.py", title="Criar Cliente"),
        ],
        "Conta": [
            st.Page("pages/criar_conta.py", title="Criar Conta"),
            st.Page("pages/listar_contas.py", title="Listar Contas"),
        ],
        "Transação": [
            st.Page("pages/sacar.py", title="Sacar"),
            st.Page("pages/depositar.py", title="Depositar"),
        ],
        "Extrato": [
            st.Page("pages/extrato.py", title="Extrato"),
        ],
    }

    pg = st.navigation(pages)
    pg.run()
