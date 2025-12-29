
import pandas as pd
import psycopg2

caminho_do_arquivo = r"C:\Users\manue\OneDrive\Desktop\Projeto_Anac-SGBDS\Anac\Arquivo Json\PecasAprovadas.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')

#Colunas selecionadas:
colunas = ['ORG_NOME', 'PAPP_COD','PAPP_NOME' ,'PAPP_PN',
       'APAA_CODI', 'APAA_DATA', 'APAA_STATUS', 'PAPP_REPOE']
[colunas]   
df.head()


from sqlalchemy import create_engine,delete

dbname = 'seu banco'           
user = 'seu usuario'
password = 'sua senha'          
host = 'localhost'
port = '5432'

#String de conexão:
conexao_str = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

#Criando uma conexão usando o SqlAlchemy:
engine = create_engine(conexao_str)

nome_tabela = 'Anac_sqlalchemy'

#Envia DataFrame para o banco  de dados:
df.to_sql(nome_tabela, engine, index=False, if_exists='replace')



#Fecha a conexão:
engine.dispose()


