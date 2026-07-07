import pandas as pd
import os
import glob
import sys
import re
import numpy as np

# --- CORREÇÃO DO ERRO DE EMOJI (WINDOWS) ---
sys.stdout.reconfigure(encoding='utf-8') # type: ignore

# --- 1. CONFIGURAÇÃO DO MAPA SINCRO (Padronizado e Unificado) ---
MAPA_COLUNAS_ATUAL = {
    # --- Identificadores ---
    'codigo_ibge': 'CODIGO_IBGE', 
    'anomes_s': 'COMPETENCIA',
    
    # --- Desempenho e Indicadores (Taxas) ---
    'igdm_f': 'TAXA_IGDM', 
    'igd_pab_igdm_f': 'TAXA_IGDM',
    'tx_atual_cad_f': 'TAXA_ATUALIZACAO', 
    'igd_pab_tac_f': 'TAXA_ATUALIZACAO',
    'tx_acomp_freq_escol_f': 'TAXA_FREQ_ESCOLAR', 
    'igd_pab_tafe_f': 'TAXA_FREQ_ESCOLAR',
    'tx_acomp_agenda_saude_f': 'TAXA_ACOMP_SAUDE', 
    'igd_pab_taas_f': 'TAXA_ACOMP_SAUDE',
    
    # --- Pilares Financeiros Principais ---
    'vl_rep_mes_f': 'REPASSE_REAL', 
    'igd_pab_vl_repassado_igdm_f': 'REPASSE_REAL',
    'vl_cal_com_incent_f': 'TETO_POTENCIAL', 
    'igd_pab_vl_calculado_com_incentivos_f': 'TETO_POTENCIAL',
    
    # --- Decomposição do Orçamento (DNA do Cálculo) ---
    'vl_cal_sem_icent_f': 'TETO_BASE_SEM_INCENTIVO',
    'igd_pab_vl_calculado_sem_incentivos_f': 'TETO_BASE_SEM_INCENTIVO',
    'vl_tot_incent_f': 'VALOR_TOTAL_INCENTIVOS',
    'igd_pab_vl_total_incentivos_f': 'VALOR_TOTAL_INCENTIVOS',
    
    # --- Tetos Regulatórios Históricos ---
    'teto_rep_igdm_f': 'TETO_REGULATORIO', 
    'igd_pab_vl_teto_repasse_igdm_f': 'TETO_REGULATORIO',
    
    # --- Penalidades Administrativas e Administrativo ---
    'igd_pbf_fator_redutor_conforme_saldo_f': 'FATOR_REDUTOR_FINANCEIRO',
    'igd_pab_fator_redutor_conforme_saldo_f': 'FATOR_REDUTOR_FINANCEIRO',
    'mt_imp_rep_s': 'MOTIVO_IMPEDIMENTO',
    'igd_pab_motiv_imped_repasse_s': 'MOTIVO_IMPEDIMENTO',
    
    # --- Quantitativos de Público Alvo ---
    'igd_pbf_qtd_familias_cad_ate_meio_sm_i': 'QTD_FAMILIAS', 
    'igd_pab_qtd_familias_cad_ate_meio_sm_i': 'QTD_FAMILIAS',
    'igd_pbf_qtd_total_publico_saude_i': 'SAUDE_PUBLICO_TOTAL', 
    'igd_pab_qtd_total_publico_saude_i': 'SAUDE_PUBLICO_TOTAL',
    'igd_pbf_qtd_pessoas_cond_saude_informada_i': 'SAUDE_ACOMPANHADOS', 
    'igd_pab_qtd_pessoas_cond_saude_informada_i': 'SAUDE_ACOMPANHADOS',
    'igd_pbf_qtd_pessoas_com_freq_escolar_informada_i': 'EDUCACAO_ACOMPANHADOS', 
    'igd_pab_qtd_pessoas_com_freq_escolar_informada_i': 'EDUCACAO_ACOMPANHADOS'
}

def extrair_ano(nome_arquivo):
    """Extrai o ano do nome do arquivo (ex: calculos_2024.csv -> 2024)"""
    match = re.search(r'20\d{2}', nome_arquivo)
    return match.group(0) if match else "Indefinido"

