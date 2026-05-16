
import pandas as pd
import psycopg2
import os 
from sqlalchemy import create_engine,INTEGER, VARCHAR, TIMESTAMP
from dotenv import load_dotenv
load_dotenv()


pd.set_option('display.max_columns', None)
caminho_do_arquivo = r"C:\Users\manue\OneDrive\Desktop\Data-Enginner\Pipeline-de-Dados-ANAC\Anac\Arquivo-Json\PecasAprovadas.json" #Caminho do seu arquivo Json
df = pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')
df.head()


#Colunas selecionadas:
colunas = ['ORG_NOME', 'PAPP_COD','PAPP_NOME' ,'PAPP_PN',
       'APAA_CODI', 'APAA_DATA', 'APAA_STATUS']
df[colunas].fillna('') #Limpeza dos valores NAN. 



DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Cria a URL de conexão  no .env(dialect+driver://user:password@host:port/dbname)
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(DATABASE_URL)

# Teste de conexão
try:
    with engine.connect() as connection:
        print("Conexão ao PostgreSQL bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar: {e}")


nome_tabela = 'anac_mapeamento' #Nome da tabela no banco de dados PostgreSQL

df.to_sql(nome_tabela, engine, index=False,if_exists='append',
 dtype={
                                      'ORG_NOME': VARCHAR(75),
                                      'PAPP_COD	': INTEGER,
                                     ' PAPP_NOME': VARCHAR(85),
                                     ' PAPP_PN': VARCHAR(85),
                                      'APAA_CODI':VARCHAR(85),
                                      'APAA_DATA':TIMESTAMP,
                                      'APPA_STATUS': VARCHAR(10)
                                
})
#Fecha a conexão:
engine.dispose()    


