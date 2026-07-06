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

O projeto foi estruturado de forma coesa, unindo scripts Python utilitários para governança de dados e notebooks sequenciais para análise avançada:

### 🛠️ Governança e Engenharia de Dados Auxiliar (`scripts/`)
Antes do início do tratamento, uma esteira de scripts garante a confiabilidade e a documentação do ecossistema de dados:
* **`verificar_bruto.py` (Validação de Entrada):** Realiza uma checagem prévia e automatizada na pasta de matrizes originais do Governo Federal, garantindo que os arquivos essenciais estejam presentes antes da execução do pipeline.
* **`auditoria_colunas.py` (Consistência de Esquema):** Mapeia e valida a integridade estrutural das tabelas do MDS ao longo dos anos, identificando variações históricas de nomenclatura e exportando o diagnóstico detalhado no arquivo utilitário **`relatorio_colunas.txt`**.
* **`gerar_dicionario.py` (Metadados Automatizados):** Lê os schemas dos dados processados e gera de forma automatizada duas saídas distintas: o arquivo estruturado **`dicionario_dados.csv`** (salvo na pasta `dados_tratados/` para consumo de sistemas) e o arquivo de documentação **`DICIONARIO_DADOS.md`** (salvo na raiz do projeto para leitura direta no repositório).

---

### 1️⃣ ETL e Integração (`notebooks/01_ETL_Integrado.ipynb`)
* **Desafio:** Resolver a descontinuidade temporal e a fragmentação de múltiplas bases anuais dispersas.
* **Solução:** Desenvolvimento de um pipeline automatizado de extração, limpeza, tipagem temporal padronizada (`DATA_ISO`) e persistência segura em formato binário Pickle (`.pkl`) e Excel (`.xlsx`) na pasta `dados_tratados/`.

### 2️⃣ Diagnóstico de KPIs e Gargalos (`notebooks/02_diagnostico_financeiro_kpis.ipynb`)
* **Análise:** Auditoria histórica dos repasses e cálculo dos indicadores de desempenho (KPIs) do Tripé da Qualidade (Saúde, Educação e Gestão).
* **Estatística:** Implementação de um **Ranking de Impacto Estatístico (Pearson)** para isolar quais componentes possuem maior correlação linear ($r$) com a oscilação do repasse financeiro real.
* **Resultado:** Mapeamento de um gap crítico e reativo no acompanhamento de Saúde (frequência de pesagem) dentro do município.

### 3️⃣ Simulação de Cenários e Plano de Ação Prescritivo (`notebooks/03_simulacao_cenarios_plano_acao.ipynb`)
* **Calculadora de ROI:** Modelagem financeira parametrizada que isola a perda estrutural gerada pela ineficiência da Nota IGD-M, limpando com precisão falsos positivos gerados por repasses retroativos federais.
* **Simulação de Sensibilidade:** Projeção matemática de cenários de resgate de caixa (Conservador, Moderado e Otimista) baseados em níveis realistas de esforço de gestão.
* **Análise de Viabilidade:** Avaliação robusta da otimização operacional frente à receita preservada, validando a lógica de "blindagem orçamentária" e priorização cirúrgica de públicos críticos (como o BPC) sob as rígidas travas de contenção de despesas da pasta.

---

## 💡 Principais Resultados & Impacto Prático

O projeto utiliza a Ciência de Dados para transformar registros administrativos em decisões estratégicas de gestão pública, dividindo-se em duas vertentes: o diagnóstico do cenário fiscal atual e a projeção de retorno do plano de ação proposto.

A abordagem substitui o modelo tradicional de busca ativa massiva por uma estratégia de **inteligência operacional preditiva**. Com isso, o modelo atua diretamente no equilíbrio entre a eficiência fiscal do município e a proteção social ativa, convertendo os dados tratados em uma ferramenta de planejamento capaz de otimizar a rotina de atendimento sem gerar novas despesas operacionais.

---

### 🔍 O Diagnóstico de Eficiência Atual

> 📉 **Nota Média Recente (IGD-M):** **87%** (0.87) de eficiência.
> 💸 **Custo de Oportunidade Anual:** **R\$ 23.435,10** em recursos federais não acessados.

* **O Gargalo Estrutural ($r = +0.66$):** A análise estatística provou que o número de famílias no Cadastro Único cresceu aceleradamente, mas a estrutura para registrar os acompanhamentos não acompanhou o mesmo ritmo. Isso gerou um represamento de beneficiários fora do radar das condicionalidades de saúde.

