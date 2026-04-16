import streamlit as st


def get_clientes_from_session():
    if "clientes" not in st.session_state:
        st.session_state.clientes = []

    return st.session_state.clientes


def get_contas_from_session():
    if "contas" not in st.session_state:
        st.session_state.contas = []

    return st.session_state.contas
