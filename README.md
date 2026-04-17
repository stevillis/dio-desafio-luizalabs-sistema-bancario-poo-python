# 🏦 Desafio LuizaLabs - Sistema Bancário em POO com Python

Bem-vindo ao **Sistema Bancário em POO com Python** desenvolvido como parte do desafio da DIO (Digital Innovation One) em parceria com o LuizaLabs!

## 🎯 Situação

O desafio proposto exigia a construção e aperfeiçoamento de um Sistema Bancário utilizando as melhores práticas de **Programação Orientada a Objetos (POO)** na linguagem Python. Era mandatório evoluir a aplicação criando uma modelagem de domínio sólida.

## 🚀 Tarefa

A missão foi desenvolver uma aplicação robusta, escalável e de fácil interação, traduzindo o mundo real de clientes e contas bancárias para a infraestrutura de código, indo além de simples scripts e implementando uma interface limpa.

## 🛠️ Ação

Para transformar o desafio em uma aplicação de destaque, a solução foi dividida em duas grandes camadas:

1. **Backend POO:**
   O coração do sistema foi desenhado separando responsabilidades:
   - `PessoaFisica`: Mantém o registro do usuário.
   - `ContaCorrente`: Gerencia os parâmetros da conta (dados, limite de saque e número de saques diários).
   - `Historico` e Transações (`Saque`, `Deposito`): Modelam os eventos financeiros garantindo integridade.

2. **Frontend Interativo (Dashboard Web):**
   Substituímos o clássico terminal (CLI) por uma poderosa suíte interativa em **Streamlit**. Isso resultou numa interface gráfica intuitiva que abrange:
   - **Gestão de Perfil:** Criação de clientes e contas vinculadas.
   - **Operações Financeiras:** Telas para Depósito e Saque com feedback imediato e validação de regras de negócios.
   - **Extrato Visual:** Histórico de movimentações transformado em uma UI rica, clara e de fácil leitura.

## ✅ Resultado

O resultado é um sistema bancário moderno, 100% funcional, e testável através de mocks preestabelecidos. A adoção do _Streamlit_ eleva o projeto, tornando-o um diferencial em portfólios para entrevistas técnicas.

## 👉 Como Executar

### Preparação do Ambiente

1. Instale o Python 3.11.9 ou superior.

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

### Executando a Versão Web

Execute o painel principal com o comando:

```bash
streamlit run frontend/app.py
```

### Executando a Versão CLI

Execute a aplicação com o comando:

```bash
python frontend/cli.py
```

Utilize as opções do menu para navegar pelo sistema.
