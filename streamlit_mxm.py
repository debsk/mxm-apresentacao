import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np


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

st.markdown(
    """
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
    </style>
    """, unsafe_allow_html=True
)

# Header principal
st.markdown("<h1 style='color:#002f6c;'>MXM Sistemas</h1>", unsafe_allow_html=True)

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

    # Dados
    anos = [2010, 2012, 2014, 2016, 2018, 2020]
    adocao_si = [2, 4, 6, 7, 9, 10]

    # Estilo de fontes e layout
    plt.style.use('seaborn-v0_8-darkgrid')  # Usando um estilo predefinido para o fundo e as linhas

    # Criando o gráfico
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plotando a linha (com suavização para um visual mais moderno)
    ax.plot(anos, adocao_si, marker='o', color='#1f77b4', linestyle='-', linewidth=2, markersize=8, label="Adoção de Sistemas de Informação")

    # Adicionando título e rótulos
    ax.set_title("Evolução da Adoção de Sistemas de Informação (SI)", fontsize=18, fontweight='bold', family='sans-serif')
    ax.set_xlabel("Ano", fontsize=14, fontweight='bold', family='sans-serif')
    ax.set_ylabel("Número de Empresas Adotando SI", fontsize=14, fontweight='bold', family='sans-serif')

    # Adicionando uma legenda no canto superior direito
    ax.legend(loc='upper left', fontsize=12)

    # Adicionando rótulos nos pontos
    for i, txt in enumerate(adocao_si):
        ax.annotate(txt, (anos[i], adocao_si[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=12, color='black')

    # Melhorando a visualização: adicionando a grade, ajustando ticks
    ax.grid(True, linestyle='--', alpha=0.6)

    # Ajuste de escala dos eixos
    ax.set_xticks(np.arange(2010, 2021, 2))
    ax.set_yticks(np.arange(0, 12, 2))

    # Exibindo o gráfico
    st.pyplot(fig)

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

    # Gráfico interativo de tipos de sistemas
    st.subheader("Distribuição de Tipos de Sistemas de Informação")
    systems_data = pd.DataFrame({
        "Sistema": ["SPT", "SIG", "SAD", "Estratégicos"],
        "Proporção": [35, 25, 20, 20]
    })
    fig = px.pie(systems_data, names='Sistema', values='Proporção', title="Proporção de Tipos de SI na MXM")
    st.plotly_chart(fig)

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
    - 🗃️ **Bancos de Dados**: Oracle e Oracle/Amazon RDS

    **Ferramentas de Colaboração:**

    - Internamente: Pacote Office, Microsoft Teams  
    - Externamente: Plataformas SaaS com acesso remoto seguro

    Com essas tecnologias, a MXM promove **agilidade, inovação e conectividade contínua** com seus clientes.
    """)

    # Exemplo de ícones interativos
    st.subheader("Tecnologias Usadas")
    st.write("Clique nas opções abaixo para saber mais sobre cada tecnologia utilizada pela MXM:")

    tecnologia = st.selectbox("Escolha uma tecnologia", ["Pacote Office", "Microsoft Teams", "SAU", "Oracle/Amazon RDS"])

    if tecnologia == "Pacote Office":
        st.markdown("<h4><i class='fas fa-file-alt'></i> Pacote Office</h4>", unsafe_allow_html=True)
        st.write("""
        O **Pacote Office** é uma suíte de aplicativos de produtividade amplamente utilizada em empresas de todos os tamanhos.
        A MXM utiliza as ferramentas do **Office** para otimizar suas operações administrativas e de comunicação. Entre os principais aplicativos usados:
        
        - **Excel**: Para criação e gestão de planilhas financeiras, controle de estoque, relatórios de performance e muito mais.
        - **PowerPoint**: Para criação de apresentações corporativas e relatórios executivos.
        - **Word**: Para elaboração de documentos formais, como relatórios, contratos e manuais internos.
        
        Essas ferramentas ajudam na organização de informações, melhorando a eficiência no processamento de dados e na criação de conteúdos gerenciais.
        """)
    elif tecnologia == "Microsoft Teams":
        st.markdown("<h4><i class='fab fa-microsoft'></i> Microsoft Teams</h4>", unsafe_allow_html=True)
        st.write("""
        O **Microsoft Teams** é uma plataforma de colaboração usada para comunicação interna, reuniões online e troca de informações em tempo real.
        A MXM utiliza o **Teams** para facilitar a interação entre os membros da equipe, promovendo um ambiente de trabalho mais ágil e integrado. As principais funcionalidades incluem:
        
        - **Chats e Mensagens Instantâneas**: Para comunicação rápida e eficiente entre os membros da equipe.
        - **Reuniões Virtuais**: Organizar e participar de reuniões online com funcionários, clientes e parceiros.
        - **Armazenamento de Arquivos**: Compartilhar e colaborar em documentos em tempo real, diretamente dentro da plataforma.
        
        O Teams facilita a colaboração entre os times e assegura que todos os envolvidos em um projeto tenham fácil acesso a informações e atualizações em tempo real.
        """)
    elif tecnologia == "SAU":
        st.markdown("<h4><i class='fas fa-ticket-alt'></i> Sistema de Abertura de Chamados (SAU)</h4>", unsafe_allow_html=True)
        st.write("""
        O **Sistema de Abertura de Chamados (SAU)** é utilizado pela MXM para registrar, monitorar e gerenciar demandas de suporte, manutenção e solicitações de clientes ou colaboradores.
        Esse sistema garante que todas as solicitações sejam atendidas de maneira organizada e eficiente. As funcionalidades principais incluem:
        
        - **Registro de Chamados**: Permite que os usuários abram chamados para relatar problemas ou solicitar serviços.
        - **Acompanhamento de Chamados**: Usuários e equipes de suporte podem acompanhar o status e a evolução de cada chamado em tempo real.
        - **Gestão de Prioridades**: O sistema permite priorizar chamados com base na urgência ou impacto no negócio.
        
        Esse sistema assegura a qualidade no atendimento e melhora a eficiência da resolução de problemas internos e externos.
        """)
    elif tecnologia == "Oracle/Amazon RDS":
      st.markdown("<h4><i class='fas fa-database'></i> Oracle/Amazon RDS</h4>", unsafe_allow_html=True)
      st.write("""
      O **Oracle** e o **Amazon RDS (Relational Database Service)** são bancos de dados robustos utilizados pela MXM para garantir a integridade, segurança e escalabilidade das informações.
      Essas soluções de gerenciamento de banco de dados relacional sustentam os principais sistemas da empresa, como o ERP MXM-WebManager. Entre suas funcionalidades, destacam-se:
      
      - **Armazenamento de Dados**: Armazenam dados críticos como transações financeiras, controle de estoque, cadastros de clientes e fornecedores.
      - **Performance de Consultas**: Permitem consultas eficientes e de alta performance, essenciais para relatórios e análises em tempo real.
      - **Alta Disponibilidade e Backup**: Ambos oferecem soluções robustas de replicação, segurança e backup automatizado para garantir continuidade e proteção dos dados.
      - **Linguagens Utilizadas**: Utilizam as linguagens **SQL** (Structured Query Language) e **PL/SQL** (Procedural Language/SQL, exclusiva do Oracle) para manipulação e programação dentro do banco de dados.

      Com essa infraestrutura, a MXM assegura operações confiáveis, com alta disponibilidade e capacidade de crescimento escalável.
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

    # Gráfico de Radar para análise das Forças de Porter
    st.subheader("Forças de Porter: Radar Competitivo")

    porter_data = pd.DataFrame({
        'Força': ['Rivalidade', 'Ameaça de Novos Entrantes', 'Ameaça de Substitutos', 'Poder dos Fornecedores', 'Poder dos Clientes'],
        'Intensidade': [8, 6, 5, 6, 9]
    })

    fig = px.line_polar(
        porter_data,
        r='Intensidade',
        theta='Força',
        line_close=True,
        title='Análise de Porter',
        template='plotly'  # Tema mais legível
    )

    fig.update_traces(fill='toself', line_color='blue')

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                tickfont=dict(color='white')
            ),
            angularaxis=dict(
                tickfont=dict(color='white')
            )
        ),
        font=dict(color='white'),
        paper_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        plot_bgcolor='rgba(0,0,0,0)'    # Fundo do gráfico também transparente
    )

    st.plotly_chart(fig)

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
