import pandas as pd

pd.set_option('display.max_columns', None)
caminho_do_arquivo = r"C:\Users\manue\OneDrive\Desktop\Data-Enginner\Pipeline-de-Dados-ANAC\Anac\Arquivo-Json\PecasAprovadas.json" #Caminho do seu arquivo Json
df = pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')
df.head(3)

#Colunas selecionadas:
colunas = ['ORG_NOME', 'PAPP_COD','PAPP_NOME' ,'PAPP_PN',
       'APAA_CODI', 'APAA_DATA', 'APAA_STATUS']
df[colunas].head() 

#import psycopg2
from sqlalchemy import create_engine

dbname ='seu banco'          
user = 'seu usuario'
password = 'sua senha'            
host = 'localhost'
port = '5432'

#String de conexão:
conexao_str = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

#Criando uma conexão usando o SqlAlchemy:
engine = create_engine(conexao_str)

nome_tabela = 'anac_mapeamento' #Nome da tabela no banco de dados PostgreSQL

df.to_sql(nome_tabela, engine, index=False,if_exists='replace')

engine.dispose()
    