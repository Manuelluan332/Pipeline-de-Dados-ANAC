
import pandas as pd 
import psycopg2
import os
from dotenv  import load_dotenv 
load_dotenv()


caminho_arquivo = pd.read_json(r"C:\Users\manue\OneDrive\Desktop\Data-Enginner\Py-Testes\Scripts\PecasAprovadas.json",encoding='utf-8-sig')


#Colunas selecionadas:
colunas = ['ORG_NOME', 'PAPP_COD','PAPP_NOME' ,'PAPP_PN',
       'APAA_CODI', 'APAA_DATA', 'APAA_STATUS']
df= caminho_arquivo[colunas].fillna('') #Limpeza dos valores NAN. 
df.head()


df['APAA_DATA'] = pd.to_datetime(df['APAA_DATA'], errors='coerce')
df = df.astype(object).where(df.notnull(), None) #Python None é convertido para NULL pelo driver do banco (psycopg2/npgsql).


DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')


def conexao_banco_dados():
    try:
        conexao = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Conexão ao PostgreSQL bem-sucedida!")
        return conexao
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None 
    
conexao =conexao_banco_dados()


cursor = conexao.cursor()

#Delete base antes da Carga:
#cursor.execute(" delete from Anac")

#Carga dos Dados:
for indice,coluna_df in df.iterrows():
      cursor.execute( """  insert into  ANAC  (
				ORG_NOME,
				PAPP_COD,
				PAPP_NOME,
				PAPP_PN,
			    APAA_CODI,
				APAA_DATA,
				APAA_STATUS
		) VALUES (%s,%s,%s,%s,%s,%s,%s) 

		""", (
				coluna_df["ORG_NOME"],
				coluna_df["PAPP_COD"],
				coluna_df["PAPP_NOME"],
				coluna_df["PAPP_PN"],
				coluna_df["APAA_CODI"],
		    	coluna_df["APAA_DATA"],
				coluna_df["APAA_STATUS"]
		)
		 )

conexao.commit()
cursor.close()
conexao.close()


