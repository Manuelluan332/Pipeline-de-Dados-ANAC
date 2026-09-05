import pandas as pd 
import psycopg2
import os 
import logging
from sqlalchemy import create_engine,INTEGER, VARCHAR,DATE
from dotenv import load_dotenv
load_dotenv()
from  pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#EXTRACT:
outh_path = Path(__file__).resolve().parent
json_path = outh_path.parent / "Arquivo_Json" / "PecasAprovadas.json"

try:
    print('--------')
    print('EXTRACT: ')
    print('--------')
    raw_data = pd.read_json(json_path, encoding="utf-8-sig")
    logging.info("Dados Extraidos com Sucesso!")

    print(raw_data.head())
    raw_data.head()
except Exception  as e:
   logging.error(f"Erro na extração dos dados: {e}")


#TRANFORM:
def Data_transformation(df:pd.DataFrame) -> pd.DataFrame:
  
   #Excluão de colunas desnecessárias:
     df = df.drop(
      columns=[
          'APAA_STATUS',
          'PAPP_OTP',
          'PAPP_REPOE',
          'PAPP_MAPROV',
          'PAPP_MODELOAER',
          'PAPP_TIPO',
          'PAPP_AUTORIDADE',
          'ORG_CODI',
          'PAPP_MODELO'
      ]
  )
   #Renomeação
     df = df.rename(
      columns={
          'ORG_NOME': 'Organization_Name',
          'PAPP_COD': 'Product_Code',
          'PAPP_NOME': 'Name_Product',
          'PAPP_PN': 'Part_Number',
          'APAA_CODI': 'Approval_Code',
          'APAA_DATA': 'Approval_Date',
          'ORG_NABREV_FAB_PRO': 'Organization_Manufactures_Product'
      }
      )

    # Conversão de datas:
     df['Approval_Date'] = pd.to_datetime(df['Approval_Date'],errors='coerce')
     df['Approval_Date'] = df['Approval_Date'].dt.strftime('%Y/%m/%d')

      
    #Remoção de valores nulls:
     df = df.fillna('')

     #Remoção de duplicatas: 
     df = df.drop_duplicates(subset=['Organization_Name','Product_Code','Name_Product'])

  
     return df 

try: 
   df_tranformation = Data_transformation(raw_data)
   print('----------')
   print('TRANFORM: ')
   print('----------')
   logging.info("Tranformação  dos dados feita com sucesso!")
   print(df_tranformation.head())
except Exception as e:
   logging.error(f"Error na Tranformação dos dados: {e}")   

#Execução para coluna 'Approval_Date' não apresentar error com strings vazias: 
df_tranformation['Approval_Date'] = pd.to_datetime(df_tranformation['Approval_Date'], errors='coerce')

#LOAD:

#Cria a URL de conexão  no .env(dialect+driver://user:password@host:port/dbname)
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# Teste de conexão:
try:
    with engine.connect() as connection:
        print('----------')
        print('LOARD: ')
        print('----------')
        logging.info("Conexão ao PostgreSQL bem-sucedida!")
except Exception as e:
    logging.error(f"Erro ao conectar: {e}")

table_name = 'anac' #Nome da tabela  criada  para o banco de dados:    
                                                 
df_tranformation.to_sql(table_name, engine, index=False,if_exists='append',
 dtype={
                                      'Organization_Name': VARCHAR(85),
                                      'Product_Code': INTEGER,
                                      'Name_Product': VARCHAR(85),
                                      'Part_Number': VARCHAR(85),
                                      'Approval_Code':VARCHAR(85),
                                      'Approval_Date':DATE,
                                      'Organization_Manufactures_Product': VARCHAR(85)   
                                                                  
})
#Fecha a conexão:
engine.dispose()  


