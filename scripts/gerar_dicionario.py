import pandas as pd
import os
import glob

# Reaproveita o mapa oficial para manter o dicionário sempre sincronizado
from auditoria_colunas import MAPA_COLUNAS_ATUAL

# Descrições técnicas e amigáveis para o Power BI e para a Banca do TCC
DESCRICOES = {
    'CODIGO_IBGE': 'Código identificador do município no IBGE (Padrão 6 dígitos para o cruzamento).',
    'COMPETENCIA': 'Ano e mês de referência dos dados no formato AAAAMM.',
    'TAXA_IGDM': 'Índice de Gestão Descentralizada Municipal do Programa Bolsa Família.',
    'TAXA_ATUALIZACAO': 'Percentual de atualização cadastral do município.',
    'TAXA_FREQ_ESCOLAR': 'Percentual de cumprimento da condicionalidade de frequência escolar.',
    'TAXA_ACOMP_SAUDE': 'Percentual de cumprimento da condicionalidade de saúde (vacinação/peso).',
    'REPASSE_REAL': 'Valor financeiro efetivamente repassado pelo MDS ao fundo municipal (R$).',
    'TETO_POTENCIAL': 'Valor máximo orçamentário que o município poderia receber se atingisse 100% das metas.',
    'TETO_REGULATORIO': 'Teto regulatório normativo de referência do IGD-M.',
    'TETO_BASE_SEM_INCENTIVO': 'Valor orçamentário base calculado para o município, desconsiderando bonificações de desempenho.',
    'VALOR_TOTAL_INCENTIVOS': 'Montante financeiro adicional (bônus) concedido ao município pelo cumprimento de metas de eficiência no IGD-M.',
    'QTD_FAMILIAS': 'Quantidade total de famílias inscritas no Cadastro Único com renda até meio salário mínimo.',
    'SAUDE_PUBLICO_TOTAL': 'Total de pessoas que compõem o público-alvo para acompanhamento da saúde.',
    'SAUDE_ACOMPANHADOS': 'Quantidade de pessoas que tiveram a condicionalidade de saúde informada.',
    'EDUCACAO_ACOMPANHADOS': 'Quantidade de pessoas com frequência escolar acompanhada e informada.',
    'FATOR_REDUTOR_FINANCEIRO': 'Índice de redução de repasse aplicado caso o município possua saldo excessivo em conta.',
    'MOTIVO_IMPEDIMENTO': 'Justificativa administrativa caso o repasse do mês tenha sido bloqueado ou zerado.'
}

def inferir_tipo_mapeado(col_final: str) -> str:
    """Classifica o tipo semântico das colunas consumidas no pipeline."""
    col_upper = col_final.upper()
    if any(k in col_upper for k in ['REAL', 'TETO', 'INCENTIVO', 'NAO_CAPTADO']):
        return 'Decimal / Moeda (R$)'
    elif any(k in col_upper for k in ['TAXA', 'FATOR_REDUTOR']):
        return 'Percentual / Decimal (0 a 1)'
    elif any(k in col_upper for k in ['QTD', 'TOTAL', 'ACOMPANHADOS', 'PUBLICO']):
        return 'Inteiro'
    elif any(k in col_upper for k in ['COMPETENCIA', 'DATA']):
        return 'Temporal'
    return 'Texto'

def extrair_todas_colunas_brutas(caminho_dados_brutos):
    """Varre todas as pastas e arquivos para capturar o universo de colunas existentes."""
    colunas_descobertas = set()
    pastas = ['CALCULOS', 'TAXAS', 'PUBLICO']
    
    for pasta in pastas:
        path_pasta = os.path.join(caminho_dados_brutos, pasta)
        arquivos = glob.glob(os.path.join(path_pasta, "*.[cC][sS][vV]"))
        for arq in arquivos:
            try:
                with open(arq, 'r', encoding='latin1') as f:
                    primeira_linha = f.readline()
                sep = ',' if ',' in primeira_linha else ';'
                df_temp = pd.read_csv(arq, sep=sep, encoding='latin1', dtype=str, nrows=0)
                
                for col in df_temp.columns:
                    colunas_descobertas.add(col.strip().lower())
            except:
                pass
    return sorted(list(colunas_descobertas))

def gerar_dicionario():
    print("📖 GERANDO DICIONÁRIO DE DADOS AUTOMATIZADO INTEGRAL...")
    
    pasta_scripts = os.path.dirname(os.path.abspath(__file__))
    caminho_brutos = os.path.abspath(os.path.join(pasta_scripts, "..", "dados_brutos"))
    
    todas_colunas_brutas = extrair_todas_colunas_brutas(caminho_brutos)
    
    dados_dic = {}
    for col_bruta, col_final in MAPA_COLUNAS_ATUAL.items():
        if col_final not in dados_dic:
            dados_dic[col_final] = []
        dados_dic[col_final].append(col_bruta)
        
    linhas = []
    colunas_processadas_brutas = set()
    
    # 1. Colunas mapeadas (Utilizadas)
    for col_final, origens in dados_dic.items():
        linhas.append({
            'Status': '✅ UTILIZADA',
            'Nome no Modelo': col_final,
            'Colunas Brutas Equivalentes': ", ".join(origens),
            'Tipo Sugerido': inferir_tipo_mapeado(col_final),
            'Descrição': DESCRICOES.get(col_final, 'Descrição não mapeada.')
        })
        for o in origens:
            colunas_processadas_brutas.add(o.lower().strip())
            
    # 2. Colunas não mapeadas (Disponíveis para auditoria futura)
    for col_bruta in todas_colunas_brutas:
        if col_bruta not in colunas_processadas_brutas:
            tipo_futuro = 'Decimal' if col_bruta.endswith('_f') else ('Inteiro' if col_bruta.endswith('_i') else 'Texto')
            
            linhas.append({
                'Status': '⬜ DISPONÍVEL',
                'Nome no Modelo': 'Não mapeada (Pula no ETL)',
                'Colunas Brutas Equivalentes': col_bruta,
                'Tipo Sugerido': tipo_futuro,
                'Descrição': 'Coluna nativa presente nos arquivos brutos do MDS, disponível para futura extração.'
            })
            
    df_dic = pd.DataFrame(linhas)
    df_dic.sort_values(by=['Status'], ascending=False, inplace=True)
    
    caminho_md = os.path.abspath(os.path.join(pasta_scripts, "..", "DICIONARIO_DADOS.md"))
    caminho_csv = os.path.abspath(os.path.join(pasta_scripts, "..", "dados_tratados", "dicionario_dados.csv"))
    
    with open(caminho_md, "w", encoding="utf-8") as f:
        f.write("# Dicionário de Dados Abrangente - TCC Campo Belo\n\n")
        f.write("Este arquivo descreve tanto as colunas consumidas pelo pipeline atual quanto os campos brutos mantidos para fins de auditoria histórica.\n\n")
        f.write(df_dic.to_markdown(index=False))
        
    os.makedirs(os.path.dirname(caminho_csv), exist_ok=True)
    df_dic.to_csv(caminho_csv, index=False, sep=';', encoding='utf-8-sig')
    
    print(f"✅ Dicionário Markdown atualizado: {caminho_md}")
    print(f"✅ Dicionário CSV gerado para o Power BI: {caminho_csv}")

if __name__ == "__main__":
    gerar_dicionario()
    