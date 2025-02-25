import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 📌 Título do Dashboard
st.title("📊 Análises Univariadas e Bivariadas")

# 📌 Carregar os dados
@st.cache_data
def carregar_dados():
    return pd.read_csv("previsao_de_renda.csv")  # Substitua pelo caminho correto do seu dataset

renda = carregar_dados()

# 📌 Seleção de tipo de análise
analise_tipo = st.sidebar.selectbox("Selecione o Tipo de Análise", ["Univariada", "Bivariada"])

# 📌 Análise Univariada
if analise_tipo == "Univariada":
    st.header("📊 Análise Univariada")
    
    # Criar lista de variáveis numéricas
    variaveis_numericas = renda.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    # Selecionar variável para visualização
    variavel = st.selectbox("Escolha uma variável numérica:", variaveis_numericas)

    # 📌 Histograma
    st.subheader(f"Distribuição de {variavel}")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(renda[variavel], bins=30, kde=True, ax=ax)
    ax.set_xlabel(variavel)
    ax.set_ylabel("Frequência")
    ax.set_title(f"Histograma de {variavel}")
    st.pyplot(fig)

    # 📌 Boxplot (para detectar outliers)
    st.subheader(f"Boxplot de {variavel}")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.boxplot(x=renda[variavel], ax=ax)
    ax.set_title(f"Boxplot de {variavel}")
    st.pyplot(fig)

# 📌 Análise Bivariada
elif analise_tipo == "Bivariada":
    st.header("📊 Análise Bivariada")

    # Criar lista de variáveis numéricas
    variaveis_numericas = renda.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    # Selecionar variáveis para análise bivariada
    variavel_x = st.selectbox("Escolha a variável X:", variaveis_numericas)
    variavel_y = st.selectbox("Escolha a variável Y:", variaveis_numericas)

    # 📌 Scatterplot (Gráfico de Dispersão)
    st.subheader(f"Relação entre {variavel_x} e {variavel_y}")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.scatterplot(x=renda[variavel_x], y=renda[variavel_y], alpha=0.5, ax=ax)
    ax.set_title(f"Gráfico de Dispersão entre {variavel_x} e {variavel_y}")
    ax.set_xlabel(variavel_x)
    ax.set_ylabel(variavel_y)
    st.pyplot(fig)

    # 📌 Heatmap de Correlação (Corrigido)
    st.subheader("Matriz de Correlação")
    
    # Filtrar apenas colunas numéricas para evitar erro
    renda_numerico = renda.select_dtypes(include=['int64', 'float64'])

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(renda_numerico.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
    ax.set_title("Matriz de Correlação")
    st.pyplot(fig)

    # 📌 Boxplot de Comparação por Categoria
    variaveis_categoricas = renda.select_dtypes(include=['object', 'bool']).columns.tolist()
    categoria = st.selectbox("Escolha uma variável categórica:", variaveis_categoricas)

    st.subheader(f"Distribuição da Renda por {categoria}")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.boxplot(x=renda[categoria], y=renda["renda"], ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_title(f"Distribuição da Renda por {categoria}")
    st.pyplot(fig)
