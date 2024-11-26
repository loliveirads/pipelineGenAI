import streamlit as st
from datetime import datetime, time

def main():

    st.title("Sistema de CRM e Vendas da ZapFlow - FrontEnd Simples")
    vendedor = st.text_input("Campo de texto para inserção do vendedor")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Campo para selecionar a data que a venda foi realizada", datetime.now())
    hora = st.time_input("Campo para selecionar a hora que a venda foi realizada")
    valor = st.number_input("Campo numérico para inserir o valor monetário da venda", min_value=0.0, format='%.2f')
    quantidade =st.number_input("Campo numérico para inserir a quantidade de produtos vendidos", min_value=1, step=1)
    produto = st.selectbox("Campo de seleção para escolher o produto vendido",["zapflow com Gemini", "zapflow com groq", "zapflow com gpt"])

    if st.button("Salvar"):

        data_hora = datetime.combine(data, hora)
        st.write("**Dados da Venda:**")
        st.write(f"Email do Vendedor: {email}")
        st.write(f"Data e Hora da Compra: {data_hora}")
        st.write(f"Valor da Venda: R$ {valor:.2f}")
        st.write(f"Quantidade de Produtos: {quantidade}")
        st.write(f"Produto: {produto}")


if __name__=="__main__":
    main()