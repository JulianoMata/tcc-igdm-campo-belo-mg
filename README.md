# 📊 Otimização de Receita Pública com Data Science - Campo Belo/MG

> **Projeto de TCC (Ciência de Dados e Inteligência Artificial)**
> Como a gestão pública orientada a dados e a eficiência operacional podem blindar e expandir os repasses financeiros federais (IGD-M) do município.

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Pandas](https://img.shields.io/badge/Lib-Pandas-150458) ![Power BI](https://img.shields.io/badge/Dashboards-Power_BI-yellow) ![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Sobre o Projeto

Este repositório contém o desenvolvimento de um projeto aplicado de **Ciência de Dados e Inteligência Artificial** voltado à **Gestão Pública Municipal**.

O Cadastro Único (CadÚnico) e o acompanhamento das condicionalidades do Programa Bolsa Família constituem os pilares de sustentação dos recursos socioassistenciais no Brasil. Contudo, descontinuidades de fluxos e defasagens cadastrais geram perdas financeiras silenciosas para as prefeituras.

Através da extração, engenharia de dados defensiva, análise estatística e simulação de cenários com dados abertos do Governo Federal, este projeto comprova empiricamente que a **eficiência técnica da equipe de ponta é um vetor direto de captação e blindagem orçamentária**.

O resultado final é um ecossistema analítico capaz de apoiar a tomada de decisão estratégica dos gestores de **Campo Belo/MG**, mitigando glosas fiscais e maximizando os repasses do **Índice de Gestão Descentralizada Municipal (IGD-M)**.

---

## 📈 Dashboard Interativo

A visualização executiva dos indicadores orçamentários, histórico de repasses e do **Tripé da Qualidade (Educação, Saúde e Cadastro Único)** está publicada em um painel interativo:

[![Acessar Dashboard Power BI](https://img.shields.io/badge/Acessar_Dashboard-Power_BI_Online-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://app.powerbi.com/view?r=eyJrIjoiMDVlMTI1NWYtODYzMy00MmE1LTkxNjAtNmEzZWM3Mzg2MWNiIiwidCI6IjE4MzJhNTBkLWZmYWYtNDhiYi1iM2NjLWU4MDk3ZWM4NGVlZiJ9)

> 🔗 **Link direto:** [Visualizar Painel Interativo no Power BI](https://app.powerbi.com/view?r=eyJrIjoiMDVlMTI1NWYtODYzMy00MmE1LTkxNjAtNmEzZWM3Mzg2MWNiIiwidCI6IjE4MzJhNTBkLWZmYWYtNDhiYi1iM2NjLWU4MDk3ZWM4NGVlZiJ9)

---

## 🎯 O Problema de Negócio

Muitos gestores municipais tratam as transferências federais de apoio à gestão como transferências passivas e automáticas. Contudo, o **IGD-M** opera sob uma lógica de desempenho: **o valor repassado varia de 0% a 100% da cota máxima**, condicionado diretamente à eficiência operacional do município.

* **A Fragilidade Oculta:** Quedas na atualização cadastral ou na pesagem de saúde geram glosas orçamentárias imediatas, drenando recursos sem aviso prévio.
* **O Objetivo Estratégico:** Analisar a série histórica de **2019 a 2026** de Campo Belo/MG para mapear gargalos operacionais, mensurar o custo de oportunidade da ineficiência e demonstrar matematicamente o Retorno sobre o Investimento (ROI) de ações preventivas de busca ativa.

---

## 📂 Fonte dos Dados (Data Source)

Os dados utilizados são de acesso público e foram extraídos do **Portal de Dados Abertos do Governo Federal** (Ministério do Desenvolvimento e Assistência Social, Família e Combate à Fome - MDS).

O desafio central de **Engenharia de Dados** residiu na fragmentação e volatilidade dos esquemas ao longo dos anos. Foi desenvolvido um pipeline automatizado para coletar, higienizar e sincronizar três matrizes matriciais anuais distintas (**Taxas de Qualidade**, **Valores Calculados** e **Públicos Totais**), unificando-as em uma série temporal contínua e normalizada.

* **Fonte Oficial:** [Índice de Gestão Descentralizada (IGD-M) — dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/indice-de-gestao-descentralizada-dos-municipios---igd-m)
* **Janela Temporal Consolidada:** Janeiro de 2019 a Abril de 2026 (88 competências mensais).
* **Escopo Geográfico:** Município de **Campo Belo/MG** (Código IBGE: `311120`).
* **Privacidade e Governança:** Dados estritamente agregados e anonimizados na fonte, em plena conformidade com as diretrizes da Lei Geral de Proteção de Dados Pessoais (LGPD).

---

## 🗂 Estrutura do Projeto

```text
TCC_CAMPOBELO/
├── dados_brutos/          # Matrizes originais do Governo Federal (Ignoradas no Git)
│   ├── CALCULOS/          # Histórico de valores liquidados e repassados
│   ├── PUBLICO/           # Quantitativos de famílias e metas de público-alvo
│   └── TAXAS/             # Índices e taxas de cobertura das condicionalidades
├── dados_tratados/        # Datasets consolidados e relatórios de auditoria
│   ├── dataset_financeiro_tratado.pkl   # Base tratada serializada (preserva tipagem para Python)
│   ├── dataset_financeiro_tratado.xlsx  # Base tratada em Excel (camada de consumo e BI)
│   ├── dicionario_dados.csv             # Matriz de metadados das variáveis tratadas
│   └── relatorio_colunas.txt            # Diagnóstico textual da estrutura das colunas
├── notebooks/             # Pipelines sequenciais do projeto (Jupyter Notebooks)
│   ├── 01_ETL_Integrado.ipynb           # Extração, engenharia de dados e fusão defensiva
│   ├── 02_diagnostico_financeiro_kpis.ipynb   # Análise exploratória, correlações e Tripé da Qualidade
│   └── 03_simulacao_cenarios_plano_acao.ipynb # Modelagem de ROI, metas (OKRs) e plano prescritivo
├── PBIX/                  # Arquivos de inteligência visual e relatórios executivos
│   └── tcc_campo_belo_mg.pbix           # Dashboard interativo de monitoramento do IGD-M
├── scripts/               # Scripts Python auxiliares para automação e validação
│   ├── auditoria_colunas.py             # Scanner automatizado de consistência de esquemas
│   ├── gerar_dicionario.py              # Extrator dinâmico de metadados e dicionário
│   └── verificar_bruto.py               # Validação de integridade dos arquivos brutos federais
├── venv/                  # Ambiente virtual Python isolado (Ignorado no Git)
├── .gitattributes         # Normalização de quebras de linha (LF) e proteção de binários
├── .gitignore             # Regras de exclusão defensiva de dados brutos e caches
├── DICIONARIO_DADOS.md    # Documentação técnica detalhada das variáveis do modelo
├── LICENSE                # Licença de uso e distribuição do projeto (MIT)
├── README.md              # Documentação institucional e guia do repositório
└── requirements.txt       # Manifesto de dependências e bibliotecas do ecossistema
```

---

## 🚀 Etapas do Pipeline Analítico

O ecossistema analítico foi estruturado de forma modular, integrando rotinas em scripts Python para governança de dados e Jupyter Notebooks sequenciais para modelagem quantitativa:

### 🛠️ Governança e Engenharia de Dados Auxiliar (`scripts/`)

Antes do pipeline principal, uma esteira de scripts garante a conformidade e a documentação do projeto:

* **`verificar_bruto.py` (Validação de Entrada):** Executa uma checagem prévia na pasta de matrizes originais do Governo Federal, garantindo a integridade dos arquivos antes do processamento.
* **`auditoria_colunas.py` (Consistência de Esquema):** Mapeia a estrutura das tabelas do MDS ao longo dos anos, identificando variações históricas de nomenclatura e gerando o diagnóstico em `dados_tratados/relatorio_colunas.txt`.
* **`gerar_dicionario.py` (Metadados Automatizados):** Inspeciona os esquemas dos dados consolidados e gera duas saídas: a matriz estruturada `dados_tratados/dicionario_dados.csv` (para consumo programático) e a documentação técnica `DICIONARIO_DADOS.md` (na raiz do repositório).

---

### 1️⃣ ETL e Integração (`notebooks/01_ETL_Integrado.ipynb`)

* **Desafio:** Resolver a fragmentação de bases anuais dispersas e a volatilidade dos esquemas federais ao longo de 88 competências mensais.
* **Solução:** Construção de um pipeline defensivo de extração, higienização, tipagem temporal padronizada (`DATA_ISO`) e persistência dupla em formato serializado Pickle (`.pkl`) e planilha tabular (`.xlsx`) na pasta `dados_tratados/`.

### 2️⃣ Diagnóstico de KPIs e Gargalos (`notebooks/02_diagnostico_financeiro_kpis.ipynb`)

* **Análise:** Auditoria histórica dos repasses e cálculo dos indicadores de desempenho do Tripé da Qualidade (Saúde, Educação e Gestão do Cadastro Único).
* **Estatística Direcionada:** Aplicação de correlação linear (Coeficiente $r$ de Pearson) para isolar os componentes operacionais com maior sensibilidade e impacto sobre o fluxo financeiro recebido.
* **Diagnóstico:** Identificação de comportamento reativo no acompanhamento da Saúde (oscilação por campanhas sazonais) e risco de represamento na Taxa de Atualização Cadastral.

### 3️⃣ Simulação Prescritiva e Modelagem de ROI (`notebooks/03_simulacao_cenarios_plano_acao.ipynb`)

* **Mensuração do Montante Não Captado e Custo de Oportunidade:** Quantificação exata da frustração de receita orçamentária decorrente do *gap* de eficiência na nota do IGD-M, isolando distorções de repasses retroativos federais.
* **Simulação de Sensibilidade:** Modelagem determinística de resgate de receita potencial sob três cenários operacionais (Conservador a 30%, Moderado a 60% e Otimista a 90%).
* **Análise de Viabilidade Econômica (ROI):** Demonstração do retorno fiscal sobre o investimento marginal (horas extras e logística de busca ativa), validando a blindagem orçamentária do Fundo Municipal de Assistência Social em períodos de restrição fiscal.

---

## 💡 Principais Resultados & Impacto Prático

O projeto aplica a **Ciência de Dados** para converter registros administrativos brutos em decisões estratégicas de gestão pública, estruturando-se em duas frentes complementares:

* **Diagnóstico Fiscal Situacional:** Mapeamento do custo de oportunidade e isolamento das causas raízes de glosas orçamentárias na série histórica (2019–2026).
* **Modelagem Prescritiva de Retorno:** Projeção quantitativa de recuperação de receita via simulação de cenários de sensibilidade e comprovação do ROI positivo.

A abordagem substitui o modelo reativo tradicional por uma estratégia de **inteligência operacional preventiva**. O ecossistema equilibra a **eficiência fiscal do município** e a **garantia de direitos socioassistenciais**, transformando dados tratados em um instrumento contínuo de tomada de decisão capaz de otimizar a rotina de atendimento e blindar o caixa municipal.

---

### 🔍 O Diagnóstico de Eficiência Atual

> 📉 **Nota Média Recente (IGD-M):** **87%** ($0{,}87$) de eficiência operacional.  
> 💸 **Custo de Oportunidade Anual:** **R\$ 23.435,10** em repasses federais não captados por defasagem nos índices operacionais.

* **Efeito de Escala vs. Alavancas Operacionais ($r = +0{,}66$):** A análise estatística bivariada em nível capturou a expansão estrutural conjunta das séries impulsionada pelo ciclo nacional de ampliação do Cadastro Único (2022–2023). Contudo, o teste de robustez em **primeira diferença ($\Delta$ mensal)** dissipa a correlação no curto prazo ($r = 0{,}019; p = 0{,}86$), evidenciando que o volume de famílias define a cota máxima autorizada, enquanto as verdadeiras alavancas operacionais de liquidação mensal residem no cumprimento tempestivo das metas do Tripé da Qualidade (Saúde e Gestão).
* **O Impacto da Latência de Dados:** Na rotina de atendimento, os registros de acompanhamento nutricional (pesagem) e vacinação ocorrem na atenção primária, mas enfrentam atrasos de digitação e sincronização nos sistemas de registro (**SISAB / e-SUS APS** e sistema de condicionalidades). O atraso na transmissão é computado pelo Governo Federal como descumprimento de meta, deflagrando glosas automáticas no valor liquidado mensalmente.

---

### 🚀 Viabilidade e Retorno do Plano de Ação

Para captar a receita orçamentária represada e blindar o custeio do Fundo Municipal de Assistência Social, o modelo de simulação projetou o impacto financeiro do resgate de eficiência:

| Cenário Analisado | Resgate do Montante Não Captado | Incremento Anual Estimado | Impacto Acumulado no Mandato (4 Anos) | Nível de Esforço / Finalidade |
| :--- | :---: | :---: | :---: | :--- |
| **1. Conservador (Ajuste de Fluxo)** | **30%** do *gap* | **+ R\$ 7.030,53** | **+ R\$ 28.122,12** | Baixo (agilização de digitação e sincronização) |
| **2. Moderado (Busca Ativa Focal)** | **60%** do *gap* | **+ R\$ 14.061,06** | **+ R\$ 56.244,24** | Médio (triagem de cadastros defasados e contato direto) |
| **3. Otimista (Força-Tarefa Intersetorial)** | **90%** do *gap* | **+ R\$ 21.091,59** | **+ R\$ 84.366,36** | Alto (busca ativa direcionada e intersetorialidade) |
| *🎯 Teto Teórico de Referência (Custo Total)* | *100% do gap* | *R\$ 23.435,10* | *R\$ 93.740,40* | *Baliza teórica máxima (não operacional)* |

> 📌 **Nota Explicativa sobre o Teto de 100%:**  
> A linha correspondente a **100% do *gap*** não constitui um plano de ação executável, pois a perfeição matemática contínua (nota $1{,}00$ ininterrupta) é inviável na dinâmica socioassistencial real. Ela quantifica o **custo de oportunidade total** do município (R\$ 23.435,10/ano; R\$ 93.740,40 no quadriênio) e funciona como a régua máxima de referência para balizar o ganho proporcional dos três cenários operacionais viáveis (Cenários 1, 2 e 3).

---

#### 🛡️ A Lógica da Eficiência Preventiva & Análise de ROI

O planejamento estratégico demonstra como a Ciência de Dados blinda o orçamento municipal ao reorganizar as rotinas da equipe existente, eliminando a necessidade de novos aportes financeiros, contratações adicionais ou gastos com horas extras:

* **Mitigação de Risco Fiscal & Blindagem:** Com **87% ($0{,}87$) de eficiência média recente**, Campo Belo/MG mantém estabilidade e situa-se a apenas 3 pontos percentuais da faixa de excelência ($90\%$). A governança de dados atua como um seguro fiscal, evitando quedas pontuais que gerem glosas financeiras.

* **Triagem Inteligente sob Contenção de Despesas (Foco no BPC):** Em períodos de contingenciamento de custeio (restrição de frotas e insumos), a análise de dados substitui a busca ativa indiscriminada por uma **priorização preditiva**. O pipeline segmenta preventivamente beneficiários do **Benefício de Prestação Continuada (BPC)** que se aproximam da janela limite de 24 meses sem atualização. Por envolver cruzamentos diretos com o INSS e risco de suspensão imediata de renda para idosos e pessoas com deficiência, o agendamento antecipado no CRAS resolve a pendência no atendimento de rotina, protegendo a família e o índice municipal com custo operacional marginal nulo.

* **Conformidade com o Piso Regulatório ($0{,}80$):** A legislação federal do MDS fixa o índice de **0,80 (80%)** como patamar mínimo regulatório; valores inferiores disparam penalidades graduais e retenção integral de repasses. A gestão orientada por evidências assegura margem contínua de segurança acima do piso legal, garantindo previsibilidade orçamentária ao Fundo Municipal.

---

## ⚙️ Como Executar o Projeto

Para reproduzir as análises localmente:

### 1. Clonar e Instalar

```bash
# Clone o repositório
git clone [https://github.com/JulianoMata/tcc-igdm-campo-belo-mg.git](https://github.com/JulianoMata/tcc-igdm-campo-belo-mg.git)

# Entre na pasta raiz do projeto
cd tcc-igdm-campo-belo-mg

# Crie o ambiente virtual (Recomendado)
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as dependências estruturais
pip install -r requirements.txt
```

### 2. Executar as Análises (via VS Code)

O projeto foi inteiramente estruturado e testado utilizando o **Visual Studio Code**.

```bash
# Abra a pasta do projeto no VS Code
code .
```

💡 Nota de Execução: Certifique-se de possuir a extensão oficial Jupyter instalada no seu VS Code. Para garantir a consistência das simulações e o correto carregamento dos arquivos serializados em disco (.pkl), navegue até a pasta notebooks/ e execute as células respeitando a ordem sequencial:

1. 01_ETL_Integrado.ipynb

2. 02_diagnostico_financeiro_kpis.ipynb

3. 03_simulacao_cenarios_plano_acao.ipynb

---

### 📝 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### 🤝 Contribuições

Contribuições voltadas à otimização de algoritmos de inteligência governamental, engenharia de dados públicos e expansão do modelo analítico para outros municípios são muito bem-vindas! Sinta-se à vontade para abrir uma *issue* ou submeter um *pull request*.

---

### 📞 Contato

Para dúvidas, insights ou discussões técnicas sobre Ciência de Dados aplicada à governança e finanças públicas:

**Juliano França da Mata**  
📧 [jfmatta@gmail.com](mailto:jfmatta@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/julianomata)  
🐙 [GitHub](https://github.com/JulianoMata)
