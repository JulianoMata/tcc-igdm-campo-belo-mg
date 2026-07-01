import pandas as pd
import glob
import os

caminho_calculos = os.path.abspath(os.path.join(os.getcwd(), "dados_brutos", "CALCULOS"))
arquivos_alvo = ['calculos_2024.csv', 'calculos_2025.csv', 'calculos_2026.csv']

print("🕵️‍♂️ INVESTIGAÇÃO DE TIPOS E VALORES BRUTOS (2024-2026)")
print("=" * 70)

for nome_arq in arquivos_alvo:
    caminho_arq = os.path.join(caminho_calculos, nome_arq)
    if os.path.exists(caminho_arq):
        # Detecta delimitador real do arquivo
        with open(caminho_arq, 'r', encoding='latin1') as f:
            primeira_linha = f.readline()
        sep = ',' if ',' in primeira_linha else ';'
        
        # Lê o arquivo puro
        df = pd.read_csv(caminho_arq, sep=sep, encoding='latin1', dtype=str)
        df.columns = df.columns.str.strip().str.lower()
        
        # Identifica coluna de IBGE
        col_ibge = [c for c in df.columns if 'ibge' in c or 'codigo' in c][0]
        df_cb = df[df[col_ibge].isin(['311120', '3111200'])].copy()
        
        print(f"\n📄 ARQUIVO: {nome_arq} (Delimitador: '{sep}')")
        print(f"Colunas identificadas no disco: {list(df.columns)}")
        print(f"Total de linhas para Campo Belo: {len(df_cb)}")
        
        if not df_cb.empty:
            # Mostra uma amostra das primeiras linhas encontradas para checarmos os valores visuais e tipos
            print("-" * 70)
            # Pegamos as 3 primeiras linhas para analisar os valores lado a lado
            print(df_cb.head(3).to_string())
            print("-" * 70)
    else:
        print(f"❌ Arquivo não localizado: {nome_arq}")