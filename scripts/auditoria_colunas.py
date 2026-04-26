import pandas as pd
import os
import glob
import sys

# --- CORREÇÃO DO ERRO DE EMOJI (WINDOWS) ---
# Força o terminal a aceitar caracteres especiais (UTF-8)
sys.stdout.reconfigure(encoding='utf-8') # type: ignore

# --- 1. CONFIGURAÇÃO DO MAPA ATUAL ---
MAPA_COLUNAS_ATUAL = {
    'codigo_ibge': 'IBGE', 'anomes_s': 'COMPETENCIA',
    'igdm_f': 'TAXA_IGDM', 'igd_pab_igdm_f': 'TAXA_IGDM',
    'tx_atual_cad_f': 'TAXA_ATUALIZACAO', 'igd_pab_tac_f': 'TAXA_ATUALIZACAO',
    'tx_acomp_freq_escol_f': 'TAXA_FREQ_ESCOLAR', 'igd_pab_tafe_f': 'TAXA_FREQ_ESCOLAR',
    'tx_acomp_agenda_saude_f': 'TAXA_ACOMP_SAUDE', 'igd_pab_taas_f': 'TAXA_ACOMP_SAUDE',
    'vl_rep_mes_f': 'VALOR_REPASSADO', 'igd_pab_vl_repassado_igdm_f': 'VALOR_REPASSADO',
    'vl_cal_com_incent_f': 'VALOR_CALCULADO', 'igd_pab_vl_calculado_com_incentivos_f': 'VALOR_CALCULADO',
    'igd_pbf_qtd_familias_cad_ate_meio_sm_i': 'QTD_FAMILIAS', 
    'igd_pab_qtd_familias_cad_ate_meio_sm_i': 'QTD_FAMILIAS',
    'igd_pbf_qtd_total_criancas_adolescentes_pbf_i': 'QTD_CRIANCAS', 
    'igd_pab_qtd_total_criancas_adolescentes_pab_i': 'QTD_CRIANCAS',
    'igd_pbf_qtd_total_publico_saude_i': 'SAUDE_PUBLICO_TOTAL',
    'igd_pbf_qtd_pessoas_cond_saude_informada_i': 'SAUDE_ACOMPANHADOS',
    'igd_pab_qtd_total_publico_saude_i': 'SAUDE_PUBLICO_TOTAL',
    'idg_pab_qtd_total_publico_saude_i': 'SAUDE_PUBLICO_TOTAL',
    'igd_pab_qtd_pessoas_cond_saude_informada_i': 'SAUDE_ACOMPANHADOS',
    'idg_pab_qtd_pessoas_cond_saude_informada_i': 'SAUDE_ACOMPANHADOS',
    'igd_pbf_qtd_pessoas_com_freq_escolar_informada_i': 'EDUCACAO_ACOMPANHADOS',
    'igd_pab_qtd_pessoas_com_freq_escolar_informada_i': 'EDUCACAO_ACOMPANHADOS',
    'igd_pbf_fator_redutor_conforme_saldo_f': 'FATOR_REDUTOR_FINANCEIRO' 
}

def auditar_tudo():
    print("🕵️‍♂️ INICIANDO AUDITORIA COMPLETA DE COLUNAS...")
    
    # Tenta achar a pasta dados_brutos subindo um nível
    caminho_base = os.path.join(os.path.dirname(__file__), "..", "dados_brutos")
    caminho_base = os.path.abspath(caminho_base)
    
    if not os.path.exists(caminho_base):
        print(f"❌ Erro: Pasta de dados não encontrada em: {caminho_base}")
        return

    # Ordem de prioridade para análise
    pastas = ['CALCULOS', 'TAXAS', 'PUBLICO']
    
    # Prepara o arquivo de relatório na mesma pasta do script
    arquivo_saida = os.path.join(os.path.dirname(__file__), "relatorio_colunas.txt")
    
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write(f"RELATÓRIO DE AUDITORIA DE DADOS - TCC CAMPO BELO\n")
        f.write("="*60 + "\n\n")
        
        for pasta in pastas:
            path_pasta = os.path.join(caminho_base, pasta)
            # Busca case-insensitive para .csv ou .CSV
            arquivos = sorted(glob.glob(os.path.join(path_pasta, "*.[cC][sS][vV]")))
            
            f.write(f"📂 PASTA: {pasta}\n")
            f.write("-" * 60 + "\n")
            
            print(f" > Lendo pasta: {pasta}...") # Feedback no terminal
            
            if arquivos:
                arq_recente = arquivos[-1]
                nome_arq = os.path.basename(arq_recente)
                f.write(f"Arquivo analisado: {nome_arq}\n\n")
                
                try:
                    df = pd.read_csv(arq_recente, sep=',', encoding='latin1', dtype=str, nrows=0)
                    
                    ja_temos = []
                    disponiveis = []
                    
                    for col in df.columns:
                        if col in MAPA_COLUNAS_ATUAL:
                            ja_temos.append(f"✅ {col} -> {MAPA_COLUNAS_ATUAL[col]}")
                        else:
                            disponiveis.append(f"⬜ {col}")
                    
                    f.write(">>> COLUNAS JÁ MAPEADAS (UTILIZADAS):\n")
                    for item in ja_temos: f.write(f"{item}\n")
                    
                    f.write("\n>>> COLUNAS DISPONÍVEIS (NÃO UTILIZADAS):\n")
                    for item in disponiveis: f.write(f"{item}\n")
                    
                except Exception as e:
                    f.write(f"❌ Erro ao ler arquivo: {e}\n")
            else:
                f.write("⚠️ Nenhum arquivo CSV encontrado.\n")
            
            f.write("\n" + "="*60 + "\n\n")

    print(f"\n✅ Relatório gerado com sucesso!")
    print(f"📄 Abra o arquivo: {arquivo_saida}")

if __name__ == "__main__":
    auditar_tudo()
    