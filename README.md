# 📊 Otimização de Receita Pública com Data Science - Campo Belo/MG

> **Projeto de TCC (Ciência de Dados e Inteligência Artificial)** 
> Como a gestão pública orientada a dados e a eficiência operacional podem blindar e expandir os repasses financeiros federais (IGD-M) do município.

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Pandas](https://img.shields.io/badge/Lib-Pandas-150458) ![Power BI](https://img.shields.io/badge/Dashboards-Power_BI-yellow) ![License](https://img.shields.io/badge/License-MIT-green)

---
## 📖 Sobre o Projeto
Este repositório contém o desenvolvimento de um projeto aplicado de Ciência de Dados e Inteligência Artificial voltado à Gestão Pública Municipal.

O Cadastro Único (CadÚnico) e o acompanhamento das condicionalidades do Bolsa Família são os pilares de sustentação dos recursos socioassistenciais no Brasil. Contudo, descontinuidades de fluxos e defasagens cadastrais geram perdas financeiras silenciosas para as prefeituras. Através da extração, tratamento, análise estatística direcionada e simulação de cenários com dados abertos do Governo Federal, este projeto comprova empiricamente que a eficiência técnica da equipe de ponta é um vetor direto de captação e blindagem de recursos. O resultado final é um ecossistema analítico capaz de guiar a tomada de decisão dos gestores de Campo Belo/MG, maximizando os repasses do Índice de Gestão Descentralizada (IGD-M).

---

## 📈 Dashboard Interativo

A visualização completa dos indicadores financeiros e das taxas de qualidade do tripé de condicionalidades está disponível em um painel executivo online.

🔗 **[Acessar o Dashboard no Power BI Online](https://app.powerbi.com/view?r=eyJrIjoiMDVlMTI1NWYtODYzMy00MmE1LTkxNjAtNmEzZWM3Mzg2MWNiIiwidCI6IjE4MzJhNTBkLWZmYWYtNDhiYi1iM2NjLWU4MDk3ZWM4NGVlZiJ9)**

---

## 🎯 O Problema de Negócio

Muitos gestores municipais desconhecem que o repasse de verbas federais de apoio à gestão (IGD-M) não é uma cota fixa. Ele varia de 0% a 100% de acordo com indicadores de desempenho locais.

**O Objetivo:** Analisar o histórico do município de **2019 a 2026** para expor falhas operacionais, mensurar o custo de oportunidade das perdas de receita e provar matematicamente que o investimento na busca ativa e na otimização de fluxos atua como uma apólice de seguro fiscal, blindando o caixa do Fundo Municipal.

---

## 📂 Fonte dos Dados (Data Source)

Os dados utilizados são de acesso público e foram extraídos do **Portal de Dados Abertos do Governo Federal**. 

O desafio inicial de **Engenharia de Dados** centrou-se na fragmentação: os registros não estavam centralizados. Foi necessário desenvolver um pipeline robusto para coletar, cruzar e unificar três matrizes de dados distintas para cada período anual (Taxas de qualidade, Valores Calculados e Públicos Totais) para compor a base consolidada.

* **Fonte Oficial:** [Índice de Gestão Descentralizada (IGD-M) - dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/indice-de-gestao-descentralizada-dos-municipios---igd-m)
* **Janela Temporal Coletada:** 2019 a 2026.
* **Escopo Regional:** Dados filtrados estritamente para o município de **Campo Belo/MG** (Código IBGE: 311120).

---

## 🗂 Estrutura do Projeto

```text
TCC_CAMPOBELO/
├── dados_brutos/          # Matrizes originais do Governo Federal (Ignoradas no Git)
│   ├── CALCULOS/          # Histórico de valores liquidados e repassados
│   ├── PUBLICO/           # Quantitativos de famílias e metas de público-alvo
│   └── TAXAS/             # Índices e taxas de cobertura das condicionalidades
├── dados_tratados/        # Datasets consolidados e dicionário auxiliar
│   ├── dataset_financeiro_tratado.pkl  # Dataset serializado para consumo rápido no Python
│   ├── dataset_financeiro_tratado.xlsx # Dataset em formato Excel para auditoria ou BI
│   └── dicionario_dados.csv            # Matriz de metadados das variáveis tratadas
├── notebooks/             # Pipelines sequenciais do projeto (Jupyter Notebooks)
│   ├── 01_ETL_Integrado.ipynb          # Extração, limpeza e consolidação das bases de dados
│   ├── 02_diagnostico_financeiro_kpis.ipynb # Análise exploratória e cálculo de indicadores do IGD-M
│   └── 03_simulacao_cenarios_plano_acao.ipynb # Modelagem preditiva, simulações e prescrição de metas
├── PBIX/                  # Arquivos de modelagem visual e Dashboards (Power BI)
├── scripts/               # Scripts Python auxiliares e rotinas de validação
│   ├── auditoria_colunas.py   # Mapeamento e consistência das colunas nos datasets
│   ├── gerar_dicionario.py    # Geração automatizada do arquivo de metadados em CSV
│   ├── relatorio_colunas.txt  # Output textual da estrutura e integridade das colunas
│   └── verificar_bruto.py     # Script de validação inicial dos arquivos brutos federais
├── venv/                  # Ambiente virtual Python isolado (Ignorado no Git)
├── .gitignore             # Exclusão defensiva de dados brutos, caches e ambientes
├── DICIONARIO_DADOS.md    # Metadados e documentação técnica dos schemas das tabelas
├── LICENSE                # Licença de uso do projeto (MIT)
├── README.md              # Documentação principal do repositório
└── requirements.txt       # Dependências estruturais do projeto
```

---

## 🚀 Etapas do Pipeline Analítico

O projeto foi estruturado de forma coesa e modular em 3 notebooks sequenciais e scripts auxiliares:

### 🛠️ Engenharia de Dados Auxiliar (`scripts/auditoria_de_colunas.py`)
* **Função:** Script fundamental para validar a integridade estrutural das matrizes brutas do MDS, mapeando variações de nomenclatura e garantindo a consistência do esquema antes da consolidação.

### 1️⃣ ETL e Integração (`notebooks/01_ETL_Integrado.ipynb`)
* **Desafio:** Resolver a descontinuidade temporal e a fragmentação de múltiplas bases anuais dispersas.
* **Solução:** Desenvolvimento de um pipeline automatizado de extração, limpeza, tipagem temporal padronizada (`DATA_ISO`) e persistência segura em formato binário Pickle (.pkl) na pasta `dados_tratados/`.

### 2️⃣ Diagnóstico de KPIs e Gargalos (`notebooks/02_diagnostico_financeiro_kpis.ipynb`)
* **Análise:** Auditoria histórica dos repasses e cálculo dos indicadores de desempenho (KPIs) do Tripé da Qualidade (Saúde, Educação e Gestão).
* **Estatística:** Implementação de um **Ranking de Impacto Estatístico (Pearson)** para isolar quais componentes possuem maior correlação linear ($r$) com a oscilação do repasse financeiro real.
* **Resultado:** Mapeamento de um gap crítico e reativo no acompanhamento de Saúde (frequência de pesagem) dentro do município.

### 3️⃣ Simulação de Cenários e Plano de Ação Prescritivo (`notebooks/03_simulacao_cenarios_plano_acao.ipynb`)
* **Calculadora de ROI:** Modelagem financeira parametrizada que isola a perda estrutural gerada pela ineficiência da Nota IGD-M, limpando com precisão falsos positivos gerados por repasses retroativos federais.
* **Simulação de Sensibilidade:** Projeção matemática de cenários de resgate de caixa (Conservador, Moderado e Otimista) baseados em níveis realistas de esforço de gestão.
* **Análise de Viabilidade:** Avaliação robusta do custo operacional frente à receita preservada, validando a lógica de "blindagem orçamentária" sob as rígidas travas da LRF em ano eleitoral.

---

## 💡 Principais Resultados & Impacto Prático

O projeto utiliza a Ciência de Dados para transformar registros administrativos em decisões estratégicas de gestão pública, dividindo-se em duas vertentes: o diagnóstico do cenário fiscal atual e a projeção de retorno do plano de ação proposto.

---

### 🔍 O Diagnóstico de Eficiência Atual

> 📉 **Nota Média Recente (IGD-M):** **87%** (0.87) de eficiência.
> 💸 **Custo de Oportunidade Anual:** **R$ 23.435,10** em recursos federais não acessados.

* **O Gargalo Estrutural:** A análise de correlação de Pearson revelou um coeficiente de **$r = +0.66$**. Isso demonstra cientificamente que, enquanto a base de dados de famílias (escala) expandiu fortemente, a capacidade operacional de acompanhamento entrou em um *platô técnico*. O principal reflexo desse gap físico foi o represamento de indivíduos fora do radar de acompanhamento das condicionalidades de saúde (SUS).

---

### 🚀 Viabilidade e Retorno do Plano de Ação

Para mitigar a perda financeira e garantir a segurança jurídica do município, o algoritmo de simulação avaliou o impacto de mutirões focados na atualização de cadastros vencidos há mais de 24 meses:

| Cenário Analisado | Meta de Recuperação | Impacto Financeiro (Retorno ao Fundo) | Viabilidade Operacional |
| :--- | :---: | :---: | :--- |
| **Cenário Moderado** | **60%** | **+ R$ 14.061,06 / ano** | Alta (Foco em cadastros críticos > 24 meses) |
| **Cenário Otimista** | **100%** | **+ R$ 23.435,10 / ano** | Médio-Alto (Demanda varredura completa) |

#### 🛡️ A Lógica do Seguro (Análise de ROI)
O custo anual estimado para execução das rodadas de mutirão e ampliação sazonal da jornada de entrevistas é de **R$ 12.000,00**. 

* **Autossustentável:** No cenário moderado, o plano já se paga sozinho, gerando um superávit real para o Fundo Municipal de Assistência Social.
* **Mitigação de Risco Fiscal:** O investimento representa **menos de 2.5%** do orçamento anual total protegido pelo IGD-M. Ele funciona como um seguro ativo, afastando em **100%** o risco de sanções, advertências ou bloqueios totais dos repasses por descumprimento do piso legal de 80% de eficiência exigido pelo Governo Federal.
---

## ⚙️ Como Executar o Projeto

Para reproduzir as análises localmente:

### 1. Clonar e Instalar

```bash
# Clone o repositório
git clone [https://github.com/JulianoMata/tcc-igdm-campo-belo-mg.git](https://github.com/JulianoMata/tcc-igdm-campo-belo-mg.git)

# Entre na pasta raiz do projeto
cd tcc-igdm-campo-belo-mg

# Crie e ative o ambiente virtual (Recomendado)
# Windows:
python -m venv venv
venv\Scripts\activate

# Linux/Mac:
python3 -m venv venv
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
*💡 Nota de Execução: Certifique-se de possuir a extensão oficial Jupyter instalada no seu VS Code. Para garantir a consistência das simulações e o correto carregamento dos arquivos serializados em disco (.pkl), navegue até a pasta notebooks/ e execute as células respeitando rigorosamente a ordem sequencial cronológica (01_ETL_Integrado.ipynb a 03_simulacao_cenarios_plano_acao.ipynb).

---

### 📝 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 🤝 Contribuições
Contribuições focadas em otimização de algoritmos de inteligência governamental e melhorias em pipelines de dados públicos são muito bem-vindas! Sinta-se à vontade para abrir issues ou submeter pull requests.

### 📞 Contato
Para dúvidas, insights ou discussões acadêmicas sobre ciência de dados aplicada à governança e finanças públicas:

**Juliano França da Mata** 

📧 jfmatta@gmail.com  
💼 [LinkedIn](https://www.linkedin.com/in/julianomata)
🐈 [GitHub](https://github.com/JulianoMata)    