def auditar_tudo():
    print("🕵️‍♂️ INICIANDO MONITORAMENTO ANUAL DE COMPORTAMENTO DE DADOS...")
    
    caminho_base = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "dados_brutos"))
    if not os.path.exists(caminho_base):
        print(f"❌ Erro: Pasta de dados não encontrada em: {caminho_base}")
        return

    pastas = ['CALCULOS', 'TAXAS', 'PUBLICO']
    
    # Define a gravação do log diretamente dentro de dados_tratados
    arquivo_saida = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "dados_tratados", "relatorio_colunas.txt"))
    
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write("============================================================\n")
        f.write("       RELATÓRIO DE AUDITORIA ANUAL E DATA QUALITY - TCC     \n")
        f.write("============================================================\n\n")
        
        for pasta in pastas:
            path_pasta = os.path.join(caminho_base, pasta)
            arquivos = sorted(glob.glob(os.path.join(path_pasta, "*.[cC][sS][vV]")))
            
            f.write(f"📁 PASTA TEMÁTICA: {pasta}\n")
            f.write("=" * 60 + "\n")
            
            print(f" > Escaneando pasta: {pasta}...")
            
            if not arquivos:
                f.write("⚠️ Nenhum arquivo CSV localizado nesta pasta.\n\n")
                continue
                
            for arq in arquivos:
                nome_arq = os.path.basename(arq)
                ano_arq = extrair_ano(nome_arq)
                
                f.write(f"📄 Arquivo: {nome_arq} [Safra: {ano_arq}]\n")
                f.write("-" * 60 + "\n")
                
                try:
                    # Detecção de Delimitador Dinâmico
                    with open(arq, 'r', encoding='latin1') as f_check:
                        primeira_linha = f_check.readline()
                        sep = ',' if ',' in primeira_linha else ';'
                    
                    # Leitura completa para análise volumétrica de nulos
                    df = pd.read_csv(arq, sep=sep, encoding='latin1', dtype=str)
                    df.columns = df.columns.str.strip().str.lower() # Normalização de colunas
                    
                    total_linhas = len(df)
                    f.write(f" -> Volume Total de Linhas (Nacional): {total_linhas}\n")
                    f.write(f" -> Total de Colunas Identificadas: {len(df.columns)}\n\n")
                    
                    f.write(f"{'STATUS':<8} | {'COLUNA ORIGINAL':<50} | {'MAPEAMENTO':<25} | {'TIPO':<10} | {'NULOS / MISSING':<15}\n")
                    f.write("-" * 115 + "\n")
                    
                    for col in df.columns:
                        # Identificação de Tipo Amostral Simples
                        amostra = df[col].dropna()
                        if idx_nulos := total_linhas - len(amostra):
                            pct_nulos = (idx_nulos / total_linhas) * 100
                            txt_nulos = f"{idx_nulos} ({pct_nulos:.1f}%)"
                        else:
                            txt_nulos = "0 (0.0%)"
                            
                        # Detecta o tipo predominante real dos caracteres preenchidos
                        tipo_detectado = "Object/Str"
                        if len(amostra) > 0:
                            exemplo = str(amostra.iloc[0]).replace(',', '.')
                            if exemplo.strip().replace('-', '').isdigit():
                                tipo_detectado = "Int"
                            else:
                                try:
                                    float(exemplo.strip())
                                    tipo_detectado = "Float"
                                except ValueError:
                                    pass
                        
                        # Tratamento Semântico no Mapa
                        if col in MAPA_COLUNAS_ATUAL:
                            status = "✅ [MAP]"
                            traducao = MAPA_COLUNAS_ATUAL[col]
                        else:
                            status = "⬜ [DISP]"
                            traducao = "Não Utilizada"
                            
                        f.write(f"{status:<8} | {col:<50} | {traducao:<25} | {tipo_detectado:<10} | {txt_nulos:<15}\n")
                        
                except Exception as e:
                    f.write(f"❌ Falha crítica na análise de metadados: {e}\n")
                
                f.write("\n" + "."*115 + "\n\n")
            f.write("\n" + "="*60 + "\n\n")

    print(f"\n🚀 Inspeção Concluída com Sucesso!")
    print(f"📄 Relatório de Data Quality gerado em: {arquivo_saida}")

if __name__ == "__main__":
    auditar_tudo()
    