* **O Impacto no Sistema do Conservador:** Na prática, muitas pesagens e vacinações são realizadas na ponta, mas a informação demora a ser digitada ou sincronizada no sistema do **Conservador (SISAB/e-SUS)**. Como o Governo Federal não enxerga esses dados em tempo hábil, ele interpreta a defasagem como descumprimento de meta, aplicando descontos automáticos no repasse mensal do IGD-M e gerando a perda financeira anual de **R\$ 23.435,10**.


---

### 🚀 Viabilidade e Retorno do Plano de Ação

Para mitigar a perda financeira e garantir a segurança jurídica do município, o algoritmo de simulação avaliou o impacto de mutirões focados na atualização de cadastros vencidos através de três cenários de eficiência na busca ativa:

| Cenário Analisado | Meta de Recuperação | Impacto Financeiro (Retorno ao Fundo) | Viabilidade Operacional |
| :--- | :---: | :---: | :--- |
| **Cenário Conservador** | **30%** | **+ R\$ 7.030,53 / ano** | Baixo Risco (Recuperação mínima com esforço habitual) |
| **Cenário Moderado** | **60%** | **+ R\$ 14.061,06 / ano** | Alta Viabilidade (Foco em cadastros críticos > 24 meses) |
| **Cenário Otimista** | **100%** | **+ R\$ 23.435,10 / ano** | Desafiador (Demanda varredura completa e atualização plena) |
---

#### 🛡️ A Lógica da Eficiência Preventiva & Análise de ROI (Retorno sobre Investimento)

O planejamento estratégico avalia como a aplicação de Ciência de Dados pode blindar o orçamento do município, otimizando as rotinas internas da equipe sem a necessidade de novos aportes financeiros, contratações ou horas extras. A viabilidade financeira e o potencial de captação de recursos variam conforme a eficiência dos cenários simulados:

* **Métrica de ROI (Retorno sobre Investimento):**
  * 📉 **Cenário Conservador:** Recuperação de **R\$ 7.030,53 / ano** (atingido apenas com o realinhamento da busca ativa rotineira e cruzamento de dados interno).
  * ⚖️ **Cenário Moderado:** Recuperação de **R\$ 14.061,06 / ano** (ponto de otimização focado na triagem inteligente de cadastros críticos com mais de 24 meses de defasagem).
  * 🚀 **Cenário Otimista:** Recuperação de **R\$ 23.435,10 / ano** (teto máximo de eficiência e captação de recursos federais represados).

* **Mitigação de Risco Fiscal & Estabilidade:** O município opera hoje em um patamar seguro de **87% de eficiência**, consolidando uma boa margem de estabilidade e estando a apenas 3 pontos percentuais de atingir a meta de excelência de 90%. O uso das ferramentas de dados atua como um mecanismo preventivo de proteção de receita, garantindo que o município mantenha sua performance estável e permaneça distante da zona crítica.

* **Triagem Inteligente na Contenção de Despesas (Foco em BPC):** Em cenários reais de limitação de recursos de custeio (como restrição de combustível e suspensão de horas extras), a inteligência de dados substitui a busca ativa genérica por um **direcionamento cirúrgico**. O algoritmo prioriza automaticamente o cruzamento de dados de beneficiários do **BPC (Benefício de Prestação Continuada)** cujos cadastros estejam entrando na janela de revisão de 24 meses. Diferente de outros programas, o BPC possui regras rígidas de cruzamento de dados com o INSS e histórico de suspensão imediata do benefício pago a idosos e pessoas com deficiência. A identificação antecipada dessas famílias permite que o CRAS realize o atendimento preventivo de forma interna e rotineira, evitando o bloqueio do benefício do cidadão sem gerar custos de deslocamento para a prefeitura.

* **Fundamentação Legal do Piso Regulatório (80%):** Conforme as diretrizes normativas do Ministério do Desenvolvimento Social (MDS) que regulamentam o IGD-M, o índice de **0,80** é o limite mínimo de tolerância para a gestão descentralizada, abaixo do qual aplicam-se sanções em cascata (advertências e bloqueio total de repasses). A otimização preditiva das filas de atendimento protege o orçamento da pasta, mantendo a nota municipal e garantindo a continuidade dos repasses federais com custo zero de execução de campo.
---

## ⚙️ Como Executar o Projeto

Para reproduzir as análises localmente:

### 1. Clonar e Instalar

```bash
# Clone o repositório
git clone https://github.com/JulianoMata/tcc-igdm-campo-belo-mg.git

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
💡 Nota de Execução: Certifique-se de possuir a extensão oficial Jupyter instalada no seu VS Code. Para garantir a consistência das simulações e o correto carregamento dos arquivos serializados em disco (.pkl), navegue até a pasta notebooks/ e execute as células respeitando rigorosamente a ordem sequencial cronológica (01_ETL_Integrado.ipynb a 03_simulacao_cenarios_plano_acao.ipynb).

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
