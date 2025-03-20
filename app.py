import streamlit as st

# Configuração inicial da página
st.set_page_config(page_title="Calculadora de Turnover", page_icon="📊", layout="centered")

# Título da aplicação
st.title("📊 Calculadora de Turnover")

st.write("Preencha os campos abaixo para calcular o percentual de turnover:")

# Entrada de valores
colaboradores_ativos = st.number_input("Número de colaboradores ativos", min_value=1, step=1)
admissoes = st.number_input("Número de admissões", min_value=0, step=1)
demissoes = st.number_input("Número de demissões", min_value=0, step=1)

# Botão de cálculo
if st.button("Calcular Turnover"):
    if colaboradores_ativos > 0:
        turnover = ((admissoes + demissoes) / 2) / colaboradores_ativos * 100
        
        if turnover > 5:
            st.error(f"⚠️ O turnover é de **{turnover:.2f}%**. 🚨 Passou de 5%! Você não entregaria a meta.")
        else:
            st.success(f"✅ O turnover é de **{turnover:.2f}%**. Dentro do limite permitido!")

    else:
        st.error("O número de colaboradores ativos deve ser maior que zero.")