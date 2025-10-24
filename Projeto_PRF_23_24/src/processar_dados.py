# Importando as bibliotecas
import pandas as pd
import os

def carregar_dados(diretorio_raw: str) -> pd.DataFrame:
    """
    Lê todos os arquivos CSV na pasta 'raw', adiciona uma coluna 'ano'
    e retorna um único DataFrame unificado
    """
    arquivos = [f for f in os.listdir(diretorio_raw) if f.endswith('.csv')]
    dataframes = []

    for arquivo in arquivos:
        caminho = os.path.join(diretorio_raw, arquivo)
        print(f'Carregado: {arquivo}')

        # Extraindo o ano do nome do arquivo
        ano = ''.join(filter(str.isdigit, arquivo))
    
        df = pd.read_csv(caminho, sep=';', low_memory=False, encoding='latin1')
        df['ano'] = int(ano) if ano else None # adiciona o ano ao DataSet

        dataframes.append(df)
    # Concatenando todos os DataFrames
    df_final = pd.concat(dataframes, ignore_index=True)
    return df_final


def salvar_dados(df: pd.DataFrame, diretorio_processado: str, nome_arquivo: str = 'dados_prf_consolidados.csv'):
    """
    Salvar o DataFrame consolidado na pasta 'processed'
    """
    os.makedirs(diretorio_processado, exist_ok=True)
    caminho_saida = os.path.join(diretorio_processado, nome_arquivo)
    df.to_csv(caminho_saida, sep=';', index=False, encoding='latin1')
    print(f'Arquivo consolidado, salvo em: {caminho_saida}')


if __name__ == '__main__':
    # Caminho base dinâmico (onde o Script está salvo)
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Diretórios padronizados
    caminho_raw = os.path.join(base_dir, '..', 'data', 'raw')
    caminho_processed = os.path.join(base_dir, '..', 'data', 'processed')

    print(f'Diretório Base: {base_dir}')
    print(f'Lendo Arquivos em: {caminho_raw}')

    # Executando
    df_consolidado = carregar_dados(caminho_raw)
    salvar_dados(df_consolidado, caminho_processed)
    print(f'Dados consolidados com sucesso! Total de linhas: {len(df_consolidado)}')