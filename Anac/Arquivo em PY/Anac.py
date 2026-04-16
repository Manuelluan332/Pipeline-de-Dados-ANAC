
#Tratamento de dados: 
import pandas as pd     
pd.set_option('display.max_columns', None)   #Filtro das colunas  que queremos + Seu  arquivo salvo
#Caminho do seu arquivo Json
caminho_do_arquivo = r"C:\Users\manue\OneDrive\Desktop\Data-Enginner\Pipeline-de-Dados-ANAC\Anac\Arquivo-Json\PecasAprovadas.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')

df.head()  


colunas = ['ORG_NOME', 'PAPP_COD','PAPP_NOME' ,'PAPP_PN',
       'APAA_CODI', 'APAA_DATA', 'APAA_STATUS']
df = df[colunas]      
df.head()



df['APAA_DATA'] = pd.to_datetime(df['APAA_DATA'], errors='coerce')
df = df.astype(object).where(df.notnull(), None)


import   psycopg2

#Parametro de conexão:
dbname ='forca_aerea'          
user = 'postgres'
password = 'db123 '            
host = 'localhost'
port = '5432'

#Cria uma conexão:
conexao= psycopg2.connect( dbname=dbname,
							user=user,
							password=password,
							host=host,
							port=port)

#Cria uma cursor  para manipular os dados:
cursor = conexao.cursor()

#Delete base antes da Carga:
#cursor.execute(' delete from public.anac ')


#carga de dados:
for  indice,coluna_df in df.iterrows():
	cursor.execute( """ INSERT INTO anac  (
		ORG_NOME,
		PAPP_COD, 
		PAPP_NOME,
		PAPP_PN,
		APAA_CODI,
        APAA_DATA,
		APAA_STATUS
	) VALUES (%s,%s,%s,%s,%s,%s,%s)
		""",(
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



