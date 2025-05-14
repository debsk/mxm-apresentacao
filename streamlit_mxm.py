import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="MXM Sistemas", layout="wide", page_icon="📊")

# Estilo visual básico
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .sidebar .sidebar-content {
        background-color: #002f6c;
        color: white;
    }
    .css-1d391kg {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header principal
st.markdown("<h1 style='color:#002f6c;'>MXM Sistemas</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#005baa;'>Transformando dados em decisões inteligentes</h3>", unsafe_allow_html=True)

# Menu lateral
menu = st.sidebar.radio("🔷 Navegue pela apresentação", [
    "📌 Introdução e SI",
    "🧩 Modelo de Negócio + Tipos de Sistemas",
    "💼 Soluções e Colaboração",
    "📈 Forças de Porter e Benefícios",
    "📍 Localização"
])

# Seções do site conforme roteiro

if menu == "📌 Introdução e SI":
    st.header("📌 Introdução + Sobre Sistemas de Informação")
    st.markdown("""
    - Este trabalho foi desenvolvido por Mel, Leticia, Débora e Stefani.  
    - O tema é **Sistemas de Informação (SI)**.  
    - Sistemas de Informação são essenciais para coletar, processar e transformar dados em conhecimento, apoiando empresas em decisões estratégicas.
    - A **MXM Sistemas** é um exemplo prático de como os SI transformam a operação de empresas, por meio de soluções robustas, como o ERP MXM-WebManager.
    """)

elif menu == "🧩 Modelo de Negócio + Tipos de Sistemas":
    st.header("🧩 Modelo de Negócio da MXM + Tipos de Sistemas")
    st.markdown("""
    A **MXM Sistemas** atua no modelo B2B, desenvolvendo soluções tecnológicas para empresas de todos os portes.  
    Seu principal produto é o **MXM-WebManager**, um ERP 100% web, que centraliza a gestão de diferentes áreas da empresa: fiscal, contábil, estoque, compras, financeiro, RH e muito mais.

    A empresa mantém uma **estrutura enxuta, inovadora e tecnológica**, o que permite flexibilidade e adaptação constante.

    **Tipos de Sistemas de Informação utilizados pela MXM:**

    - 💳 **SPT - Sistemas de Processamento de Transações**  
      Gerenciam operações como faturamento, compras e pagamentos.
    
    - 📋 **SIG - Sistemas de Informação Gerencial**  
      Apoiam gestores com relatórios operacionais e de desempenho.

    - 📊 **SAD - Sistemas de Apoio à Decisão**  
      Incluem ferramentas de BI para análise de indicadores estratégicos.

    - 🧠 **Sistemas Estratégicos**  
      O ERP da MXM se diferencia pela integração total, inteligência fiscal e facilidade de uso, sendo um diferencial competitivo no mercado.

    """)

elif menu == "💼 Soluções e Colaboração":
    st.header("💼 Soluções e Tecnologias Usadas + Ferramentas de Colaboração")
    st.markdown("""
    **Soluções da MXM:**

    - **ERP MXM-WebManager**  
      ERP 100% web com estrutura modular, pronto para ambientes multiempresa e multissetorial, disponível como SaaS ou instalação própria.

    - **BPMS - Gestão de Processos**  
      Automatiza e digitaliza fluxos, reduzindo retrabalho e aumentando controle operacional.

    - **BI Integrado (Business Intelligence)**  
      Dashboards e relatórios dinâmicos para gestão orientada por dados.

    - **Consultoria, suporte e capacitação**  
      Equipe especializada para acompanhar a implementação e evolução dos sistemas.

    **Tecnologias utilizadas no dia a dia:**

    - 📦 **Pacote Office**  
    - 💬 **Microsoft Teams**  
    - 🗂️ **SAU (Sistema de Abertura de Chamados)**  
    - 🗃️ **Bancos de Dados**: Oracle e MariaDB

    **Ferramentas de Colaboração:**

    - Internamente: Slack, Microsoft Teams  
    - Externamente: plataformas SaaS com acesso remoto seguro

    Com essas tecnologias, a MXM promove **agilidade, inovação e conectividade contínua** com seus clientes.
    """)

elif menu == "📈 Forças de Porter e Benefícios":
    st.header("📈 Forças Competitivas de Porter + Benefícios")
    st.markdown("""
    **Análise de Porter para a MXM Sistemas:**

    - ⚔️ **Rivalidade entre concorrentes**  
      Elevada. Mercado competitivo com diversos fornecedores de ERP no Brasil.

    - 🚪 **Ameaça de novos entrantes**  
      Moderada. Exige conhecimento técnico, investimento em infraestrutura e construção de credibilidade.

    - 🔄 **Ameaça de produtos substitutos**  
      Existe (softwares gratuitos ou genéricos), mas com limitações em escalabilidade, suporte e segurança.

    - 🔌 **Poder de barganha dos fornecedores**  
      Moderado. A MXM depende de infraestrutura robusta de TI e data centers.

    - 🧾 **Poder de barganha dos clientes**  
      Alto. Clientes têm muitas opções e exigem soluções completas e customizadas.

    **Benefícios gerados aos clientes da MXM:**

    - ✅ Redução de custos com automatização de processos  
    - ✅ Acesso em tempo real às informações da empresa  
    - ✅ Cumprimento de obrigações fiscais com mais segurança  
    - ✅ Apoio à gestão estratégica com relatórios e BI  
    - ✅ Flexibilidade para operar de forma remota e segura

    **Conclusão:**  
    A MXM se destaca por entregar soluções completas em gestão empresarial, apoiadas por sistemas de informação modernos, que permitem inovação, conformidade e escalabilidade.
    """)

elif menu == "📍 Localização":
    st.header("📍 Localização das Sedes da MXM Sistemas")
    st.markdown("Veja abaixo as principais unidades da empresa:")

    # Dados das sedes com coordenadas aproximadas
    sedes = pd.DataFrame({
        'local': [
            'Matriz - Niterói/RJ',
            'Filial - Rio de Janeiro/RJ',
            'Filial - São Paulo/SP',
            'Filial - Salvador/BA',
            'Filial - Porto Alegre/RS'
        ],
        'lat': [-22.8915, -22.9068, -23.5614, -12.9818, -30.0277],
        'lon': [-43.1216, -43.1764, -46.6564, -38.4820, -51.2287]
    })

    st.map(sedes)

    st.markdown("""
    - 🏢 **Matriz – Niterói/RJ**  
      Av. Ernani do Amaral Peixoto, 500, Centro  
    - 🏢 **Filial – Rio de Janeiro/RJ**  
      Av. Rio Branco, 131, 16º andar, Centro  
    - 🏢 **Filial – São Paulo/SP**  
      Alameda Santos, 2326, Salas 151 e 152  
    - 🏢 **Filial – Salvador/BA**  
      Av. Tancredo Neves, 620, Sala 3305  
    - 🏢 **Filial – Porto Alegre/RS**  
      Rua Mostardeiro, 366, Conj. 501
    """)

    st.write("🔗 [Site Oficial da MXM](https://www.mxm.com.br)")