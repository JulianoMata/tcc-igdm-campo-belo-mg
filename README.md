# 📊 Otimização de Receita Pública com Data Science - Campo Belo/MG

> **Projeto de TCC (Ciência de Dados e Inteligência Artificial)**
> Como a gestão eficiente de cadastros pode aumentar o repasse financeiro do Governo Federal para o município.

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Pandas](https://img.shields.io/badge/Lib-Pandas-150458) ![Power BI](https://img.shields.io/badge/Dashboards-Power_BI-yellow) ![License](https://img.shields.io/badge/License-MIT-green)

---
## 📖 Sobre o Projeto
Este repositório contém o desenvolvimento de um projeto aplicado de Ciência de Dados e Inteligência Artificial voltado para a Gestão Pública.

O Cadastro Único (CadÚnico) é a porta de entrada para os programas sociais no Brasil, mas a desatualização desses dados gera perdas financeiras silenciosas para as prefeituras. Através da coleta, tratamento, análise estatística e simulação de cenários usando dados abertos do Governo Federal, este projeto comprova que a assistência social não é apenas um centro de custos, mas um vetor de captação de recursos. O resultado final é um simulador capaz de guiar a tomada de decisão de gestores municipais, maximizando os repasses do Índice de Gestão Descentralizada (IGD-M).

---

## 📈 Dashboard Interativo

A visualização completa dos indicadores financeiros e das taxas de qualidade (IGD-M) está disponível em um painel interativo.

🔗 **[Acessar o Dashboard no Power BI Online](https://app.powerbi.com/view?r=eyJrIjoiZGE0MTFkYTgtNWZjYi00MWQ5LTkyMzctNTdkNGE0YjAzNWIzIiwidCI6IjkxMGFjMTUzLTc0NWMtNGZkNy1iNDNkLTQyNGE3Yjc5OTQyYiJ9&pageName=f8873520a2400a91b393)**

---

## 🎯 O Problema de Negócio

Muitos gestores públicos desconhecem que o repasse de verbas federais (como o **IGD-M** associado aos programas de transferência de renda) não é fixo. Ele varia conforme a qualidade da administração local.

**O Objetivo:** Este projeto analisa dados públicos de **2019 a 2026** para provar matematicamente que investir na busca ativa e na atualização cadastral gera retorno financeiro direto para o município, pagando o próprio investimento da operação.

---

## 📂 Fonte dos Dados (Data Source)

Os dados utilizados são públicos e foram extraídos do **Portal de Dados Abertos do Governo Federal**. 

O desafio inicial de **Engenharia de Dados** foi a fragmentação: as informações não estavam centralizadas. Foi necessário coletar, cruzar e unificar **três bases distintas para cada período anual** (Taxas, Valores Calculados e Público Utilizado) para compor o dataset final.

* **Fonte Oficial:** [Índice de Gestão Descentralizada (IGD-M) - dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/indice-de-gestao-descentralizada-dos-municipios---igd-m)
* **Períodos Coletados:** 2019 a 2026.
* **Escopo Regional:** Dados filtrados especificamente para o município de **Campo Belo/MG** (Código IBGE: 311120).

---

## 🗂 Estrutura do Projeto

```text
TCC_CAMPOBELO/
├── dados_brutos/      # CSVs originais do Governo Federal (Ignorados no Git)
├── dados_tratados/    # Datasets processados e unificados para análise
├── notebooks/         # Pipeline de Análise e Simulação
├── PBIX/              # Dashboards e Relatórios Visuais (Power BI)
├── scripts/           # Scripts auxiliares (ex: auditoria_de_colunas.py)
├── venv/              # Ambiente virtual Python (Ignorado no Git)
├── .gitignore         # Configuração de arquivos ignorados pelo Git
├── LICENSE            # Licença de uso do projeto (MIT)
├── README.md          # Documentação principal do Projeto
└── requirements.txt   # Bibliotecas e dependências necessárias
```

---

## 🚀 Etapas do Pipeline

O projeto foi estruturado de forma coesa em 3 notebooks sequenciais e scripts de apoio:

### 🛠️ Engenharia de Dados Auxiliar (`scripts/auditoria_de_colunas.py`)
* **Função:** Script fundamental para validar a integridade dos dados brutos, garantindo a consistência das nomenclaturas e a presença de todas as colunas necessárias antes do processamento.

### 1️⃣ ETL e Integração (`notebooks/01_ETL_Integrado.ipynb`)
* **Desafio:** Unificar dados fragmentados de múltiplas bases anuais.
* **Solução:** Processo automatizado de extração, limpeza e integração para a criação do dataset consolidado.

### 2️⃣ Diagnóstico Financeiro (`notebooks/02_diagnostico_financeiro_kpis.ipynb`)
* **Análise:** Cálculo de indicadores de desempenho (KPIs) e auditoria histórica dos repasses.
* **Resultado:** Identificação da saúde financeira e mapeamento de gargalos na captação de recursos.

### 3️⃣ Simulação de Cenários e Plano de Ação (`notebooks/03_simulacao_cenarios_plano_acao.ipynb`)
* **Calculadora de ROI:** Modelagem financeira que isola a perda estrutural gerada pela ineficiência da Taxa IGD-M, removendo distorções de repasses retroativos.
* **Simulação:** Projeção de cenários de recuperação (Conservador, Moderado, Otimista) baseados em metas viáveis de gestão.
* **Análise de Viabilidade:** Avaliação do custo operacional versus a receita preservada, aplicando a lógica de "blindagem orçamentária" para o município.

---

## 💡 Principais Resultados

### O Preço da Eficiência
A análise permitiu quantificar o retorno financeiro da gestão operacional do Cadastro Único.

> **Insight Estratégico:** Cada **1%** de melhoria no índice do **IGD-M** gera um retorno direto ao caixa do município, justificando o investimento na equipe de ponta.

### Projeção de Cenários
Mesmo com as oscilações de repasse em períodos atípicos, a simulação capturou com precisão a tendência de recuperação e o potencial financeiro.

---

## ⚙️ Como Executar o Projeto

Para reproduzir as análises localmente:

### 1. Clonar e Instalar

```bash
# Clone o repositório
git clone [https://github.com/JulianoMata/tcc-igdm-campo-belo-mg.git](https://github.com/JulianoMata/tcc-igdm-campo-belo-mg.git)

# Entre na pasta
cd tcc-igdm-campo-belo-mg

# Ative o ambiente virtual (opcional, mas recomendado)
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 2. Executar Análises (via VS Code)

O projeto foi desenvolvido utilizando o **Visual Studio Code**.

```bash
# Abra a pasta do projeto no VS Code
code .
```
*Certifique-se de ter a extensão **Jupyter** instalada. Navegue até a pasta `notebooks/` e execute os arquivos na ordem sequencial (01 a 03).*

---

### 📝 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### 🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções.

### 📞 Contato
Para dúvidas ou sugestões, entre em contato:

**Juliano França da Mata** 
📧 jfmatta@gmail.com  
💼 [LinkedIn](https://www.linkedin.com/in/julianomata/)