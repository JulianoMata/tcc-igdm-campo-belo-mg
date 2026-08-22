from pathlib import Path
import pandas as pd

# Garante resolução robusta a partir da localização do arquivo atual
DIRETORIO_RAIZ = Path(__file__).resolve().parent.parent if "__file__" in locals() else Path.cwd()
caminho_calculos = DIRETORIO_RAIZ / "dados_brutos" / "CALCULOS"
arquivos_alvo = ['calculos_2024.csv', 'calculos_2025.csv', 'calculos_2026.csv']

print("🕵️‍♂️ INVESTIGAÇÃO DE TIPOS E VALORES BRUTOS (2024-2026)")
print("=" * 70)

for nome_arq in arquivos_alvo:
    caminho_arq = caminho_calculos / nome_arq
    if caminho_arq.exists():
        # Detecta delimitador real da primeira linha
        with open(caminho_arq, 'r', encoding='latin1') as f:
            primeira_linha = f.readline()
        sep = ',' if ',' in primeira_linha else ';'
        
        # Leitura bruta dos dados como texto para auditoria
        df = pd.read_csv(caminho_arq, sep=sep, encoding='latin1', dtype=str)
        df.columns = df.columns.str.strip().str.lower()
        
        # Identifica dinamicamente a coluna de IBGE
        cols_ibge = [c for c in df.columns if 'ibge' in c or 'codigo' in c]
        if not cols_ibge:
            print(f"\n⚠️ Coluna de IBGE não encontrada no arquivo: {nome_arq}")
            continue
            
        col_ibge = cols_ibge[0]
        df_cb = df[df[col_ibge].isin(['311120', '3111200'])].copy()
        
        print(f"\n📄 ARQUIVO: {nome_arq} (Delimitador: '{sep}')")
        print(f"Colunas identificadas no disco: {list(df.columns)}")
        print(f"Total de linhas para Campo Belo: {len(df_cb)}")
        
        if not df_cb.empty:
            print("-" * 70)
            print(df_cb.head(3).to_string())
            print("-" * 70)
    else:
        print(f"❌ Arquivo não localizado: {nome_arq}")
        